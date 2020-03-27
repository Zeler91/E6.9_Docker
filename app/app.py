import sys
import os
import json
from pymemcache.client import Client
from bottle import route
from bottle import run

def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2

def json_deserializer(key, value, flags):
   if flags == 1:
       return value.decode("utf-8")
   if flags == 2:
       return json.loads(value.decode("utf-8"))
   raise Exception("Unknown serialization format")

def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

port = int(os.environ.get("PORT", 5000))
client = Client(('memcached', 11211), serializer=json_serializer, deserializer=json_deserializer)

@route('/')
def hello_world():
    return "Hi, this is module E6.9! Add integer number after host adress, like this: http://0.0.0.0:8080/10"

@route("/<n:int>")
def fib_handler(n):
   fib_result = client.get(str(n))
   if(fib_result):
       result = fib_result
       return str(result)
   else:
        result = fib(n)
        client.set(str(n), result)
        return str(result)

if __name__ == "__main__":
    run(host="0.0.0.0", port=port, debug=True)
