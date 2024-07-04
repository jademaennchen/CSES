#6: SOLVED
import sys

tests = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()[1:]]

for y, x in tests:
    mx = max(y, x)
    if mx % 2 == 0: print(mx**2 - (x-1) - (mx - y))
    else: print(mx**2 - (y-1) - (mx - x))
