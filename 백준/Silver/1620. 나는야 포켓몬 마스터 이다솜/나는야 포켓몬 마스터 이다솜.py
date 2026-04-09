import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pokemon = {}

for i in range(1, N+1):
    name = input().strip()
    pokemon[i] = name
    pokemon[name] = i

for _ in range(M):
    cmd = input().strip()

    if cmd.isdigit():
        print(pokemon[int(cmd)])
    else:
        print(pokemon[cmd])