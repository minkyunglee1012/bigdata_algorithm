# testcase 1
a, b, n = 2, 1, 20  # 19

# testcase 2
# a, b, n = 3, 1, 20  # 9

# 조건 1: n >= a


# new = n // a   * b개 만큼 받을 수 있음
# n % a 개 만큼 남고 new개를 추가하여 다시 조건 1 만족하면 //a  *b
# 반복

def solution(a, b, n):
    c_sum = 0
    while n >= a:
        new = (n//a) * b
        c_sum += new
        n = new + n%a
    return c_sum


print(solution(a, b, n))
