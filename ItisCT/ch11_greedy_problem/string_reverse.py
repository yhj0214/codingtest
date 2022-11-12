s = input()
now = s[0]
answer = []
answer.append(now)
for i in s:
    if i != now:
        answer.append(i)
        now = i
print(len(answer)//2)