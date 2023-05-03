#Problem 11658: https://onlinejudge.org/external/116/11658.pdf

from sys import stdin

def solve(n, m, prices, memo):
    A = []
    for price in prices:
        a, b = map(int, price.strip().split('.'))
        A.append(a * 100 + b)
    possible_prices = [0] * 10001
    up = 10000 - A[m-1]
    possible_prices[0] = 1
    for i in range(n):
        if i != m-1:
            for j in range(up, -1, -1):
                if possible_prices[j]:
                    possible_prices[j+A[i]] = 1
    up = 5001 - A[m-1]
    while not possible_prices[up]:
        up += 1
    ans = round(A[m-1] * 100 / (up + A[m-1]), 2)
    memo[(n, m, tuple(A))] = ans
    return ans

def main():
    n, m = map(int, stdin.readline().strip().split())
    while n != 0:
        prices = [stdin.readline().strip() for _ in range(n)]
        memo = {}
        ans = solve(n, m, prices, memo)
        print(f'{ans:.2f}')
        n, m = map(int, stdin.readline().strip().split())

main()
