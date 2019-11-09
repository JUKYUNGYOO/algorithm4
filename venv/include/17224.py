# https://www.acmicpc.net/problem/17224

# N L K
# 4 8 4
# 1 8
# 4 5
# 6 20
# 9 12
# N 문제의 갯수, L 현정이의 역량,
# K 대회 중 풀 수 있는 문제 갯수

# 어떤 문제에 대해 쉬운 버전을 해결한다면 100점을 얻고,
# 어려운 버전을 해결한다면 여기에 40점을 더 받아 140점을 얻게 된다.
# 어려운 버전을 해결하면 쉬운 버전도 같이 풀리게 되므로,
# 한 문제를 해결한 것으로 계산한다.

N,L,K = map(int,input().split())
easy,hard = 0,0

for i in range(N):
    sub1, sub2 = map(int,input().split())
    # 쉬운 버전의 난이도, 어려운 버전의 난이도
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1
# hard 문제
ans = min(hard,K) * 140

# easy
if hard < K:
    ans += min(K-hard,easy) * 100
#     min(K-hard,easy)
#     min(덜푼문제, 쉬운문제)
print(ans)
