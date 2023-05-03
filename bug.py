#Problem 1216: https://onlinejudge.org/external/12/1216.pdf

import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find(parents, u):
    if parents[u] != u:
        parents[u] = find(parents, parents[u])
    return parents[u]

def union(parents, ranks, u, v):
    pu, pv = find(parents, u), find(parents, v)
    if pu == pv:
        return False
    if ranks[pu] < ranks[pv]:
        parents[pu] = pv
    elif ranks[pu] > ranks[pv]:
        parents[pv] = pu
    else:
        parents[pv] = pu
        ranks[pu] += 1
    return True

def kruskal(graph, num_clusters):
    n = len(graph)
    edges = []
    for u in range(n):
        for v, w in graph[u]:
            if u < v:
                edges.append((w, u, v))
    edges.sort()
    parents = list(range(n))
    ranks = [0] * n
    num_components = n
    max_weight = 0
    for w, u, v in edges:
        if union(parents, ranks, u, v):
            num_components -= 1
            max_weight = w
            if num_components == num_clusters:
                break
    return max_weight

def solve(num_receivers, sensors):
    n = len(sensors)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(sensors[i], sensors[j])
            graph[i].append((j, d))
            graph[j].append((i, d))
    ecd = kruskal(graph, num_receivers)
    return math.ceil(ecd)
  
def main():
    w = int(input())
    for _ in range(w):
        num_receivers = int(input())
        sensors = []
        line = input().strip()
        while line != '-1':
            x, y = map(int, line.split())
            sensors.append((x, y))
            line = input().strip()
        ecd = solve(num_receivers, sensors)
        print(ecd)

main()