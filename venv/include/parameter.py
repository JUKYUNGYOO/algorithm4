#
# money_sum : 돈의 합을 출력
# N : 사람수, money_arr : 사람의 돈

def money_sum(N,money_arr):
    ret = 0

    for i in range(N):
        ret += money_arr[i]

    return ret

# 배열, 구조화
# container의 역할
# Tuple : 위치(index)에 따른 의미
# Set : 포함 여부의 의미
# List : index와 원소의 관계
# Dict : Key와 value의 관계
# 함수와 마찬가지로 적절한 명명 필요

set() #중복이름제거
A = [0 for i in range(100)] #A[i] = i번째 소년의 키

# dp[i][j] i번째 사람이 j개를 먹는 가짓수

A = [[0 for i in range(2)] for j in range(100)]
print(A)


# 1번째 값은 순서, 2번째 값은 값
# A[i][0], A[i][1]






