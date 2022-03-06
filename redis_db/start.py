import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)  # open redis connection

print(redis_client.set(name="name", value="value", ex=30))  # set value by key
print(redis_client.get("name").decode())  # get value and decode it
print(redis_client.keys("*"))  # get all keys in redis db
redis_client.close()  # closw connection
