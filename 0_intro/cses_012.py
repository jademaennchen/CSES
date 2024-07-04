#12: SOLVED
import sys

string = sys.stdin.read().strip()
palindrom, mid = '', ''

for i in range(65, 91):
    if string.count(chr(i)) % 2 == 0: palindrom += chr(i) * (string.count(chr(i)) // 2)
    elif len(string) % 2 == 1 and mid == '':
        mid = chr(i)
        palindrom += chr(i) * ((string.count(chr(i))-1) // 2)
    else:
        print('NO SOLUTION')
        break
else: print(palindrom + mid + palindrom[::-1])
