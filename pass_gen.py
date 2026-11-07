import string
import secrets

pool = string.ascii_letters + string.digits


password = "".join(secrets.choice(pool) for _ in range(16))
print(password)