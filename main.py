def main():
    print("안전 공학 계산기에 오신 것을 환영합니다!")

    # 사용자로부터 두 개의 숫자 입력 받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))

    # 연산 수행
    sum_result = num1 + num2
    diff_result = num1 - num2
    product_result = num1 * num2

    # 두 번째 숫자가 0이 아닌 경우에만 나눗셈 수행
    if num2 != 0:
        division_result = num1 / num2
    else:
        division_result = "두 번째 숫자가 0입니다. 나눗셈은 불가능합니다."

    # 제곱 계산
    square1_result = num1 ** 2
    square2_result = num2 ** 2

    # 결과 출력
    print("\n결과:")
    print("두 숫자의 합:", sum_result)
    print("두 숫자의 차:", diff_result)
    print("두 숫자의 곱:", product_result)
    print("첫 번째 숫자의 제곱:", square1_result)
    print("두 번째 숫자의 제곱:", square2_result)
    print("첫 번째 숫자를 두 번째 숫자로 나눈 결과:", division_result)

if __name__ == "__main__":
    main()
