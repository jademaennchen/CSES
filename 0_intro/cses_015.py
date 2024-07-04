#15: SOLVED
import sys

string = sys.stdin.read().strip()
counts, strings = {chr(i): string.count(chr(i)) for i in range(97, 123) if chr(i) in string}, ['']

for _ in range(len(string)): strings = [ch+string for ch in counts.keys() for string in strings if string.count(ch)+1 <= counts[ch]]

print(len(strings)), [print(string) for string in strings]
