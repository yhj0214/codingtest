
s = list(map(int, list(input())))
print(s)
num1 = 0
num2 = 0
for i in range(0,len(s)//2):
    num1 += s[i]
for j in range(len(s)//2,len(s)):
    num2 += s[j]
if num1 == num2:
    print("LUCKY")
else:
    print("READY")