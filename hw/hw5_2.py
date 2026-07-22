import asyncio
import time


def async_timer(func):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = await func(*args, **kwargs)

        end = time.perf_counter()
        print(f"Время выполнения: {round(end - start, 2)} сек.")

        return result

    return wrapper


@async_timer
async def download_data():
    await asyncio.sleep(2)
    return "Данные загружены"


async def main():
    result = await download_data()
    print(result)


asyncio.run(main())