class PoolExhausted(RuntimeError):
    """Raised when no database connections are available."""


class Connection:
    def __init__(self, connection_id):
        self.connection_id = connection_id


class ConnectionPool:
    def __init__(self, max_connections=3):
        if max_connections < 1:
            raise ValueError("max_connections must be at least 1")

        self.max_connections = max_connections
        self._active_ids = set()
        self._next_id = 1

    @property
    def active_connections(self):
        return len(self._active_ids)

    def acquire(self):
        if self.active_connections >= self.max_connections:
            raise PoolExhausted("database connection pool exhausted")

        connection = Connection(self._next_id)
        self._next_id += 1
        self._active_ids.add(connection.connection_id)

        return connection

    def release(self, connection):
        if connection.connection_id not in self._active_ids:
            raise ValueError("connection is not active or was already released")

        self._active_ids.remove(connection.connection_id)