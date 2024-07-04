#2: SOLVED
import sys

count, nums = [line.strip() for line in sys.stdin.readlines()]
sum = int(int(count)/2 * (int(count)+1))

for num in nums.split():
    sum -= int(num)

print(sum)
