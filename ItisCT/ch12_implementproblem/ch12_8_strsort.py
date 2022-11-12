s = list(input())

### 개인 코드
s.sort()
num = []
strarr = []
for i in s:
    if ord(i) < 64:
        num.append(int(i))
    else:
        strarr.append(i)
print(num)
for i in strarr:
    print(i, end = '')
if sum(num)!= 0:
    print(sum(num))


### 책보고 쓴 코드
value = 0
result = []
for i in s:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)
result.sort()

if value != 0:
    result.append(value)

for i in result:
    print(i, end = '')