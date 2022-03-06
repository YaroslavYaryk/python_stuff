import redis
from string import ascii_letters

with redis.Redis() as redis_client:  # open redis connection
    # for elem in range(20):
    #     redis_client.set(name=str(elem), value=ascii_letters[elem])
    a = redis_client.scan_iter( )
    b = redis_client.scan_iter(match="*", count=5)
    print(a) #returns generator of all keys in redis db
    for elem in a:
        try:
            print(elem, redis_client.get(elem))
        except Exception as e:
            print(f"wrong elem {elem}")