n = input()
column = int(ord(n[0])-ord('a')+1)
row = int(n[1])
count = 0

move_list = [[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1]]

for i in move_list:
    nrow = row +i[0]
    ncolumn = column + i[1]
    if nrow < 9 and ncolumn < 9 and nrow > 0 and ncolumn > 0:
        count += 1
print(count)