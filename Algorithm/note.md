# 공부하며 알게 된 것.

- 파이썬 변수 scope 룰을 LEGB 룰이라고 불리기도 함
- 변수 값을 찾을 때, Local -> Enclosed -> Global-> Built-in
  1. Local - 가장 가까운 함수안 범위
  2. Enclosed - 함수를 내포하는 또 다른 함수 영역
  3. Globa - 함수 영역에 포함되지 않는 모듈 영역
  4. Built-in - 내장 
- https://open.oregonstate.education/computationalbiology/chapter/variables-and-scope/
- 파이썬에서 if, for, while 안에 선언된 변수들은 지역 변수가 아니라 블록 바깥의 스코프에서도 유지된다. 파이썬은 오직 함수 레벨의 스코핑을 사용한다.
