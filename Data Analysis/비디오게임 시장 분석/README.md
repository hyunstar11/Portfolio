# 비디오게임 시장 분석 (2021.12.08~13) 

### 비디오게임 시장 매출 데이터 분석을 통한 다음 분기에 설계할 게임 제안 

# 프로젝트 목차 

#### 1. 서론
 - 1.1. 분석 목적 
 - 1.2. 데이터셋에 대한 설명 

#### 2. 프로젝트 진행 과정 
- 2.1. EDA
- 2.2. 가설 검정
- 2.3. 시각화 및 데이터 분석
  - 2.3.1. 연도별 게임 판매량
  - 2.3.2. 출고량이 높은 게임에 대한 분석  
- 2.4 게임 추천 
#### 3. 한계점 및 향후 발전방향 



# 1. 서론 
### 1.1. 분석 목적 
- 다음 분기 신규 게임 개발을 위한 인사이트 도출 및 게임 시장 동향 파악

### 1.2. 데이터셋에 대한 설명 
- 결측치 제거 후 총 16,277개의 게임 데이터
- 지역별 매출실적(북미/유럽/일본/그 외)
- 게임 출시 연도(1980~2017), 플랫폼(31개), 게임 타이틀(11,330개) 

# 2. 프로젝트 진행 과정 
### 2.1. EDA
- 결측치 제거 및 중복 데이터 확인 

### 2.2. 가설 검정  
- Ho : 지역별로 선호하는 게임의 차이가 없다  
- Ha : 지역별로 선호하는 게임의 차이가 있다  

### 2.3. 시각화 및 데이터 분석 
- 각 지역별 장르 출고량 데이터 정리 및 시각화 
- 유일하게 일본만 선호하는 장르가 다름 (RPG, Action, Sports 순) 
<img width="1116" alt="스크린샷 2022-07-14 오후 5 22 50" src="https://user-images.githubusercontent.com/90128775/178936974-89568ab6-894e-4d8a-8371-7dbae22ecd36.png">

- F-Stat 가설검정으로 봐도 지역별로 선호하는 게임의 차이가 있음을 알 수 있음 
- P-value가 유의 수준 0.05 보다 작기 때문에 귀무가설인 Ho을 버리고 대립을 채택 
<img width="793" alt="스크린샷 2022-07-14 오후 5 27 26" src="https://user-images.githubusercontent.com/90128775/178937995-14ed811b-9691-405a-8476-161efd3a94e9.png">

#### 2.3.1 연도별 게임 판매량 
- 총 판매량 피크 후 급속한 하락
- 1990~2000년대 초반까지는 스포츠 게임이 시장의 강자 역할 
- 2003년 이후로는 액션 게임이 시장을 지배하기 시작함 
- 최근 몇 년 간은 데이터가 별로 없음? -> 최근의 트렌드를 파악하는데 어려움이 존재함 

<img width="298" alt="스크린샷 2022-07-14 오후 9 38 04" src="https://user-images.githubusercontent.com/90128775/178986564-6ed40529-a793-4958-9d83-695c2709d919.png">

<img width="292" alt="스크린샷 2022-07-14 오후 9 38 19" src="https://user-images.githubusercontent.com/90128775/178987689-065ddfd4-e816-4b2b-84bd-0e2c6043d0d3.png">

#### 2.3.2. 출고량이 높은 게임에 대한 분석 
- 어떤 게임들이 출고량이 높은가? -> 닌텐도사의 게임들이 전반적으로 높은 출고량을 자랑함 
<img width="696" alt="스크린샷 2022-07-14 오후 10 13 33" src="https://user-images.githubusercontent.com/90128775/178990820-0f2d3313-c1b7-4b3f-a1f3-2505f98801f3.png">

- Top 10 판매량 게임들의 경우 플랫폼, 스포츠 순으로 많았음 
<img width="317" alt="스크린샷 2022-07-14 오후 10 13 48" src="https://user-images.githubusercontent.com/90128775/178990830-2d6828a9-57f1-4dfa-89ce-ddfb96cb4446.png">

### 2.4 게임 추천 
- 여러가지 방법이 있겠지만 시장의 평균적인 퍼포먼스를 따라가는 방법을 선택 -> 'MISC' 카테고리에 해당하는 게임을 설계하는 걸 추천 
- 공략해야 될 시장으로는 판매량이 확실히 높은 북미 + 유럽 시장을 위주로 공략 
<img width="775" alt="스크린샷 2022-07-14 오후 10 15 43" src="https://user-images.githubusercontent.com/90128775/178991581-db922761-27d9-4478-9340-65b60490c891.png">

<img width="869" alt="스크린샷 2022-07-14 오후 10 15 54" src="https://user-images.githubusercontent.com/90128775/178991599-177d0dab-8855-493c-9d62-8183d10f88da.png">

# 3. 한계점 및 향후 발전방향 
- 부트캠프를 시작하고 한 달만에 처음 했던 프로젝트가 어색한 점들이 많았음
- 좀 더 효율적인 시각화 방법 + 깔끔한 이미지 사용 (Matplotlib 대신에 Seaborn 사용)  

