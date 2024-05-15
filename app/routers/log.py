import json
import os
from fastapi import Query, APIRouter
from app.schemas import LogEntry
from typing import Optional, List

log_router = APIRouter(
    prefix="/log",
    tags=["Log"],
)


def read_logs(log_dir: str) -> List[LogEntry]:
    logs = []
    for root, dirs, files in os.walk(log_dir):
        for file_name in files:
            if file_name.endswith(".log"):
                with open(os.path.join(root, file_name), "r") as file:
                    for line in file:
                        try:
                            log = LogEntry(**json.loads(line.strip()))
                            logs.append(log)
                        except Exception as e:
                            # Skip log entries that fail to parse
                            pass
    return logs


logs_directory = "./logs/"  # Update this with your logs directory


@log_router.get("/")
async def query_logs(
        level: Optional[str] = Query(None, description="Filter logs by level"),
        log_string: Optional[str] = Query(None, description="Search for logs containing this string"),
        start_timestamp: Optional[str] = Query(None, description="Start timestamp of the time range"),
        end_timestamp: Optional[str] = Query(None, description="End timestamp of the time range"),
        metadata_source: Optional[str] = Query(None, description="Filter logs by metadata source")
):
    logs = read_logs(logs_directory)

    # Apply filters based on query parameters
    if level:
        logs = [log for log in logs if log.level == level]
    if log_string:
        logs = [log for log in logs if log_string in log.log_string]
    if metadata_source:
        logs = [log for log in logs if log.metadata.get("source") == metadata_source]
    if start_timestamp:
        logs = [log for log in logs if log.timestamp >= start_timestamp]
    if end_timestamp:
        logs = [log for log in logs if log.timestamp <= end_timestamp]

    return logs
