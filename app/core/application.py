import aiohttp
from utils.decorator import retry
from core.config import AppConfig

config = AppConfig()

class Application:
    """
    Manages interactions with a web service using asynchronous HTTP requests. 
    This class handles initializing and closing client sessions, retrieving 
    the current status of the application, and updating the number of replicas.

    Attributes:
        config (AppConfig): Configuration settings for the application.
        session (aiohttp.ClientSession): The asynchronous HTTP session.
    """

    def __init__(self):
        """
        Initializes an Application instance. Sets up the configuration 
        using AppConfig and creates a new aiohttp.ClientSession.
        """
        self.config = config
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        """
        Asynchronous context manager entry method. Returns the application 
        instance when entering the context.

        Returns:
            Application: The instance of the Application class.
        """
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """
        Asynchronous context manager exit method. Closes the aiohttp.ClientSession 
        and handles any exceptions that occur, ensuring resource cleanup.

        Args:
            exc_type (Exception Type): Type of the exception.
            exc (Exception): Exception instance.
            tb (Traceback): Traceback object.
        """
        await self.session.close()

    @retry(config)
    async def get_current_status(self):
        """
        Retrieves the current status of the application from a specified endpoint.

        Decorated with @retry to handle potential request retries.

        Returns:
            dict: The response from the server, typically including the status of the application.
        
        Raises:
            HTTPException: If the request encounters an HTTP error.
        """
        async with self.session.get(f"{self.config.base_url}/app/status", headers={"Accept": "application/json"}) as response:
            response.raise_for_status()
            return await response.json()

    @retry(config)
    async def update_replicas(self, new_replica_count):
        """
        Updates the number of replicas for the application by sending a PUT request.

        Decorated with @retry to manage potential request retries.

        Args:
            new_replica_count (int): The new number of replicas to set.

        Raises:
            HTTPException: If the request encounters an HTTP error.
        """
        async with self.session.put(
            f"{self.config.base_url}/app/replicas",
            json={"replicas": new_replica_count},
            headers={"Content-Type": "application/json"}
        ) as response:
            response.raise_for_status()
