# Sort_정렬

#### 정렬 알고리즘 개요
* 데이터를 정렬할 경우 이진탐색이 가능해진다.
* 정렬은 오름차순을 가정한다.// 오름차순 정렬 +reverse(O(N)) -> 내림차순 정렬
* 대표적인 정렬로는 선택, 삽입, 퀵, 계수(정렬)이 있다.


#### 선택 정렬
###### 1. 선택정렬 개요
* 가장 작은 값을 찾아 리스트의 가장 앞자리와 바꾸어가며 정렬하는 방식
* 파이썬에서는 swap 함수를 제공함. 배열을 포함한 다른 자료형도 가능하다.
ex) array[0], array[1] = array[1], array[0]

###### 2. 선택정렬 시간복잡도 -> O(N^2)
    1. 선택정렬에서 가장 작은 수의 위치를 찾는 것은 O(N)이다.
    2. 이후 인덱스 1번을 채우고 2, 3...을 채우는 것은 n-1,n-2..의 연산을 필요로 한다.
    3. 따라서 연산 횟수는 N + (N-1) + (N-2)... +2 +1로 볼 수 있다.
    4. 등차수열에서 위는 N(N+1)/2로, 간단히 빅오표기법으로 표현 시 O(N^2)로 나타낸다.

#### 삽입 정렬
###### 1. 삽입정렬 개요
* 첫번째 데이터를 기준으로, 두번째 데이터는 첫번째 데이터의 앞이나 뒤에 삽입된다.
* 이후 세번째 데이터부터 마지막 데이터까지 자기 앞의 정렬된 데이터의 알맞은 위치에 삽입되며, 정렬된다.

###### 2. 삽입정렬 시간복잡도 -> O(N^2)
* 데이터를 하나씩 정렬할 때마다 최소 0번에서 최대 n번 -> N
* 데이터의 개수가 N개이므로 윗줄의 과정을 N-1번 수행하여야 함
* 따라서 시간복잡도는 O(N^)
* ※ 정렬이 거의 되어있다면 이동이 거의 없어 다른 정렬 알고리즘보다 훨씬 빠를 수 있다.

#### 퀵 정렬
###### 1. 퀵 정렬 개요
* 퀵 정렬과 병합정렬은 정렬 라이브러리에 근간이 되었다.
* 호어 분할 방식 : 리스트의 첫번째 데이터를 피벗으로 정하여 분할을 수행
* 피벗 : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준
    1. 피벗을 제외한 배열의 가장 앞과, 뒤에서 시작
    2. 앞 : 앞에서부터 기준보다 큰 값이 나올때까지 순회
    3. 뒤 : 뒤에서부터 기준보다 작은 값이 나올때까지 순회
    4. 앞에서 큰 값을 찾고, 뒤에서 작은 값을 찾으면 교환
    5. 찾지 못하고, 서로를 지나치게 되면 작은 값과 기준을 교환

###### 2. 퀵 정렬 시간복잡도 -> O(NlogN)
* 선택, 삽입정렬은 O(N^2)이지만, 퀵 정렬은 O(NlogN)이다.
* 배열의 개수를 8이라 하였을 때, 표현을 쉽게 하였을 때 8/2/2/2 -> 3번에 정렬 종료
* 퀵 정렬은 이미 데이터가 정렬되어 있는 경우 매우 느리게 동작한다.(최악의 경우 N^2)
    ※ c++같은 퀵정렬을 기반으로 한 정렬을 제공하는 언어는 최악의 경우에도 O(NlogN)을 보장하도록 추가적인 로직을 더하였다.

#### 계수 정렬
###### 1. 계수 정렬 개요
* 특정한 조건이 부합할 때 사용 가능한, 매우 빠른 정렬 알고리즘
  ->  조건 : 데이터의 크기 범위가 제한되어 있을 때(정수로 표현 가능하여야함)
  ->  최악의 경우에도 시간복잡도 O(N+K)를 보장(N-데이터 개수, K-최댓값)
  ※ 일반적으로 큰 데이터와 작은 데이터의 차이가 백만을 넘지 않을 때 효과적
* 계수 정렬은 별도의 리스트를 선언하고, 그 안에 정렬에 대한 정보를 담음(비교기반x)
* 선언된 리스트에 각 데이터가 몇 번 등장하였는지 횟수를 기록


###### 2. 계수 정렬 시간복잡도 -> O(N+K)
* 데이터의 횟수를 기록할 배열 생성 및 배열 내 N개의 모든 데이터 순회 -> O(N)
* 데이터의 횟수가 기록된 배열을 순회, 개수만큼 반복 -> O(K+N)
* 현존 알고리즘 중, 기수 정렬과 더불어 가장 빠름(기수 정렬은 넓은 범위, 조금 느린 속도)

###### 3. 계수 정렬 공간복잡도 -> O(N+K)
* 데이터의 개수가 적고 범위가 넓은 경우 사용이 부적합
* 데이터의 개수가 매우 많을때 효과적으로 사용 가능

#### 파이썬의 정렬 라이브러리

###### sort함수 사용하기
* 변수를 선언하고 sorted(배열)을 입력하면 배열은 원상태, 정렬된 배열이 변수에 저장
* 배열.sort()를 사용하면 배열 자체가 정렬되어 저장된다.
* ex) result = sorted(array) //array는 정렬되지 않음
* ex) array.sort()  // array자체가 정렬되어 있음

###### 정렬 라이브러리의 시간 복잡도
* 정렬 라이브러리는 항상 최악의 경우에도 시간복잡도 O(NlogN)을 보장
* 정렬 라이브러리는 병합과 삽입을 더한 하이브리드 방식의 알고리즘
* 일반적으로 라이브러리를 사용하는 것이 효율적이며, 데이터 범위가 한정이라면 계수정렬