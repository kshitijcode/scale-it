import asyncio
import logging
from aiohttp import ClientError
from core.config import AppConfig  # Import AppConfig

logger = logging.getLogger(__name__)

def retry(config: AppConfig):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(config.retry_attempts):
                try:
                    return await func(*args, **kwargs)
                except ClientError as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} for {func.__name__} failed - {e}")
                    if attempt == config.retry_attempts - 1:
                        raise last_exception
                    await asyncio.sleep(config.retry_delay)
        return wrapper
    return decorator
