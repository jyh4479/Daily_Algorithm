from itertools import permutations

N,M,K=map(int,input().split())
alphabetList=[]
for _ in range(N):
    alphabetList.append('a')
for _ in range(M):
    alphabetList.append('z')

print("".join(sorted(set(permutations(alphabetList,len(alphabetList))))[K-1]))