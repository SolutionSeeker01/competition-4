import unittest

from app.connection_pool import ConnectionPool
from app.inventory import DatabaseTimeout, lookup_inventory


class InventoryIncidentTests(unittest.TestCase):

    def setUp(self):
        self.pool = ConnectionPool(max_connections=3)

    def test_known_sku_returns_stock(self):
        self.assertEqual(lookup_inventory("SKU-100", self.pool), 25)

    def test_unknown_sku_returns_zero(self):
        self.assertEqual(lookup_inventory("SKU-999", self.pool), 0)

    def test_successful_request_releases_connection(self):
        lookup_inventory("SKU-200", self.pool)
        self.assertEqual(self.pool.active_connections, 0)

    def test_database_timeout_releases_connection(self):
        with self.assertRaises(DatabaseTimeout):
            lookup_inventory(
                "SKU-100", self.pool, simulate_timeout=True
            )

        self.assertEqual(self.pool.active_connections, 0)

    def test_service_recovers_after_database_timeout(self):
        with self.assertRaises(DatabaseTimeout):
            lookup_inventory(
                "SKU-100", self.pool, simulate_timeout=True
            )

        self.assertEqual(lookup_inventory("SKU-100", self.pool), 25)
        self.assertEqual(self.pool.active_connections, 0)

    def test_pool_does_not_exhaust_after_repeated_timeouts(self):
        for _ in range(3):
            with self.assertRaises(DatabaseTimeout):
                lookup_inventory(
                    "SKU-100", self.pool, simulate_timeout=True
                )

        self.assertEqual(self.pool.active_connections, 0)
        self.assertEqual(lookup_inventory("SKU-300", self.pool), 0)


if __name__ == "__main__":
    unittest.main()