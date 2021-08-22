import redis
import json


def db_connect(host="localhost", port="6379"):  # default port = 6379

    try:
        conn = redis.StrictRedis(
            host=host,
            port=port,
            db=0)

    except Exception as ex:

        print('Error:', ex)

    return conn


def db_test(conn):
    try:
        conn.set("test", json.dumps(["success"]))
        print(json.loads(conn.get("test")))
    except Exception as ex:

        print('Error:', ex)


if __name__ == "__main__":
    conn = db_connect()
    db_test(conn)
