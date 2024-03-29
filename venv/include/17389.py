# https://www.acmicpc.net/problem/17389

# 보너스 점수

# i번 문제의 경우 i점을 획득하며,
# 문제를 맞히면, 보너스 점수의 값이 1점 증가한다.
# 문제를 틀리면, 보너스 점수를 얻지 못하고,
# 보너스 점수의 값이 0점으로 초기화 된다.

# 입력
# 8
# XOOOXOOX
# 출력
# 26

# X000X00X

# 1번 문제를 틀렸으므로 점수를 얻지 못하고 보너스 점수가 0점으로 초기화된다.
# (총 점수0점)
# 2번 문제를 맞혔으므로 기본점수 2점과 보너스 점수 0점을 획득하며,
# 보너스 점수가 1점으로 증가한다.(총 점수 2점)
# 3번 문제를 맞혔으므로 기본 점수 3점과 보너스 점수 1점을 획득하며,
# 보너스 점수가 2점으로 증가한다. (총 점수 6점)
# 4번 문제를 맞혔으므로 기본점수 4점과 보너스 점수 2점을 획득하며,
# 보너스 점수가 3점으로 증가한다.(총 점수 12점)
# 5번 문제를 틀렸으므로 점수를 얻지 못하고 보너스 점수가 0점으로 초기화 된다.
# (총 점수 12점)
# 6번 문제를 맞혔으므로 기본 점수 6점과 보너스 점수 0점을 획득하며,
# 보너스 점수가 1점으로 증가한다.(총 점수 18점)
# 7번 문제를 맞혔으므로 기본 점수 7점과 보너스 점수 1점을 획득하며,
# 보너스 점수가 2점으로 증가한다.(총 점수 26점)
# 8번 문제를 틀렸으므로 점수를 얻지 못하고 보너스 점수가 0점으로 초기화된다.
# (총 점수 26점)


N, S = input(),input()

score,bonus = 0,0

# i번 문제를 맞추면,i점을 획득하며, 보너스 점수의 값이 1점 증가한다.

for idx, OX in enumerate(S):
    # score,bonus 동시에 변함.
    if OX == 'O':
        score,bonus = score + idx+1+bonus,bonus+1
    else:
        bonus = 0

print(score)











# N, S = input(),input()
#
# for idx, OX in enumerate(S):
#     print(idx,OX)
#
# 8
# XOOOXOOX
# 0 X
# 1 O
# 2 O
# 3 O
# 4 X
# 5 O
# 6 O
# 7 X












