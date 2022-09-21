# codingtest

### 1. LRUD

###### 1. 문제 재정의
공간의 크기, 이동계획서가 주어진 후 1,1에서 이동한 위치를 출력

###### 2. 조건
여행자는 N, N의 공간을 벗어나지 못한다.

###### 3. 알고리즘 설계
* 공간의크기, 이동계획서, 시작 위치를 정의
  + N, plans, (x,y) 정의
* 이동 관련 변수 정의
  + dx, dy, move_types(LRUD 관련)
* 이동 구현
  + 2중포문, 첫번째 포문은 plans를 돌며,
  + 두번째 포문은 move_types를 확인하고,
  + 이에 맞게 x, y 값을 바꿔줌
  + 조건에 맞지 않을 경우 x, y 값을 저장시키지 않고, 조건을 만족할 경우 저장
* 이동 후 값 출력
