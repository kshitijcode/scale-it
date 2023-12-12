import os
from pydantic import BaseModel


class AppConfig(BaseModel):
    base_url: str = os.getenv("BASE_URL", "http://localhost:8123")
    target_cpu_usage: float = float(os.getenv("TARGET_CPU_USAGE", "0.80"))
    poll_interval_seconds: int = int(os.getenv("POLL_INTERVAL_SECONDS", "5"))
    retry_attempts: int = int(os.getenv("RETRY_ATTEMPTS", "3"))
    retry_delay: int = int(os.getenv("RETRY_DELAY", "1"))
