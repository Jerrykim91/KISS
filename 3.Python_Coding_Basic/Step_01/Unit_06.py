# Unit_06.py
# 변수와 입력 사용하기

txt = """
- 변수와 입력 사용하기 
x = 10 
x 라는 박스에 10을 담는다 
변수이름 = 값 

- 변수 생성 규칙 
1. 영문 문자와 숫자르 사용할수 있다. 
2. 대소문자를 구분한다. 
3. 문자부터 시작해야하며 숫자부터 시작하면 안된다. 
4. \_(밑줄문자: 언더 스코어) 시작 가능하다 
5. 특수문자(+,-,\*,\/,$,@,&,%등)는 사용할수 없다
6. 파이썬 키워드(if , for , while, and , or) 등은 사용할수 없다. 

- 프로그래밍언어에서 '='은 변수에 값을 할당한다라는 의미 
    => 수학등호 같은 연산자는 '=='     

"""
print(txt)
print('-'*40)

# 변수 여러개를 한번에 
# 변수 이름 1 , 변수 이름 2 , 변수 이름 3 = 값1 ,값 2, 값3 
x, y, z = 10, 20, 30 
print( x, y, z )
x = y = z = 10 
print(x)

x, y = 10, 20
x, y = y, x
print( x, y )

print('-'*40)

# 빈 변수 만들기 
x = None 
print(x)
print('-'*40)
# 값이 없어서 아무것도 출력이 안됨 
print(x)
print('-'*40)

# 변수로 계산하기 
a = 10 
b = 10 
c =a+b 
print(c)

# 산술 연산후 할당 연산자 사용하기 
a = 10 
print(a+20 , a)

a = 10 
a += 20 
print(a)

print('-'*40)

txt = """
- input() 함수 사용 
변수 = input('문자열')    
입력 값을 정수로 변환하기     
변수 = int(input('첫번째 숫자를 입력하세요: '))    
변수 = int(input())    

- 입력 받은 값을 두개의 변수에 저장하기    
변수 1, 변수 2 = input().split()     
변수 1, 변수 2 = input().split('문자열')    
변수 1,변수 2 = input('문자열').split()      
변수 1,변수 2 = input('문자열').split('기준문자열')    

input에 split을 사용하면 입력받은 값을 공백을 기준으로      
분리하여 변수에 차례로 저장  
  
- map()을 사용하여 정수로 변환하기 
split의 결과를 매번 int로 변경하면 번거롭다-> 이때 map()을 사용         
map에 input().split()을 넣으면 split의 결과르 모두 int()로 변환      
나중에 map에서 다시 설명        

"""
print(txt)
print('-'*40)
print('input 파트 => 주석처리')
# map() 공백을 기준으로 분리 
#a,b = map(int, input('숫자 두개를 입력하세요(,제외): ').split())
#print(a+b)

# 입력 받은 값을 콤마 기준으로 분리하기 
#a,b = map(int, input('숫자 두 개를 입력하세요: ').split(','))
#print(a + b)
print('-'*40)