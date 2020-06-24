import bisect,collections,copy,heapq,itertools,math,numpy,string
from fractions import gcd
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split())) # tupleも検討する。
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N, L = LI()
    A = [S() for _ in range(N)]

    A.sort()
    print("".join(A))

if __name__ == '__main__':
    main()