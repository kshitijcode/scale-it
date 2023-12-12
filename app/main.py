import asyncio
from core.application import Application
from core.autoscaler import AutoScaler
from core.config import AppConfig
from utils.logging import setup_logging
import logging


async def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    config = AppConfig()
    try:
        async with Application() as app:
            scaler = AutoScaler(app, config.target_cpu_usage)
            logger.info("Auto-scaler started")
            # Application Loop - Continuously poll the API Given for its
            #  current status and scale as needed.
            while True:
                new_replica_count = await scaler.scale()
                if new_replica_count is not None:
                    logger.info("Updating replica count to %s", new_replica_count)
                    await app.update_replicas(new_replica_count)
                await asyncio.sleep(config.poll_interval_seconds)
    except Exception as e:
        logger.error("An error occurred: %s", e, exc_info=True)

if __name__ == "__main__":
    asyncio.run(main())
