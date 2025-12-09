---
title: "Updated Carbon Methodology for the AWS Customer Carbon Footprint Tool (CCFT)"
date: 2025-10-16
weight: 2
chapter: false
pre: "<b> 3.2. </b>"
---

*(Based on the official AWS update from April 23, 2025)*

To support customers on their sustainability journey, AWS launched the **Customer Carbon Footprint Tool (CCFT)** in 2022. CCFT helps customers track and evaluate carbon emissions resulting from their AWS usage. It includes Scope 1 and Scope 2 emissions according to the Greenhouse Gas Protocol, covering all AWS services such as Amazon EC2, Amazon S3, AWS Lambda, and more.

Today, AWS announces three updates to CCFT:

1. Easier access to carbon data through Billing and Cost Management Data Exports.  
2. Detailed carbon data broken down by AWS Region.  
3. An updated allocation methodology (v2.0), independently assured by APEX.

Starting January 2025, CCFT uses methodology v2.0. Data from December 2024 and earlier will continue using v1.0.

---

# 1. Easier Data Access

Customers can now export CCFT carbon data via **AWS Data Exports**.

Key features:

- Provides emission estimates for all accounts under AWS Organizations.  
- Monthly automated exports delivered to Amazon S3 in CSV or Parquet.  
- First export includes up to 38 months of historical data.  

Pre-Dec 2024 data uses v1.0; January 2025 onward uses v2.0.

---

# 2. Regional Carbon Granularity

Customers can now view carbon emissions broken down by **AWS Region**.  
CloudFront usage is grouped under **Global Services**.

This enhancement allows customers to:

- Identify regions contributing the most carbon emissions  
- Make better workload placement decisions  

---

# 3. Updated Methodology v2.0

Customers often use services across many AWS Regions, making carbon attribution complex.

Methodology v2.0 is aligned with industry standards including:

- GHG Protocol Corporate Standard  
- GHG Protocol Product Standard  
- ISO 14040/44 (Life Cycle Assessment)  
- ISO 14067 (Product Carbon Footprint)  
- ICT Sector Guidance  

---

## Scope 1 Overview

Scope 1 includes direct emissions from AWS-owned or controlled sources such as backup generators.  
AWS collects annual Scope 1 operational data, calculates emissions at site level, then aggregates them into clusters (AWS Regions or CloudFront edge clusters).

---

## Scope 2 Overview

Scope 2 includes indirect emissions from purchased electricity.

CCFT uses:

- **Market-based** methodology  
- Geographic emission factors  
- Grid mix and carbon intensity values verified annually  

It follows the prioritization rules of the Greenhouse Gas Protocol.

---

## Allocation Model v2.0

Emission allocation follows three steps:

1. Allocate cluster-level emissions to server racks.  
2. Allocate rack emissions to AWS services based on resource usage and service dependencies.  
3. Allocate service emissions to individual customer accounts.

Some customers may see changes in their totals due to improved accuracy.

---

## Three Key Updates in Methodology v2.0

1. **Unused capacity is now allocated to all AWS customers.**  
   Carbon associated with unused server capacity is distributed proportionally, as required by GHG Protocol and ISO standards.

2. **Improved allocation logic for services without dedicated hardware**, such as AWS Lambda or Amazon Redshift.

3. **Updated allocation of shared overhead**, including networking racks and AWS Region expansions.

---

# Moving Forward

AWS will continue improving CCFT as new climate science, data, and customer needs evolve.

---

# Climate Pledge Commitment

AWS remains committed to reaching **net-zero carbon by 2040**.  
To learn more, visit the AWS sustainability site.
