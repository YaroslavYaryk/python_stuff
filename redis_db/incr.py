import redis
import time

with redis.Redis() as redis_client:  # open redis connection
    redis_client.set(name="a", value=1)  # set value

    while int(redis_client.get("a")) < 100:
        redis_client.incr("a", 10) # increase value on 5
        redis_client.incrby("a", 5)  # increase value on 5
        print(redis_client.get("a").decode())
        time.sleep(0.1)
