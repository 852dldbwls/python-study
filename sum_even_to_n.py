num = int(input("숫자를 입력하세요: "))
total = 0

for i in range(1, num + 1):
  if i % 2 == 0:
  	total += i
	
print("짝수의 합: ", total)
