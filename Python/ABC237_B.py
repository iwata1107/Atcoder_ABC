H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

for r in zip(*A):
    print(*r)