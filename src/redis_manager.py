import redis

class RedisManager:
    def __init__(self, host='localhost', port=6379, db_alias="database", db=0):
        self.host = "172.22.0.5" #host
        self.port = port
        self.db = db
        self.db_alias = db_alias
        self.redis_client = None

    def connect(self) -> bool:  
        self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)
        try:
            self.redis_client.ping()
            print("Connected to Redis")
            return True
        except redis.ConnectionError:
            print("Failed to connect to Redis")
            return False

    def get(self, key):
        if self.redis_client:
            value = self.redis_client.get(key)
            if value:
                return value.decode('utf-8')
            else:
                print(f"Key '{key}' not found.")
        else:
            print("Not connected to Redis")

    def disconnect(self):
        if self.redis_client:
            self.redis_client.close()
            self.redis_client = None
            print("Disconnected from Redis")