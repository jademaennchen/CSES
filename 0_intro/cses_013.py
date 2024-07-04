#13: SOLVED
import sys

num = int(sys.stdin.read())
codes = ['']

for _ in range(num): codes = ['0'+c for c in codes] + ['1'+c for c in codes][::-1]

for code in codes: print(code)
