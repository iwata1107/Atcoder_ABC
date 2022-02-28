# ①入力の受け取り
S=input()
a,b=map(int,input().split())

# ②一文字ずつリストへ格納
S_list=list(S)

# 0インデックスのためマイナス1してずらす
a-=1
b-=1

# ③a文字目とb文字目を入れ替え
S_list[a],S_list[b]=S_list[b],S_list[a]

# ④リストを結合
ans="".join(S_list)

# ⑤答えを出力
print(ans)