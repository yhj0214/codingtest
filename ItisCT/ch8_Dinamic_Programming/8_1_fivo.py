def fivo(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fivo(x-1) + fivo(x-2)

print(fivo(4))