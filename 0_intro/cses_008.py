#8: SOLVED
import sys

nums = [i for i in range(int(sys.stdin.read()), 0, -1)]
sum = len(nums) * (len(nums)+1) // 2

if sum % 2 == 0:
    print('YES')
    print((len(nums)+1) // 2), print(' '.join(list(map(str, nums[1::4]+nums[2::4]))))
    print(len(nums) // 2), print(' '.join(list(map(str, nums[::4]+nums[3::4]))))
else: print('NO')
