#18: SOLVED
import sys

tests = [int(line.strip()) for line in sys.stdin.readlines()[1:]]

for num in tests:
    count, digit = 0, 1
    while 9 * 10**(digit-1) * digit + count < num: count, digit = count + 9 * 10**(digit-1) * digit, digit + 1
    rest = num - count - 1
    print(str(10**(digit-1)+rest // digit)[rest % digit])
