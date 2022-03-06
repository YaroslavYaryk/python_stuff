import redis
import time

with redis.Redis() as redis_client:  # open redis connection
    redis_client.set(name="a", value="1")  # set value
    redis_client.set(name="ahahah", value="2")  # set value
    redis_client.set(name="aggg", value="3")  # set value

    print(redis_client.keys("a*"))


