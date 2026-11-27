"""Shared data formats. Agree these on day 1 (see docs/formats.md) before building on them."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Flow(BaseModel):
    """One flow record sent by the sensor (subset of CICFlowMeter output)."""

    sensor_id: str
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    protocol: int = Field(description="IANA protocol number, e.g. 6 = TCP, 17 = UDP")
    timestamp: datetime = Field(description="Flow start time, UTC")
    duration_ms: float
    features: dict[str, float] = Field(
        default_factory=dict, description="Remaining CICFlowMeter features used by the model"
    )


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class DetectionType(str, Enum):
    known_attack = "Known attack"  # Random Forest
    anomaly = "Anomaly"  # Isolation Forest


class AlertStatus(str, Enum):
    new = "New"
    in_progress = "In progress"
    escalated = "Escalated"
    closed = "Closed"


class Disposition(str, Enum):
    true_positive = "True Positive"
    benign_positive = "Benign Positive"
    false_positive = "False Positive"


class Alert(BaseModel):
    id: int
    created_at: datetime
    severity: Severity
    confidence: float = Field(ge=0, le=1)
    detection_type: DetectionType
    attack_category: str | None = Field(None, description="None for Anomaly alerts")
    status: AlertStatus = AlertStatus.new
    disposition: Disposition | None = None
    disposition_reason: str | None = None
    assigned_to: int | None = None
    flow: Flow
