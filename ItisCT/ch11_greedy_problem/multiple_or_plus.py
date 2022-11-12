s = list(map(int, input()))
result = s[0]
for i in range(1, len(s)):
    num = s[i]
    if result == 0 or result ==1:
        result += num
    else:
        result *= num
print(result)