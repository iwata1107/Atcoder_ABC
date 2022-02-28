"""""
input_line = input()
X, Y = input_line.split()
"""""

# 入力の受け取り
X,Y = map(int,input().split())

tmp = int(Y) - int(X)

count = 0
while tmp > 0:
    count += 1
    tmp -= 10

print(count)
    
    