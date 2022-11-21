list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = 0
for i in range(0, len(list_numbers)):
    if a <= list_numbers[i]:
        a = list_numbers[i]
        b = i
list_numbers[b], list_numbers[-1] = list_numbers[-1], list_numbers[b]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
