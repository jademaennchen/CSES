#9: SOLVED
import sys

num = int(sys.stdin.read())

num = 2**num % (10**9+7)

print(num)
