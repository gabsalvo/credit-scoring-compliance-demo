# Data Card - Credit Scoring Dataset

## Dataset Overview

| Property | Value |
|----------|-------|
| Name | Acme Credit Dataset v3.2 |
| Version | 3.2.0 |
| Size | 2.4M records |
| Last Updated | 2026-01-10 |
| Format | Parquet |
| License | Proprietary - Internal Use |

## Data Sources

The dataset is compiled from the following sources:

1. **Internal Application Data**: Customer credit applications submitted through web and mobile channels
2. **Credit Bureau Data**: Aggregated credit history from major bureaus (anonymized)
3. **Transaction History**: 24-month transaction patterns (aggregated metrics only)
4. **Public Records**: Bankruptcy and lien information from public sources

## Data Composition

### Features (42 total)

| Category | Count | Examples |
|----------|-------|----------|
| Demographic | 6 | Age bucket, employment status, housing type |
| Financial | 18 | Income range, debt-to-income, credit utilization |
| Behavioral | 12 | Payment history score, account age, inquiry count |
| Derived | 6 | Risk segment, stability score, trend indicators |

### Target Variable

- **credit_decision**: Binary (approved/denied)
- **Distribution**: 68% approved, 32% denied

### Demographic Distribution

| Group | Representation |
|-------|----------------|
| Age 18-25 | 15% |
| Age 26-40 | 42% |
| Age 41-60 | 31% |
| Age 60+ | 12% |

## Collection Process

- **Time Period**: January 2023 - December 2025
- **Geographic Scope**: United States (all 50 states)
- **Collection Method**: Automated pipeline with manual validation
- **Sampling**: Stratified by region and risk segment

## Data Quality

| Metric | Value |
|--------|-------|
| Missing Values | < 0.5% |
| Duplicate Records | 0% (deduped) |
| Validation Pass Rate | 99.7% |
| Freshness | Updated weekly |

### Quality Controls

- Automated schema validation on ingestion
- Statistical anomaly detection for drift
- Manual review of edge cases
- Quarterly data quality audits

## Privacy & Consent

### Compliance

- ✅ GDPR compliant (EU customers)
- ✅ CCPA compliant (California customers)
- ✅ FCRA compliant (credit reporting)

### Data Protection Measures

- All PII removed or pseudonymized
- k-anonymity (k=50) for demographic fields
- Differential privacy for aggregate statistics
- Access controls with audit logging

### Consent

All data subjects provided explicit consent for:
- Credit decision processing
- Model training (anonymized)
- Compliance reporting (aggregated)

## Intended Use

### Approved Uses

- Credit decision support for consumer loans
- Risk segmentation for pricing
- Compliance reporting and audits
- Model fairness evaluation

### Prohibited Uses

- Marketing or advertising targeting
- Employment decisions
- Insurance underwriting
- Resale to third parties

## Known Limitations

1. **Geographic Bias**: Underrepresentation of rural areas
2. **Temporal Shift**: Pre-2024 data may not reflect current economic conditions
3. **Feature Gaps**: Self-employment income verification limited
4. **Label Quality**: Some historical decisions may reflect outdated policies

## Maintenance

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Data refresh | Weekly | Data Engineering |
| Quality audit | Monthly | Data Quality Team |
| Bias assessment | Quarterly | ML Fairness Team |
| Full review | Annually | Compliance |
