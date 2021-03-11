# I want to remember !!!

## 21.03.11
### Why string is immutable??
1. String 객체 캐싱
  - 메모리 절약 및 속도 향상
2. 보안
  - 해당 참조에 대한 문자열 값을 바꾸는 것이 불가능함으로 보안에 좋음
3. 스레드 안정성
  - 변경불가하므로 동시 참조해도 안전함

참고
https://dololak.tistory.com/699
https://www.baeldung.com/java-string-immutable
