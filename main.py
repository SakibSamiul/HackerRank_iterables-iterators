from itertools import combinations

def iterables_iterators(N, k):
    
    p = list(combinations(sorted(N), k))

    count_a = 0
    for i in p:
        if 'a' in i:
            count_a += 1

    print(count_a / len(p))

if __name__ == '__main__':
    N = int(input())
    N = input().lower().split()
    k = int(input())

    result = iterables_iterators(N, k)