import asyncio
import logging

from src.config.db.postgres.init_db import init_db
from src.main import main


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
