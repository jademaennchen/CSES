#4: SOLVED
import sys

nums = list(map(int, sys.stdin.readlines()[1].strip().split()))
cur, cnt = nums[0], 0

for num in nums[1:]:
    if num >= cur: cur = num
    else: cnt += cur - num

print(cnt)
