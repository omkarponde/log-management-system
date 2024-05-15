from pydantic import BaseModel
from typing import Dict, Optional


class LogEntry(BaseModel):
    level: Optional[str]
    log_string: Optional[str]
    timestamp: Optional[str]
    metadata: Optional[Dict[str, str]]
