n, m = map(int, input().split()) # m은 입력으로 주어지는 연산의개수

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0: # 팀 합치기 연산
        union_parent(parent, a, b)
    elif oper == 1: # 같은 팀 여부 확인 연산
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a == b :
            print("YES")
        else:
            print("NO")