#Problem 11961: https://onlinejudge.org/external/119/11961.pdf

from itertools import combinations, product

def generate_mutations():
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        seq = input()
        mutations = set()
        for k in range(K+1):
            # Generamos todas las combinaciones de posiciones a mutar
            for positions in combinations(range(N), k):
                # Generamos todas las posibles sustituciones para esas posiciones
                for replacement in product('ACGT', repeat=k):
                    mutation = list(seq)
                    # Reemplazamos los nucleótidos en las posiciones a mutar
                    for p, r in zip(positions, replacement):
                        mutation[p] = r
                    mutations.add(''.join(mutation))
        print(len(mutations))
        for m in sorted(mutations):
            print(m)

generate_mutations()