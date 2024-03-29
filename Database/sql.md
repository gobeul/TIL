# SQL
데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

### 명령어 분류
1. DDL - 데이터 정의
2. DML - 데이터 조작(crud)
3. DCL - 데이터 제어

### syntax
모든 sql 문(Statement)은 세미콜론(;)으로 끝남.

대소 문자를 구분하진 않지만 대문자를 기본으로 하길 권장(구조파악을 위해)

- Statement (문)<br>
  독립적으로 실행할 수 있는 완전한 코드 조각, statement는 clause로 구성됨
- Clause (절)<br>
  statement 의 하위 단위

# SQL 명령어 종류
- DDL : 구조(테이블, 스키마)를 정의(생성, 수정, 삭제)하기 위한 명령어
- DML : 데이터를 조작(추가,조회,변경,삭제)하기 위한 명령어
- DCL : 데이터의 보안, 사용자의 권한 부여등을 정의하기 위한 명령어. (* SQLite 는 DCL 의 일부분은 지원하지 않는다.)

# SQLite Data Types

### 데이터 타입 종류
1. NULL
   정보가 없거나 알 수 없음을 의미한다.
2. INTEGER
   정수, 크기에 따라 0,1,2,3,4,6 또는 8바이트와 같은 가변 크기를 가진다.
3. REAL
   실수, 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수
4. TEXT
   문자 데이터
5. BLOB
   입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음), 예> 이미지 데이터

참고> SQLite 에는 별도의 Boolean 타입이 없다. (대신 0(false), 1(true) 로 저장됨)

### 제약조건
입력하는 데이터에 대해 제약을 정한다.<br>
제약에 맞지 않다면 입력이 거부된다.

데이터베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위함 (**데이터 무결성**)

1. NOT NULL
   컬럼이 NULL 값을 허용하지 않도록 지정한다.(기본값은 NULL값을 허용함)
2. UNIQUE
   컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함(예시로 유저의 email 같은거 받을때)
3. PRIMARY KEY (INTEGER 타입에만 사용가능)
   테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼<BR>
   각 테이블에는 하나의 기본 키만 있다.<br>
   암시적으로 NOT NULL 제약 조건이 걸려있다.
4. AUTOINCREMENT
   사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지한다.<br>
   PRIMARY KEY 다음에 작성하면 해당 rowid(pk)를 다시 재사용하지 못하도록한다. (장고에서 id 컬럼에 기본적으로 사용되는 제약조건)

### rowid
테이블을 생성할 때 마다 rowid 라는 컬럼이 자동으로 생성된다.<br>
1부터 시작하며 따로 값을 지정하지 않는다면 순차적으로 증가, 최대값에 도달하면 사용되지 않는 정수를 찾아 사용한다.