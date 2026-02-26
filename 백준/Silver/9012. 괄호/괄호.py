import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    stack = []
    ps = input().strip()

    for check in ps:
        if check == "(":
            stack.append(check)
        else: # ")"
            if stack:
                stack.pop()
            else:
                stack.append(")")
                break
    print("YES" if not stack else "NO")