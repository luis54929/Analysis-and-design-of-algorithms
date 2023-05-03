
from sys import stdin

memo = {}

def validate(size, A, N, B, memo):
    if size in memo:
        return memo[size]
    b, n = 0, 0
    while b <= B and n != N:
        bc, rem = divmod(A[n], size)
        if rem != 0: bc += 1
        b, n = b + bc, n + 1
    memo[size] = b <= B
    return memo[size]

def solve(A, N, B):
    low, hi = 0, max(A)
    while low + 1 != hi:
        mid = (low + hi) // 2
        if validate(mid, A, N, B, memo):
            hi = mid
        else:
            low = mid
    return hi

def main():
    N, B = map(int, stdin.readline().split())
    while N != -1:
        A = [int(stdin.readline()) for _ in range(N)]
        stdin.readline()
        print(solve(A, N, B))
        N, B = map(int, stdin.readline().split())
main()