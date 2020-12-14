import time
from faker import Faker
fake = Faker()

def time_create(func):
    def timed(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
    return timed

@time_create
def create():
    card_list = []
    for card in range(1000):
        card= (f"{fake.first_name()}, {fake.last_name()}, {fake.company()}, {fake.job()}, {fake.email()},{fake.phone_number()}")
        card_list.append(card)
    print(card_list)

create()