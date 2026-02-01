# Human Oversight Documentation

## Overview

This document describes the human oversight measures implemented for the Credit Scoring Model v2.1, ensuring compliance with EU AI Act Article 14 requirements for high-risk AI systems.

## System Classification

| Property | Value |
|----------|-------|
| Risk Category | High-Risk |
| EU AI Act Reference | Annex III, Section 5(b) |
| Oversight Level | Tier 1 (Enhanced) |

## Oversight Mechanisms

### 1. Real-time Monitoring

#### Automated Monitoring Dashboard

- **Location**: https://monitor.acme-corp.internal/credit-scoring
- **Refresh Rate**: Real-time (< 5 second latency)
- **Access**: Compliance Team, ML Engineering, Operations

#### Key Metrics Monitored

| Metric | Normal Range | Alert Threshold |
|--------|--------------|-----------------|
| Approval Rate | 65-72% | < 60% or > 78% |
| Avg Processing Time | 30-60ms | > 100ms |
| Error Rate | < 0.1% | > 0.5% |
| Fairness (DIR) | > 0.88 | < 0.85 |

#### Alert Channels

- **P1 (Critical)**: PagerDuty → On-call engineer
- **P2 (High)**: Slack #ml-alerts → Team response
- **P3 (Medium)**: Email → Next business day
- **P4 (Low)**: Dashboard only → Weekly review

### 2. Human-in-the-Loop (HITL)

#### Mandatory Review Cases

All decisions meeting the following criteria require human review:

| Trigger | Description | Reviewer |
|---------|-------------|----------|
| Borderline Score | Score between 0.40 - 0.60 | Level 1 Underwriter |
| High Value | Loan amount > $25,000 | Senior Underwriter |
| Protected Group + Borderline | Applicant in protected demographic with borderline score | Senior Underwriter + Compliance |
| Model Uncertainty | Confidence interval > 0.2 | Level 1 Underwriter |
| Anomaly Flag | Input flagged by anomaly detector | Senior Underwriter |

#### Review SLAs

| Priority | Review Time | Escalation |
|----------|-------------|------------|
| Standard | 4 business hours | Auto-escalate to senior |
| Expedited | 1 business hour | Manager notification |
| Compliance | 2 business hours | Compliance team CC |

### 3. Override Capabilities

#### Who Can Override

| Role | Override Scope | Approval Required |
|------|---------------|-------------------|
| Level 1 Underwriter | Individual decisions | None |
| Senior Underwriter | Individual + batch | None |
| Compliance Officer | Policy-level | Manager |
| Operations Manager | System-wide | VP + Compliance |

#### Override Process

1. **Initiate**: Reviewer clicks "Override Decision" in underwriting UI
2. **Document**: Mandatory fields: reason code, justification text, supporting evidence
3. **Approve**: System validates override authority
4. **Execute**: Original decision replaced, audit trail created
5. **Review**: Weekly override report to Compliance

#### Override Reason Codes

| Code | Reason | Typical Use |
|------|--------|-------------|
| OVR-001 | Additional documentation | Applicant provided new info |
| OVR-002 | Extenuating circumstances | Life events affecting credit |
| OVR-003 | Model limitation | Known model blind spot |
| OVR-004 | Policy exception | Approved policy deviation |
| OVR-005 | Error correction | System or data error |

### 4. System Shutdown ("Stop Button")

#### Shutdown Authority

| Level | Scope | Who |
|-------|-------|-----|
| Pause | Individual model | ML Engineer (on-call) |
| Disable | All automated decisions | Operations Manager |
| Emergency | Complete system halt | VP Engineering or Compliance Head |

#### Shutdown Triggers

- Fairness metric below 0.80 for any group
- Error rate exceeds 5%
- Regulatory notification received
- Security incident detected
- Production bug affecting decisions

#### Fallback Procedure

When model is disabled:
1. All new applications routed to manual queue
2. Underwriters notified via Slack + email
3. Applicants notified of processing delay
4. Estimated manual processing time communicated

## Roles and Responsibilities

### Compliance Officer

- **Reports To**: Chief Compliance Officer
- **Responsibilities**:
  - Daily review of fairness metrics
  - Weekly override audit
  - Monthly regulatory reporting
  - Incident investigation lead
  - External audit coordination

### ML Model Owner

- **Reports To**: VP Engineering
- **Responsibilities**:
  - Model performance monitoring
  - Incident response (technical)
  - Model update validation
  - Documentation maintenance

### Human Reviewers (Underwriters)

- **Reports To**: Operations Manager
- **Responsibilities**:
  - Timely review of flagged decisions
  - Override documentation
  - Escalation of edge cases
  - Feedback on model performance

## Training Requirements

### Initial Training

All personnel involved in oversight must complete:

| Course | Duration | Certification |
|--------|----------|---------------|
| AI Ethics Fundamentals | 4 hours | Required |
| Credit Decisioning | 8 hours | Required |
| EU AI Act Overview | 4 hours | Required |
| System Operations | 8 hours | Required |
| Override Procedures | 2 hours | Required |

### Ongoing Training

| Activity | Frequency | Audience |
|----------|-----------|----------|
| Refresher training | Quarterly | All |
| New feature training | As needed | Reviewers |
| Regulatory updates | As published | Compliance + Managers |
| Incident learnings | After incidents | Relevant teams |

## Escalation Procedures

### Escalation Matrix

```
Level 1: Individual Decision Issue
  → Reviewer → Senior Underwriter → Operations Manager

Level 2: Pattern/Trend Issue  
  → Compliance Officer → ML Model Owner → VP Engineering

Level 3: Systemic/Regulatory Issue
  → Chief Compliance Officer → General Counsel → CEO
```

### Escalation Triggers

| Trigger | Level | Timeline |
|---------|-------|----------|
| Single override denied | 1 | Immediate |
| >5 similar overrides in 24h | 2 | Within 4 hours |
| Fairness alert | 2 | Within 2 hours |
| Regulatory inquiry | 3 | Within 1 hour |
| Media/legal threat | 3 | Immediate |

## Audit Trail

### What We Log

Every interaction with the system is logged:

| Event Type | Data Captured |
|------------|---------------|
| Prediction | Input hash, output, confidence, timestamp, model version |
| Review | Reviewer ID, duration, decision, notes |
| Override | Original decision, new decision, reason, approver |
| Access | User, action, timestamp, IP |
| System | Config changes, deployments, alerts |

### Retention

| Log Type | Retention | Storage |
|----------|-----------|---------|
| Decision logs | 7 years | Encrypted S3 |
| Access logs | 3 years | CloudWatch |
| Audit reports | 10 years | Legal hold |

### Audit Reports

| Report | Frequency | Recipients |
|--------|-----------|------------|
| Decision summary | Daily | Operations |
| Override analysis | Weekly | Compliance |
| Fairness report | Monthly | Compliance + Legal |
| Full audit | Quarterly | Executive + Board |

## Contact Information

| Role | Contact | Availability |
|------|---------|--------------|
| On-call Engineer | PagerDuty #credit-ml | 24/7 |
| Compliance Officer | compliance@acme-corp.com | Business hours |
| Privacy Officer | privacy@acme-corp.com | Business hours |
| Legal Counsel | legal@acme-corp.com | Business hours |
| Emergency Hotline | +1-555-ACME-911 | 24/7 |

---

*Last Updated: January 15, 2026*
*Document Owner: Compliance Team*
*Review Cycle: Quarterly*
