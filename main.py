import asyncio
import logging
import sys

from bot import run_bot


async def main() -> None:
    await run_bot()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
