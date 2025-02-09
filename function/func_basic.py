'''
* 함수 (function)

- 함수는 지속적으로 사용되는 코드 블록에 이름을 붙여놓은 형태입니다.

- 함수는 한 번 정의해 두면 지정된 함수 이름을 통해
언제든지 해당 코드 블록을 실행할 수 있습니다.

- 함수를 정의할 때 사용하는 키워드는 def 입니다.

- 정의해 놓은 함수를 사용하는 것을 호출(call) 이라고 부릅니다.

- 파이썬에서는 함수를 호출하려면 반드시 호출문보다 상단부에
함수를 먼저 정의해야 합니다.
'''

# 함수의 정의 (1~x까지의 누적합을 구하는 로직)

def calc_sum(end):
    sum = 0
    for n in range(1, end + 1):
        sum += n
    return sum

# 함수의 호출
print(f'함수의 호출 결과: {calc_sum(100)}')


'''
* 인수, 매개변수 (arguments)

- 인수는 함수를 호출할 때 함수 실행에 필요한 값. 함수의 호출 시 전달해 주는 값
그 값을 받아내는 변수가 매개 변수입니다.

- 인수의 개수는 제한이 없어 많은 값을 함수에 전달할 수도 있고
하나도 전달하지 않을 수 있습니다.

- 파이썬의 경우에는 데이터 타입을 작성하지 않기 때문에
이 함수를 처음 사용하는 사람도 인수 이름만 보고 무슨 값을
전달해야 할 지 의미를 알기 쉽게 지정하는 것이 좋습니다.
'''

'''
* 반환값 (return value)

- 반환값이란 함수를 호출한 곳으로 함수의 최종 실행 결과를
전달하는 값입니다.

- 인수는 여러 개 존재할 수 있지만, 반환값은 언제나
하나만 존재해야 합니다.

- 모든 함수가 반환값이 있는 것은 아닙니다.
함수 실행 후 딱히 반환할 값이 없다면 return을 생략할 수 있습니다.
'''

def add(n1, n2):
    return n1 + n2

result = add(10, 15)

# 리턴이 있는 함수는 다른 함수의 매개값으로도 사용이 가능합니다.
print(add(add(5, 7), add(9,8))) # add(12, 17)
# n = int(input('정수: '))

def operate_all(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2
    # return n1 - n2
    # return n1 * n2
    # return n1 / n2

print(type(operate_all(10, 5)))

def multi(n1, n2):
    result = n1 * n2
    print(f'{n1} x {n2} = {result}')

abc = multi(9, 6)
print(abc)



