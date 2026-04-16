num = int(input("숫자를 입력하세요: "))
even_total = 0
odd_total = 0

for i in range(1, num + 1):
  if i % 2 == 0:
  	even_total += i
  else:
  	odd_total += i
	
print("짝수의 합 : ", even_total)
print("홀수의 합 : ", odd_total)
