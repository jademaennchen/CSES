#10: SOLVED
import sys

num = int(sys.stdin.read())
count, div = 0, 5

while div <= num:
    count += num//div
    div *= 5

print(count)
