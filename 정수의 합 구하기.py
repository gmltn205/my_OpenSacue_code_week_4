# 1 부터 n까지의 정수의 합 구하기 1 (for 문)

print('1부터 n까지 정수의 합을 구합니다.')
n=int(input('n값을 입력하세요. : '))

sum=0
i=1

for i in range(1,n+1):
    sum+=i
    
print(f'합은 {sum} 입니다')
