from fabric import Connection

conn = Connection("vnr@192.168.0.21", connect_kwargs={"password": "1234"})

conn.run()