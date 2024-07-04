#16: SOLVED
import sys

nums = list(map(int, sys.stdin.readlines()[1].strip().split()))
nums, pots, goal = sorted(nums, reverse=True), set([0]), sum(nums) // 2

for num in nums:
    pots.update([num+pot for pot in pots if num+pot <= goal])

print(sum(nums)-2*max(pots))
