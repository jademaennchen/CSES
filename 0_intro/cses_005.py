#5: SOLVED
import sys

num = int(sys.stdin.read())
output = ''

for i in range(2, num+1, 2): output += ' '+str(i)
for i in range(1, num+1, 2): output += ' '+str(i)

print(output[1:]) if num not in (2, 3) else print('NO SOLUTION')
