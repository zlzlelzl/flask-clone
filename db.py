import redis

try:

    conn = redis.StrictRedis(

        host='192.168.10.100',

        port=6379,

        db=2)

    print('Set Record:', conn.set("test", "Nice to meet you"))

    print('Get Record:', conn.get("test"))

    print('Delete Record:', conn.delete("test"))

    print('Get Deleted Record:', conn.get("test"))

except Exception as ex:

    print('Error:', ex)
