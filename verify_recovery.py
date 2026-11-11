from app.connection_pool import ConnectionPool
from app.inventory import DatabaseTimeout, lookup_inventory


def main():
    pool = ConnectionPool(max_connections=3)

    # Simulate three database timeouts.
    for attempt in range(3):
        try:
            lookup_inventory(
                "SKU-100",
                pool,
                simulate_timeout=True
            )
        except DatabaseTimeout:
            pass

        if pool.active_connections != 0:
            raise SystemExit(
                f"RECOVERY FAILED: {pool.active_connections} "
                f"connection(s) remain active after timeout "
                f"attempt {attempt + 1}."
            )

    # Verify that a normal request works after the failures.
    quantity = lookup_inventory("SKU-100", pool)

    if quantity != 25 or pool.active_connections != 0:
        raise SystemExit(
            "RECOVERY FAILED: normal request did not recover cleanly."
        )

    print("RECOVERY VERIFIED")
    print("Repeated database timeouts did not leak connections.")
    print("A normal inventory request succeeded after the timeouts.")
    print("FLAG{POOL_RELEASE_RECOVERED}")


if __name__ == "__main__":
    main()