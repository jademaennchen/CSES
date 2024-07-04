#11: SOLVED
import sys

tests = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()[1:]]

for left, right in tests:
    print('YES') if (left + right) % 3 == 0 and not (left > right*2 or right > left*2)  else print('NO')
