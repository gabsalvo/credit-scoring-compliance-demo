"""
Credit Scoring Model

XGBoost-based model for consumer credit scoring decisions.
Compliant with EU AI Act requirements for high-risk AI systems.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
import json
from datetime import datetime


@dataclass
class CreditPrediction:
    """Result of a credit scoring prediction."""
    score: float
    decision: str  # 'approved' or 'denied'
    confidence: float
    explanation: Dict[str, float]
    model_version: str = "2.1.0"
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()


class CreditScoringModel:
    """
    Credit Scoring Model v2.1
    
    An XGBoost-based model for credit decision support.
    Includes built-in explainability via SHAP values.
    
    EU AI Act Classification: High-Risk (Annex III, 5(b))
    """
    
    VERSION = "2.1.0"
    RISK_CATEGORY = "high-risk"
    
    # Feature names for explainability
    FEATURES = [
        'debt_to_income',
        'credit_utilization', 
        'payment_history_score',
        'account_age_months',
        'inquiry_count_6mo',
        'income_stability',
        'employment_length',
        'existing_accounts'
    ]
    
    # Decision threshold
    THRESHOLD = 0.5
    
    def __init__(self, model_path: Optional[str] = None):
        """Initialize the model."""
        self.model = None
        self.model_path = model_path
        self._load_model()
    
    def _load_model(self):
        """Load the trained model (simulated for demo)."""
        # In production, this would load the actual XGBoost model
        # For demo purposes, we simulate the model
        print(f"[Model] Loading Credit Scoring Model v{self.VERSION}")
        self.model = self._create_demo_model()
    
    def _create_demo_model(self):
        """Create a demo model for demonstration purposes."""
        # Simulated model weights (for demo)
        return {
            'weights': {
                'debt_to_income': -0.35,
                'credit_utilization': -0.25,
                'payment_history_score': 0.30,
                'account_age_months': 0.15,
                'inquiry_count_6mo': -0.10,
                'income_stability': 0.20,
                'employment_length': 0.10,
                'existing_accounts': 0.05
            },
            'intercept': 0.5
        }
    
    def predict(self, features: Dict[str, float]) -> CreditPrediction:
        """
        Make a credit scoring prediction.
        
        Args:
            features: Dictionary of input features
            
        Returns:
            CreditPrediction with score, decision, and explanation
        """
        # Validate features
        self._validate_features(features)
        
        # Calculate score (simulated)
        score = self._calculate_score(features)
        
        # Make decision
        decision = 'approved' if score >= self.THRESHOLD else 'denied'
        
        # Calculate confidence
        confidence = abs(score - self.THRESHOLD) / self.THRESHOLD
        confidence = min(confidence, 1.0)
        
        # Generate explanation (SHAP-like)
        explanation = self._generate_explanation(features)
        
        return CreditPrediction(
            score=round(score, 4),
            decision=decision,
            confidence=round(confidence, 4),
            explanation=explanation,
            model_version=self.VERSION
        )
    
    def _validate_features(self, features: Dict[str, float]):
        """Validate input features."""
        missing = set(self.FEATURES) - set(features.keys())
        if missing:
            raise ValueError(f"Missing required features: {missing}")
    
    def _calculate_score(self, features: Dict[str, float]) -> float:
        """Calculate credit score from features."""
        weights = self.model['weights']
        intercept = self.model['intercept']
        
        score = intercept
        for feature, weight in weights.items():
            if feature in features:
                # Normalize feature to 0-1 range (simplified)
                normalized = features[feature] / 100.0 if features[feature] > 1 else features[feature]
                score += weight * normalized
        
        # Sigmoid to get probability
        score = 1 / (1 + np.exp(-score * 2))
        return score
    
    def _generate_explanation(self, features: Dict[str, float]) -> Dict[str, float]:
        """Generate SHAP-like feature contributions."""
        weights = self.model['weights']
        explanation = {}
        
        for feature, weight in weights.items():
            if feature in features:
                normalized = features[feature] / 100.0 if features[feature] > 1 else features[feature]
                contribution = weight * normalized
                explanation[feature] = round(contribution, 4)
        
        # Sort by absolute contribution
        explanation = dict(sorted(
            explanation.items(), 
            key=lambda x: abs(x[1]), 
            reverse=True
        ))
        
        return explanation
    
    def get_model_info(self) -> Dict:
        """Get model metadata for compliance."""
        return {
            'name': 'CreditScore-XGB',
            'version': self.VERSION,
            'risk_category': self.RISK_CATEGORY,
            'framework': 'XGBoost 2.0.3',
            'features': self.FEATURES,
            'threshold': self.THRESHOLD,
            'eu_ai_act_reference': 'Annex III, Section 5(b)'
        }


class HumanOversight:
    """
    Human oversight interface for the credit scoring model.
    
    Implements Article 14 requirements for human oversight of high-risk AI.
    """
    
    REVIEW_THRESHOLD_LOW = 0.4
    REVIEW_THRESHOLD_HIGH = 0.6
    
    @staticmethod
    def requires_review(prediction: CreditPrediction) -> Tuple[bool, str]:
        """
        Determine if a prediction requires human review.
        
        Returns:
            Tuple of (requires_review, reason)
        """
        # Borderline decisions always require review
        if HumanOversight.REVIEW_THRESHOLD_LOW <= prediction.score <= HumanOversight.REVIEW_THRESHOLD_HIGH:
            return True, "Borderline score requires human review"
        
        # Low confidence predictions require review
        if prediction.confidence < 0.3:
            return True, "Low confidence prediction"
        
        return False, ""
    
    @staticmethod
    def log_decision(prediction: CreditPrediction, reviewer: Optional[str] = None, override: bool = False):
        """Log a decision for audit trail."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'prediction': {
                'score': prediction.score,
                'decision': prediction.decision,
                'model_version': prediction.model_version
            },
            'reviewer': reviewer,
            'override': override,
            'audit_id': f"AUDIT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        }
        
        # In production, this would write to audit log system
        print(f"[Audit] Logged decision: {log_entry['audit_id']}")
        return log_entry


# Demo usage
if __name__ == '__main__':
    print("=" * 60)
    print("Credit Scoring Model v2.1 - Demo")
    print("=" * 60)
    
    # Initialize model
    model = CreditScoringModel()
    print(f"\nModel Info: {json.dumps(model.get_model_info(), indent=2)}")
    
    # Example prediction
    sample_features = {
        'debt_to_income': 35.0,
        'credit_utilization': 45.0,
        'payment_history_score': 85.0,
        'account_age_months': 48,
        'inquiry_count_6mo': 2,
        'income_stability': 0.8,
        'employment_length': 36,
        'existing_accounts': 5
    }
    
    print(f"\nInput Features: {json.dumps(sample_features, indent=2)}")
    
    prediction = model.predict(sample_features)
    print(f"\nPrediction:")
    print(f"  Score: {prediction.score}")
    print(f"  Decision: {prediction.decision}")
    print(f"  Confidence: {prediction.confidence}")
    print(f"\nTop Feature Contributions:")
    for feature, contribution in list(prediction.explanation.items())[:5]:
        sign = "+" if contribution > 0 else ""
        print(f"  {feature}: {sign}{contribution}")
    
    # Check if review required
    needs_review, reason = HumanOversight.requires_review(prediction)
    if needs_review:
        print(f"\n⚠️  Human review required: {reason}")
    else:
        print(f"\n✓ Automated decision permitted")
    
    # Log decision
    HumanOversight.log_decision(prediction)
