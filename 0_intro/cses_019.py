#19: SOLVED (TLE)
import sys

def valid(y, x):
    global grid
    if 0 <= y <= 6 and 0 <= x <= 6 and grid[y][x] == False: return True
    return False

def search(n, y, x):
    global string, grid, vecs, count
    if n == 48 and (y, x) == (6, 0): count += 1
    if n == 48 or (y, x) == (6, 0): return
    grid[y][x] = True
    for v in vecs.values() if string[n] == '?' else [vecs[string[n]]]:
        if valid(y+v[0], x+v[1]) and not (not valid(y+2*v[0], x+2*v[1]) and valid(y+v[0]+v[1], x+v[0]+v[1]) and valid(y+v[0]-v[1], x-v[0]+v[1])): search(n+1, y+v[0], x+v[1])
    grid[y][x] = False

string = sys.stdin.read().strip()
grid, vecs, count = [[False for _ in range(7)] for _ in range(7)], {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}, 0
search(0, 0, 0)
print(count)
