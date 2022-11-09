# 다이나믹 프로그래밍(DP : Dinamic Programming)
### 중복되는 연산 줄이기
* topdown : 추상화 수준에서 시작하여, 상세화 수준을 높이는 설계 방법
* bottomup : 구체적인 수준에서 시작하여, 전체적인 구조를 맞춰나가는 설계 방법
* Memoization 
* tabulation

#### 피보나치 수열
###### (1) 재귀적 함수만 이용한 피보나치 수열(fivo.py)
* 피보나치 수열에서 재귀함수를 이용하게 되면 시간복잡도가 O(N^2)이다.
* 하나를 호출하였을 때 f(1) 또는 f(2)를 만날때까지 계속하여 함수를 호출함
* 이 때문에 메모리의 효율성이 떨어지고, 연산량이 매우 많아지게 된다.

###### (2) 재귀적 함수와 memoization을 이용한 피보나치 수열(fibo2.py)
* 결과를 저장할 리스트하나를 생성
* 원래 함수에선 f(1), f(2)를 만날때까지 함수를 무수히 많이 반복하게 됨
* 2번의 단점을 보완하기 위하여 계산 결과를 1에서 만든 리스트에 저장하는 방식
* 필요한 결과를 매번 재계산 하지 않고 저장된 리스트에서 호출하게 됨

###### (3) 반복문을 이용한 피보나치 수열(fibo3.py)
* 원하는 수까지 결과를 저장할 배열 선언
* d[1],d[2]값에 미리 정해진 수를 넣어두고, 이후 필요한 값까지 계산하여 저장

###### 정리
* 재귀함수를 이용한 방식은 큰 문제 해결을 위해 작은 문제를 호출함(topdown방식)
* 반목문을 이용한 방식은 작은 문제부터 결과값까지 순차적으로 계산함(bottomup방식)


#### 다이나믹 프로그래밍의 사용조건
* 큰 문제를 작은 문제로 나눌 수 있어야 한다.
* 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.