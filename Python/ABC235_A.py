X = input()

a = X[0]
b = X[1]
c = X[2]

abc = a+b+c
bca = b+c+a
cab = c+a+b

ans = int(abc) +int(bca) + int(cab)
print(ans)