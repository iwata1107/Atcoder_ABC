"""""
t = int(input())

a = t**2 + 2*t + 3
b = a**2 + 2*a + 3
c = a + t
d = c**2 + 2*c + 3
e = b + d
f = e**2 + 2*e + 3

print(f)
"""""""""
# 入力の受け取り
t=int(input())

# 関数の定義
# 引数；t　返り値：t^2+2t+3
def f(t):
    return t**2+2*t+3

# 答えの計算
ans=f(f(f(t)+t)+f(f(t)))

# 答えの出力
print(ans)
