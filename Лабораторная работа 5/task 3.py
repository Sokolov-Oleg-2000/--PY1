from random import randint

def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) < 15:
        value = randint(-10, 10)
        if value not in list_:
            list_.append(value)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

