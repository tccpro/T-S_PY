from redis import Redis
import json

redis_connection = Redis()

redis_connection.mset({'mykey':json.dumps({'token':'Se2ermkewkmrkfwfwljnwfnwkergkjekqwdokfmdwe'})})


# print(redis_connection.get('mykey'))

# redis_connection.delete('mykey')

# print(redis_connection.keys())
