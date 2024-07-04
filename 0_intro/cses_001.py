#1: SOLVED
import sys

num = int(sys.stdin.read())
output = str(num)

while num != 1:
    if num % 2 == 0: num //= 2
    else: num = num*3+1
    output += ' '+str(num)

print(output)
