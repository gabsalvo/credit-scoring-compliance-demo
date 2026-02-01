# Model Card - Credit Scoring Model v2.1

## Model Details

| Property | Value |
|----------|-------|
| Name | CreditScore-XGB-v2.1 |
| Version | 2.1.0 |
| Type | Gradient Boosted Decision Tree |
| Framework | XGBoost 2.0.3 |
| Training Date | 2026-01-08 |
| Model Size | 4.2 MB |
| Inference Time | < 50ms (p99) |

### Model Architecture

- **Algorithm**: XGBoost with monotonic constraints
- **Trees**: 250 estimators
- **Max Depth**: 6
- **Learning Rate**: 0.05
- **Regularization**: L1=0.1, L2=1.0

## Intended Use

### Primary Use Case

Automated credit decision support for consumer loan applications in the range of $1,000 - $50,000. The model provides a risk score and recommended decision, which is reviewed by human underwriters for final approval.

### Users

- Automated decision pipeline (first-pass screening)
- Human underwriters (final decisions)
- Compliance team (monitoring and audit)

### Out-of-Scope Uses

This model should NOT be used for:
- Mortgage or large secured loan decisions
- Business or commercial lending
- Decisions without human oversight
- Jurisdictions outside the United States

## Training Data

- **Dataset**: Acme Credit Dataset v3.2
- **Records**: 2.4M training, 300K validation, 300K test
- **Time Period**: 2023-2025
- **Features**: 42 input features (see Data Card)

### Preprocessing

- Missing value imputation (median for numeric, mode for categorical)
- Outlier capping at 1st/99th percentiles
- One-hot encoding for categorical features
- Feature scaling (standardization)

## Evaluation

### Performance Metrics

| Metric | Test Set | Production (30-day) |
|--------|----------|---------------------|
| AUC-ROC | 0.847 | 0.841 |
| Accuracy | 0.792 | 0.788 |
| Precision | 0.813 | 0.807 |
| Recall | 0.756 | 0.749 |
| F1 Score | 0.783 | 0.777 |

### Calibration

- Brier Score: 0.142
- Expected Calibration Error: 0.023

### Fairness Evaluation

Evaluated across protected characteristics using disparate impact ratio (DIR) and equalized odds.

| Group | DIR | Equalized Odds Gap |
|-------|-----|-------------------|
| Gender | 0.94 | 0.02 |
| Age (protected) | 0.91 | 0.04 |
| Ethnicity | 0.89 | 0.05 |

All metrics within regulatory thresholds (DIR > 0.8).

### Robustness Testing

| Test | Result |
|------|--------|
| Data drift simulation | Stable (< 2% AUC drop) |
| Adversarial inputs | Robust (no significant manipulation) |
| Edge cases | 847/850 handled correctly |

## Explainability

### Global Feature Importance

| Rank | Feature | SHAP Importance |
|------|---------|-----------------|
| 1 | debt_to_income | 0.182 |
| 2 | credit_utilization | 0.156 |
| 3 | payment_history_score | 0.134 |
| 4 | account_age_months | 0.098 |
| 5 | inquiry_count_6mo | 0.087 |

### Local Explanations

Every prediction includes:
- Top 5 contributing factors (SHAP values)
- Plain-language explanation
- Confidence interval

## Limitations

1. **Performance Degradation**: May perform worse for thin-file applicants (< 2 years credit history)
2. **Economic Sensitivity**: Performance may degrade during economic downturns not represented in training data
3. **Feature Availability**: Requires all 42 features; partial inputs not supported
4. **Latency**: Not suitable for real-time interactive applications requiring < 10ms response

## Ethical Considerations

### Potential Harms

- False negatives may deny credit to qualified applicants
- False positives may expose lender to increased risk
- Systematic biases may disproportionately affect protected groups

### Mitigations

- Human review for all borderline decisions (score 0.4-0.6)
- Mandatory review for protected group members in borderline range
- Clear appeal process with human adjudication
- Regular bias audits with external review

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| AUC degradation | > 3% | PagerDuty |
| Prediction drift | > 10% | Slack |
| Fairness violation | DIR < 0.85 | Email + Jira |
| Latency p99 | > 100ms | PagerDuty |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.1.0 | 2026-01-08 | Added fairness constraints, updated training data |
| 2.0.0 | 2025-09-15 | Major architecture change to XGBoost |
| 1.5.0 | 2025-06-01 | Added SHAP explanations |
| 1.0.0 | 2025-01-10 | Initial production release |

## Contact

- **Model Owner**: ML Engineering Team
- **Compliance Contact**: compliance@acme-corp.com
- **Incident Response**: ml-incidents@acme-corp.com
