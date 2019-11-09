
# 20까지의 짝수를 출력하기 위해 다음과 같은 LC를 사용할 수 있다
evens = [x * 2 for x in range(11)]
print(evens)

# 100 이하의 제곱수가 아닌 수를 찾는 LC
from math import sqrt
non_squars = [x for x in range(101) if sqrt(x)**2 != x]
# [2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 18, 19, 20, 23, 24, 26, 28, 29, 31, 32, 37, 38, 40, 43, 45, 48, 50, 51, 52, 58, 59, 60, 61, 63, 65, 66, 72, 73, 75, 76, 77, 78, 80, 82, 87, 89, 92, 94, 95, 96, 97]

# 두 리스트의 원소들의 모든 조합을 찾는 LC
epithets = ['sweet', 'annoying', 'cool', 'grey-eyed']
names = ['john', 'alice', 'james']
epithet_names = [(e, n) for e in epithets for n in names]
# [('sweet', 'john'), ('sweet', 'alice'), ('sweet', 'james'), ('annoying', 'john'), ('annoying', 'alice'), ('annoying', 'james'), ('cool', 'john'), ('cool', 'alice'), ('cool', 'james'), ('grey-eyed', 'john'), ('grey-eyed', 'alice'), ('grey-eyed', 'james')]

# a^2 + b^2 = c^2 (a < b < c)를 만족하는 피타고라스 방정식의 해를 찾는 LC
solutions = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]

# 단어에서 모음을 제거하는 LC
word = 'mathematics'
without_vowels = ''.join([c for c in word if c not in ['a', 'e', 'i', 'o', 'u']])
# 'mthmtcs'

# 행렬을 일차원화 시키는 LC
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
flatten = [e for r in matrix for e in r]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 다음의 LC는 중복된 값들을 포함한다
no_primes = [j for i in range(2, 9) for j in range(i * 2, 50, i)]
# [4, 6, 8, 10, 12, 14, 16,
# 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 14, 21, 28, 35, 42, 49, 16, 24, 32, 40, 48]
print(no_primes)


no_primes2 = [j for i in range(2,9) for j in range(i*2,10,i)]
print('no_primes2', no_primes2)


# SC를 사용하면 중복값이 없는 집합을 얻을 수 있다
no_primes = {j for i in range(2, 9) for j in range(i * 2, 10,i)}
print('no_primes', no_primes)
# 8,9,4,6


n = [j for i in range(1,5) for j in range(2,5)]
print(n)
# j범위의 range를 i번 반복
# [2,3,4,2,3,4,2,3,4,2,3,4]