from app.connection_pool import ConnectionPool


class DatabaseTimeout(TimeoutError):
    """Represents a database query timeout."""


STOCK = {
    "SKU-100": 25,
    "SKU-200": 8,
    "SKU-300": 0,
}


def lookup_inventory(sku, pool=None, simulate_timeout=False):
    if pool is None:
        pool = ConnectionPool()

    connection = pool.acquire()
    try:
        if simulate_timeout:
            raise DatabaseTimeout("inventory query exceeded 4 second timeout")

        result = STOCK.get(sku, 0)
        return result
    finally:
        pool.release(connection)
