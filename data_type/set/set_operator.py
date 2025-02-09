
'''
* 집합의 연산

1. 합집합(|): 두 집합의 전체 요소들의 모음 (중복 제거) -> union(), a.update(b)
2. 교집합(&): 두 집합의 중복을 배제한 공통 요소들의 모음. -> a.intersection(b)
3. 차집합(-): 왼쪽 집합에서 오른쪽 집합 요소를 제거 -> difference()
4. 배타적 차집합(^): 합집합 - 교집합 -> symmetric_difference_update()
5. 부분집합 (<=): 왼쪽 집합이 오른쪽 집합의 부분집합인지를 검사. -> issubset()
'''

A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}

print('교집합:', A & B)
print('합집합:', A | B)
print('차집합(A-B):', A - B)
print('차집합(B-A):', B - A)
print('배타적 차집합:', A ^ B)

C = {4, 8, 12}
print(C <= A)
print(C <= B)






