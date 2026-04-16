num = int(input("숫자를 입력하세요: "))

a = 1

for i in range(1, num + 1):
  a *= i
	
print("팩토리얼: ", a)
