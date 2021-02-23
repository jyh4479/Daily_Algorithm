#대표적인 greedy문제 --> 딱 맞아 떨어지는경우만 가능함 아닌경우는 DP로 풀이해야함
def solution(coin):
    coins=[500,100,50,10,5,1]
    ans = 0
    for i in coins:
        ans+=coin//i
        coin%=i
    return ans

coin = 1000-int(input())
print(solution(coin))