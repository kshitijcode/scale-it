import logging

logger = logging.getLogger(__name__)

class AutoScaler:
    """
     Auto-Scaler to manage scaling of an application based on CPU usage.
    """
    def __init__(self, application, target_cpu_usage=0.80):
        self.application = application
        self.target_cpu_usage = target_cpu_usage
        logger.info(f"AutoScaler initialized with target CPU usage: {self.target_cpu_usage}")

    async def scale(self):
        """
        Scale the application based on current CPU usage.
        """
        logger.debug("Fetching current status for scaling decision.")
        status = await self.application.get_current_status()
        if status:
            current_cpu_usage = status["cpu"]["highPriority"]
            current_replicas = status["replicas"]
            logger.info(f"Current CPU usage: {current_cpu_usage}, Current replicas: {current_replicas}")

            # IF CPU usage is above target, scale up by 1
            if current_cpu_usage > self.target_cpu_usage:
                new_replicas = current_replicas + 1
                logger.info(f"CPU usage is high. Scaling up to {new_replicas} replicas.")
                return new_replicas
            # IF CPU usage is below target, scale down by 1
            elif current_cpu_usage < self.target_cpu_usage:
                new_replicas = max(1, current_replicas - 1)
                logger.info(f"CPU usage is low. Scaling down to {new_replicas} replicas.")
                return new_replicas
            else:
                # No action required
                logger.info("CPU usage is optimal. No scaling action required.")
                return current_replicas
        else:
            logger.warning("Failed to fetch current status. No scaling action will be taken.")
            return None
