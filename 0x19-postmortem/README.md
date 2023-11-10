# Web Stack Outage Postmortem

## Issue Summary:

- **Duration:**
  - Start Time: November 5, 2023, 09:00 UTC
  - End Time: November 5, 2023, 11:15 UTC
- **Impact:**
  - The product search feature experienced a temporary disruption, impacting 20% of users unable to perform successful searches.

## Timeline:

- **Issue Detected:**
  - November 5, 2023, 09:00 UTC
- **Detection Method:**
  - Automated monitoring systems triggered alerts, signaling an abnormal increase in failed product search attempts.
- **Actions Taken:**
  - Investigated logs related to the product search service, identifying a potential bottleneck in its interaction with the database.
  - Initially considered network configurations, suspecting a connectivity issue.
- **Misleading Paths:**
  - Explored network configurations, eventually ruling out connectivity issues.
  - Escalated the matter to the database team for a thorough examination.
- **Escalation:**
  - Engaged the database team for a more in-depth investigation.
- **Resolution:**
  - Determined that the product search service was overwhelmed by concurrent requests.
  - Implemented code optimizations to enhance its scalability and handle increased search volumes efficiently.

## Root Cause and Resolution:

- **Root Cause:**
  - High concurrent search requests led to performance degradation in the product search service.
- **Resolution:**
  - Enhanced the product search service by optimizing its code to efficiently manage increased search loads.

## Corrective and Preventative Measures:

- **Improvements/Fixes:**
  - Conduct a comprehensive code review across all services to identify potential bottlenecks.
  - Implement additional monitoring for product search service performance to proactively identify anomalies.
- **Tasks:**
  - Apply necessary patches to Nginx to better handle increased load during peak usage.
  - Implement robust monitoring solutions for server memory and database connection usage.


