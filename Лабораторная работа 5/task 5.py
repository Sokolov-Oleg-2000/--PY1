import random

def get_random_password(n=8) -> str:
    base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    a = random.sample(base, n)
    return "".join(a)

print(get_random_password())

