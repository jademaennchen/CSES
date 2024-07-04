#7: SOLVED
import sys

max_len = int(sys.stdin.read())
invalid, len = 0, 1

while len <= max_len:
    cases = (len**2-1) * (len**2) // 2
    invalid += max(8 * (len-2), 0)
    len += 1
    print(cases - invalid)
