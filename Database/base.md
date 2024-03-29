# 데이터베이스 기초 용어

### 데이터베이스
체계화된 데이터의 모임

검색 및 고조화 작업을 보다 쉽게 하기 위해 체계회 시킨 것이다.

기본 구조로 스키마와 테이블을 가진다.

### 스키마(Schema)
뼈대.

데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

### 테이블(Table)
필드와 레코드를 사용해 조직된 데이터 요소들의 집합으로 관계하고도 부름

### 필드(field)
속성, 열(column),

데이터의 타입을 의미

### 레코드(record)
튜플, 행(row)

데이터를 입력했다 = 하나의 레코드를 작성했다.

### PK(Primary Key)
각 레코드릐 고유한 값으로 식별자로서 사용된다.

다른 항목과 중복될 수 없는 단일 값

ex) 주민등록번호

### 쿼리(Query)
데이터를 조회하기 위한 명령어

쿼리는 날린다 = 데이터베이스를 조작한다.

---

# 데이터의 저장
데이터를 저장하는 장소는 무엇이있을까
1. 파일
  - 쉽고 간편하게 사용이 가능하지만 보안, 성능, 대용량 등의 측면에서 한계가 있다.
2. 스레드시트
  - 엑셀시트. 컬럼(열), 레코드(행)을 통해 데이터 값 저장. 이를 데이터베이스라고 할 순 없지만 db로가는 길목 정도?
3. 데이터베이스
  - 프러그래밍 언어를 사용해 작동 가능, RDB(광계형데이터베이스)를 가장 자주 쓰며, 이는 마치 스프레드시트 파일 모음과 비슷함


# 데이터베이스 란??
- 체계화된 데이터의 모임.
- 검색, 구조화 같은 작업을 쉽게하기 위함
- db를 조작하는 프로그램 = DBMS(database managements system)<br>
오라클, mysql, sqlite 등, 이때 사용하는 언어는 SQL 이다.

# RDB
RDB 란 Relational Database 관계형 데이터 베이스<br>
한 테이블에서 다른 테이블의 정보를 어떻게 연결 시킬것인지

### RDB의 장점
- 데이터의 직관전 표현 가능
- 관련한 데이터에 쉽게 접근 가능
- 대량의 데이터도 효율적으로 관리 가능

# SQL
데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

SQL을 통해 데이터베이스의 동작원리를 알 수 있다!
# SQLite
파일로 데이터를 관리함.<br>
비교적 가벼운 데이터 베이스<br>
대규모 동시 처리에는 적합치 않음<br>
높은 호환성<br>
장고의 기본 데이터베이스<br>


