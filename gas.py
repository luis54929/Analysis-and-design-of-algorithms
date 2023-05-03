#Problem 12321: https://onlinejudge.org/external/123/12321.pdf

def max_gas_stations(L, G, stations):
    stations = sorted([(x-r, x+r) for x, r in stations])
    cover = cnt = i = 0
    while cover < L:
        if i >= G or stations[i][0] > cover:
            return -1
        max_cover = stations[i][1]
        while i < G-1 and stations[i+1][0] <= cover:
            i += 1
            max_cover = max(max_cover, stations[i][1])
        cover = max_cover
        cnt += 1
        i += 1
    return G - cnt

def main():
    L, G = map(int, input().split())
    while L != 0 or G != 0:
        stations = []
        for _ in range(G):
            x, r = map(int, input().split())
            stations.append((x, r))
        result = max_gas_stations(L, G, stations)
        print(result)
        L, G = map(int, input().split())

main()