#17: SOLVED
import sys

def queens(n, coords, blocked, count):
    for pot in range((coords[-1][1]+1)*8, 57+n):
        if pot not in blocked and (n==0 or all(pos[2] != pot % 8 and (pos[1]-pot//8) / (pos[2]-pot%8) not in (1.0, -1.0, 0) for pos in coords[1:])):
            if n==7: count += 1
            else: count = queens(n+1, coords + [(pot, pot // 8, pot % 8)], blocked, count)
    return count

board = [line for line in sys.stdin.readlines()]
blocked = [y*8+x for y in range(8) for x in range(8) if board[y][x] == '*']
print(queens(0, [(-1, -1, -1)], blocked, 0))
