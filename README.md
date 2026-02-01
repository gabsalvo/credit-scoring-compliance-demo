# Credit Scoring Model

A machine learning model for consumer credit scoring decisions.

## Overview

This repository contains the Credit Scoring Model v2.1, an XGBoost-based model
for automated credit decision support.

## Project Structure

```
credit-scoring/
├── src/
│   ├── model.py          # Model training and inference
│   ├── features.py       # Feature engineering
│   └── evaluate.py       # Model evaluation
├── compliance/           # EU AI Act compliance docs (added by annexci)
│   ├── RISK_REGISTER.yaml
│   ├── DATA_CARD.md
│   ├── MODEL_CARD.md
│   └── HUMAN_OVERSIGHT.md
├── tests/
│   └── test_model.py
├── annexci.yaml          # AnnexCI configuration
└── README.md
```

## Quick Start

```bash
# Train the model
python src/model.py train

# Run predictions
python src/model.py predict --input data/applications.csv

# Run compliance scan
annexci scan
```

## Compliance

This model is classified as **high-risk** under the EU AI Act (Annex III, Section 5(b))
as it is used for creditworthiness assessment.

To run a compliance scan:

```bash
annexci scan
```

## License

Proprietary - Acme Corporation
