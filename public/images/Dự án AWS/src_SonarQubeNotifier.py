import json
import boto3
from datetime import datetime

# SNS client
sns_client = boto3.client('sns')
SNS_TOPIC_ARN = "arn:aws:sns:ap-southeast-2:788372363987:devops-aws-sns"

# Security Hub client
securityhub = boto3.client('securityhub', region_name='ap-southeast-2')

def lambda_handler(event, context):
    try:
        print("Incoming event:", json.dumps(event))  # Debug log

        # Parse JSON payload từ SonarQube
        body_raw = event.get("body", "{}")
        body = json.loads(body_raw)

        project = body.get("project", {})
        quality = body.get("qualityGate", {})

        project_name = project.get("name", "Unknown Project")
        project_key = project.get("key", "unknown-key")
        project_url = project.get("url", "No URL")
        project_url = project_url.replace("localhost", "54.206.11.79")
        quality_status = quality.get("status", "UNKNOWN")

        # ------------------------
        # 1️⃣ Gửi SNS
        # ------------------------
        message = (
            "📢 *SonarQube Quality Gate Notification*\n\n"
            f"🏷️ Project: {project_name}\n"
            f"🧩 Key: {project_key}\n"
            f"📊 Quality Gate Status: *{quality_status}*\n"
            f"🔗 URL: {project_url}\n\n"
            "— Sent automatically from AWS Lambda"
        )

        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=f"SonarQube Quality Gate Result: {quality_status}"
        )

        # ------------------------
        # 2️⃣ Gửi Security Hub Finding nếu QualityGate FAIL
        # ------------------------
        if quality_status != "OK":
            account_id = context.invoked_function_arn.split(":")[4]
            timestamp = datetime.utcnow().isoformat() + "Z"

            finding = {
                "SchemaVersion": "2018-10-08",
                "Id": f"sonarqube-{project_key}-{int(datetime.utcnow().timestamp())}",
                "ProductArn": f"arn:aws:securityhub:ap-southeast-2:{account_id}:product/{account_id}/default",
                "GeneratorId": "sonarqube-quality-gate",
                "AwsAccountId": account_id,
                "Types": ["Software and Configuration Checks/Code Vulnerability"],
                
                "CreatedAt": timestamp,
                "UpdatedAt": timestamp,
                "Severity": {"Label": "HIGH"},
                
                "Title": f"SonarQube Quality Gate Failed: {project_name}",
                "Description": (
                    f"SonarQube detected a Quality Gate FAILURE.\n"
                    f"Project: {project_name}\n"
                    f"Status: {quality_status}\n"
                    f"URL: {project_url}"
                ),
                "Resources": [
                    {
                        "Type": "Other",
                        "Id": project_key,
                        "Details": {"Other": {"ProjectURL": project_url}}
                    }
                ],
            }

            securityhub.batch_import_findings(Findings=[finding])

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Webhook processed successfully"})
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
