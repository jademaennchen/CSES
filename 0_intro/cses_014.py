#14: SOLVED
import sys

def hanoi(n, start, aux, end):
    if n == 1:
        print(f'{start} {end}')
        return
    hanoi(n-1, start, end, aux)
    print(f'{start} {end}')
    hanoi(n-1, aux, start, end)

size = int(sys.stdin.read())
print(2**size-1), hanoi(size, 1, 2, 3)
