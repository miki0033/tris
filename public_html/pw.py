import hashlib

SECRET_KEY = b"f6c23211b07568ace2707f28180429677fe1b34d6b1ba04a6114243781fbd4f2"
DBHOST = "localhost"
DBUSER = "root"
DBPW = "mikiko"
DB = "tris"


def pwEncode(pw):
    m = hashlib.sha512(pw.encode("UTF-8"))
    m = m.hexdigest()
    return m
