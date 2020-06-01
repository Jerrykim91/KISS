
# Problem : 3차시 

진행중인 프로젝트에 관한 여러가지 이슈 그리고 해결방안을 포스팅하고자 한다. 

<br>

## 일자 
- 2020년 06월 01일 월요일 

<br>

## 진행 상황

현재 전체적인 진행상황은 아래와 같다. 

- 이미지 분석 : 45 % 
- 텍스트 분석 : 85 % (감소)
- 시스템 구현 :  10% 

<br>
<br>

##  이슈 

### 이슈 1 : 모델 설계 


시간상 전체적인 모델 룰을 정하고 진행하기로 했다. 

1. 모델의 손실 값이 아직까지는 줄어 드는 것을 봐서는 에포크 값을 늘려도 될것
2. 모델이 단순해서 튜닝할 여지가 많아 튜닝해서 모델을 안정화 시키는 것 
3. 모델을 튜닝할때는 에포크를 줄이고 진행할것 

<br>

```bash

# 상위 카테고리 
#    ㄴ 각각 카테고리를 모아서(file), 합쳐서 나열한다. 
#       => 모델을 만든다.
#
# 이렇게 만든 상위 모델에서 나온 값을 받아 
# 하위 카테고리
#    ㄴ 각 카테고리를 학습시킨다(dir), 합쳐서 나열한다. 
#
# 그 값을 if문을 이용해 탐색하요 하위 카테고리 모델로 전달하여 재학습 시킨다.  
# 현재까지 아이디어는 여기까지인데 

# 여기서 문제점이 있다. 

# 1. 상위모델은 하위 모델 보다 정확도가 높아야 한다. 
# 2. 하위모델은 적어도 정확도가 90은 나와야 한다. 
# 3. 입력으로 들어오는 이미지는 최대한 음식에 집중되어야 한다. 

```


<br>
<br>


### 이슈 2 : 모델 튜닝 - 상위 모델 

우리가 가진 cnn 모델은 일단 튜닝할 여지가 많다.     
그래서 튜닝을 조금 시작할것이다.    

추가로 Transfer Learnning 공부해서 모델의 성능을 높이는 방향도 모색 할 것 

<br>

### 이슈 3 : 이미지 전처리 

멘토링을 했는데 우리의 데이터가 조금 이상했던것같다.
그래서 서브멘토가 확인을 해주겠다고 했다. 
그래서 오늘 로이미지 데이터와 코드를 넘겼고 전처리 과정이 어떤 문제가 있는지 피드백을 받기로했다. 

<br>