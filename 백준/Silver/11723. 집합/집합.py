import sys
input = sys.stdin.readline

M = int(input())
s = set()

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "add":
        if int(cmd[1]) not in s:
            s.add(int(cmd[1]))
        else:
            continue
    elif cmd[0] == "remove":
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            continue
    elif cmd[0] == "check":
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif cmd[0] == "all":
        s.clear()
        s.update({i for i in range(1, 21)})
    elif cmd[0] == "empty":
        s.clear()