#3: SOLVED
import sys

cur, cnt, mx = '', 0, 0

for c in sys.stdin.read():
    if c != cur:
        if cnt > mx: mx = cnt
        cur = c
        cnt = 0
    cnt += 1

print(max(cnt, mx))
