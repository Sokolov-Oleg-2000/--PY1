def delete(list_, index=-1):
    if index != -1:
        spisok = list_[:index]+list_[index+1:]
    else:
        spisok = list_[:index]
    return spisok

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
