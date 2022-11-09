def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b]= a
    else:
        parent[a] = b
v, e = map(int, input().split()) # 노드의 개수, 간선 개수 입력
parent = [0] * (v+1) #부모 테이블 초기화
for i in range(1, v+1): #부모 테이블 자기 자신으로 초기화
    parent[i] = i

cycle = False #사이클 여부

for i in range(e):
    a, b = map(int, input().split()) 
    if find_parent(parent, a) == find_parent(parent, b): # 사이클이 발생한 경우 멈춤
        cycle = True
        break
    else:
        union_parent(parent, a, b) # 사이클이 발생하지 않은 경우 합집합 연산 수행

if cycle:
    print("사이클이 발생하였습니다.")
else:
    print("사이클이 발생하지 않았습니다.")