---
title: "Blog 2"
date: 2025-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---
# Enabling Observability-First Operations at ScaleEnhance Data Visibility with Cribl Search and Amazon Managed Grafana
*by Rizwan Mushtaq, Kamilo "Kam" Amir, Sunil Ramachandra, and Aswin Vasudevan on 12 SEP 2025*

Observability is no longer a “nice to have” — it is a prerequisite to ensure systems operate securely, efficiently, and at scale. With the growing volume of logs, metrics, and security events, collecting, processing, and visualizing data in an organized way has become a challenge for many organizations. AWS, in partnership with Cribl Search, provides a centralized, flexible, and customizable observability pipeline — transforming raw data into actionable insights to drive faster, more confident decision-making at scale.

---

## Architecture Guidance

Below are the main components and how the integration between Cribl Search and Amazon Managed Grafana works:

---

| component              | Main role                                                                                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cribl Search           | Enables “in-place” search across multiple data sources ( Amazon S3, Cribl Lake, Amazon Security Lake, and AWS native services).<br /> No need to index all the data before searching.              |
| Amazon Managed Grafana | A powerful visualization tool: dashboards, real-time monitoring, and drill-down metrics/logs for troubleshooting. <br />Integrated with a plugin for Cribl Search to query data directly from Cribl. |

---

## Key Use Cases


Some scenarios where this solution is particularly useful:

1. **Cloud Infrastructure Monitoring**

   You can query data from AWS services via API or at rest, use Cribl to filter the required events, and then send them to a SIEM system or directly to Grafana dashboards to monitor health, resource performance, and costs.
2. **Application Performance Management (APM)**

   Dashboards display latency, error rates, and user experience, with the ability to drill down into specific transactions. Grafana makes it clear and quick to identify application issues that need to be addressed.
3. **Operations & Security (SecOps)**

   Security events are displayed in dedicated dashboards; Cribl supports continuous monitoring, compliance reporting, threat detection, and investigation workflows — helping SOC teams respond quickly to incidents.

## Implementation Walkthrough

To set up and run the solution, the basic steps are as follows:

1. **Preparation**
- An AWS account with administrative privileges.
- An S3 bucket (e.g., to store VPC Flow Logs) configured properly so services can write to it.
- A Cribl Cloud account and the necessary IAM/credentials.
2. **Authentication Setup (API Auth)**
- Create a token / API credentials in Cribl so that Grafana can connect securely.
3. **Install Cribl Search Plugin in Grafana**
- Go to the Plugins section in Amazon Managed Grafana, find the “Cribl Search” plugin, and add the connection using Cribl credentials.
4. **Create Dashboards & Visualizations**
- Example: view VPC Flow Logs from the last 15 minutes, grouped by log status per minute.
  - Switch to table view to analyze specific logs, detect anomalies, and trace request paths.
5. **Cleanup & Cost Management**
- Delete unused resources: S3 bucket, Flow Log configurations, and temporary Cribl settings to avoid unnecessary costs.


---

## Benefits & Challenges

**Benefits:**

- Reduce unnecessary storage/routing costs since only meaningful data is processed in-depth.

- Faster incident response & analysis with real-time dashboards and drill-down logs.

- Better control & compliance: all data and security events can be monitored.

- High flexibility: users can freely choose data sources, customize visualizations, and define routing needs.

**Challenges:**

- Proper security setup (credentials, access rights) is required to prevent data leaks or unauthorized access.

- Data routing must be managed to avoid sending too much raw data to Grafana or SIEM.

- Pipeline monitoring is necessary to ensure no misrouted, duplicated, or dropped messages.

---



## New Features in the Solution

### 1. AWS CloudFormation Cross-Stack References

Example *outputs* in the core microservice:

```yaml
Outputs:
  CriblSearchDatasourceARN:
    Value: !Ref CriblSearchDatasource
    Export:
      Name: !Sub ${AWS::StackName}-CriblSearchDatasource

  GrafanaWorkspaceId:
    Value: !Ref GrafanaWorkspace
    Export:
      Name: !Sub ${AWS::StackName}-GrafanaWorkspaceId

  VPCFlowLogsBucket:
    Value: !Ref VPCFlowLogsBucket
    Export:
      Name: !Sub ${AWS::StackName}-VPCFlowLogsBucket
```
