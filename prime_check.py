num = int(input("숫자를 입력하세요: "))

cnt = 0
for i in range(2, num):
  if num % i == 0:
  	cnt +=1
	
if cnt == 0:
  if num == 0 or num == 1:
    print("소수가 아닙니다")
  else:
    print("소수입니다")
else:
	print("소수가 아닙니다")
