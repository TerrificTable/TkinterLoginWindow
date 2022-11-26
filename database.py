
class Database(object):
    host=""
    username=""
    password=""
    database=""

    def __init__(self, host, username, password, database) -> None:
        self.host = host
        self.username = username
        self.password = password
        self.database = database
