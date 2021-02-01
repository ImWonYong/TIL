# 공부하며 알게 된 것.

- 파이썬 변수 scope 룰을 LEGB 룰이라고 불리기도 함
- 변수 값을 찾을 때, Local -> Enclosed -> Global-> Built-in
  1. Local - 가장 가까운 함수안 범위
  2. Enclosed - 함수를 내포하는 또 다른 함수 영역
  3. Globa - 함수 영역에 포함되지 않는 모듈 영역
  4. Built-in - 내장 
- https://open.oregonstate.education/computationalbiology/chapter/variables-and-scope/
- 파이썬에서 if, for, while 안에 선언된 변수들은 지역 변수가 아니라 블록 바깥의 스코프에서도 유지된다. 파이썬은 오직 함수 레벨의 스코핑을 사용한다.
- list comprehension에 대해 https://minjoos.tistory.com/3
  1. 수학 시간에 배운 {w | w ⊂ V & P(w)} 이런 것. 집합 V에 속하는 원소 w중에, 성질 P를 만족하는 모든 w들의 집합
  2. [w for w in V if P(w)]가 된다.
- 2차원 리스트 생성 및 입력 받기 https://minjoos.tistory.com/2
