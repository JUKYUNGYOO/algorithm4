# https://www.acmicpc.net/problem/1920

# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다.
# 다음 줄에는 N개의 정수
# A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수들의 범위는 int 로 한다.

# 입력
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
# 출력
# M개의 줄에 답을 출력한다.
# 존재하면 1을, 존재하지 않으면 0을 출력한다.
# 1
# 1
# 0
# 0
# 1

N,A = int(input()), {i: 1 for i in map(int,input().split())}
# 4 1 5 2 3
# input() 을 쪼개서 int로 바꾼다음에 있는 수들은 1로 매칭
M = input()
for i in list(map(int,input().split())):
    # 1 3 7 9 5
    print(A.get(i,0))
#     Dictionary의 get() - 아직 키가 등록되지 않는 값들은 0으로




