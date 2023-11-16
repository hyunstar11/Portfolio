# Bitcoin Price Directional Prediction Model (2022.03.17-22)

# Project Table of Contents 

#### 1. Introduction
 - 1.1. Problem Statement
 - 1.2. Description of the dataset 

#### 2. Project Steps  
- 2.1. Data EDA & Preprocessing 
- 2.2. Modeling & Results 

#### 3. Reflection 

# 1. Introduction 
### 1.1. Problem Statement
- Purpose: To create a deep learning model that predicts the price direction of bitcoin, which is like an index in the cryptocurrency market (up or down). 
  - Stock price/bitcoin prediction models commonly found on the internet are prone to summation of processes 
    - Why?: Because they use non-stationary data instead of stationary data 
  - Problem : Can we create a model that helps us with trading/investment decisions based on data (price) to minimize FOMO? 

### 1.2. Description of the dataset 
- I used Alpha Vantage's API to get daily Bitcoin price data (Open, Low, Close, Volume) 

# 2. Project Progress 
### 2.1. Data EDA & Preprocessing 
- Time period: Set data from January 2021 to April 2022, when I was working on the project. 
  - Rationale for the Time period selection: Significant institutional buying of Bitcoin starting in 2021 (e.g. Tesla, Fidelity Investments, Nexon, etc.) 
- Preprocessed closing prices for binary classification models: changed to 1 for positive closes and 0 for negative closes   
- Converting data from non-stationary to stationary (today's price - previous day's price) 
  - Why Stationary data? - Data with constant mean, covariance -> better for creating predictive models


- Time Period: January 2021 to April 2022, a period when I was actively engaged in this project.
  - Rationale for Time Period Selection: This timeframe witnessed significant institutional investment in Bitcoin, exemplified by major purchases from entities such as Tesla, Fidelity Investments, and Nexon. The influx of institutional investors during this period likely influenced market behavior, making it an ideal subject for analysis.
- Preprocessing of Closing Prices for Binary Classification Models: For simplification, the closing prices were processed into a binary format, where a positive close is represented as 1 and a negative close as 0. This binary representation is aimed at facilitating the classification task in the predictive models.
- Converting Data from Non-Stationary to Stationary: I transformed the data to a stationary format by calculating the difference between the current day’s price and the previous day’s price.
- Importance of Stationary Data: Stationarity in time series data, characterized by constant statistical properties like mean and covariance, is crucial for the effectiveness of many predictive models. Stationary data tends to be more predictable and its consistency allows for more reliable statistical inference. This is particularly important for models that are based on the assumption of stationarity, such as ARIMA. While not all models require stationary data, converting to a stationary format often simplifies the analysis and helps in avoiding misleading results due to spurious correlations in non-stationary data. However, it’s important to approach this transformation judiciously, as it can sometimes lead to the loss of important information or introduce other complexities.

### 2.2. Modeling & Results 

- To predict the price direction of Bitcoin 1). Develop a price prediction model with stationary data 2). Developed a price prediction model using binary classification 
- Normalized the data (converted to 0~1) to increase the performance of the model 
  - View several days of data and set a window 
- Use LSTM by default
  - What is LSTM: Passing on some of the previous data information to the next analysis 
  - Why: Great for time series data 

- 2.2.1. The first model 
  - LSTM model for stationary data 
<img width="770" alt="screenshot 2022-07-23 1 04 33 am" src="https://user-images.githubusercontent.com/90128775/180481895-59407c17-86bf-44d1-882f-815d62fb18d0.png">

- 2.2.2. Second Model 
  - Proceed to binary classification
<img width="783" alt="Screenshot taken on 2022-07-23 at 1 04 55" src="https://user-images.githubusercontent.com/90128775/180481910-f4445f92-2529-4824-97dd-0680f5d10e18.png">

- 2.2.3. Evaluation 
<img width="1294" alt="Screenshot 2022-07-23 AM 1 26 47" src="https://user-images.githubusercontent.com/90128775/180483039-9f4dde5a-e5ea-43cb-b154-2b73949e5a53.png">

- After evaluation, we concluded that the binary classification model performed better (0.644 accuracy) 


# 3. Retrospective and future development  
- If we had more time, we could pay more attention to the design of the deep learning model and expect better performance. 
- Additional model validation and hyper-parameter tuning 
- Try modeling with other models other than LSTM, such as ARIMA and ETS, which are known to be suitable for time series data.


____________________________________________________________________________________


# 비트코인 가격 방향성 예측 모델 (2022.03.17~22)

# 프로젝트 목차 

#### 1. 서론
 - 1.1. 문제
 - 1.2. 데이터셋에 대한 설명 

#### 2. 프로젝트 진행 과정 
- 2.1. 데이터 EDA & 전처리 
- 2.2. 모델링 & 결과 

#### 3. 회고 및 향후 발전방향  

# 1. 서론 
### 1.1. 문제
- 목적: 암호화폐 시장에서 인덱스 지표와도 같은 같은 비트코인의 가격 방향성을 예측하는 딥러닝 모델을 만드는 것 (가격의 상방 혹은 하방) 
  - 인터넷에서 흔히 접할 수 있는 주가/비트코인 예측 모델들의 경우 과정합이 자주 발생함 
    - Stationary가 아닌 Non-stationary 데이터를 사용하기 때문 
  - FOMO 하지 않고 데이터 (가격) 기반으로 매매/투자 결정에 도움이 되는 모델을 만들 수 있을까? 하는 질문에서 시작 
  - 평소에 관심 있어하던 도메인이여서 선택
 

### 1.2. 데이터셋에 대한 설명 
- Alpha Vantage사의 API를 사용하여 일별 비트코인 가격 데이터를 받아옴 (시가,저가,종가,거래량) 

# 2. 프로젝트 진행 과정 
### 2.1. 데이터 EDA & 전처리 
- 기간 설정 : 2021년 1월부터 프로젝트를 진행했던 2022년 4월까지의 데이터로 설정 
  - 이유: 2021년을 기점으로 기관들의 유의미한 비트코인 매수가 이루어짐 (e.g. 테슬라, Fidelity Investments, Nexon 등) 
- 이진 분류 모델을 위한 종가 전처리: 양봉 마감 시 1, 음봉 마감시 0 으로 변경   
- 데이터를 Non-Stationary 에서 Stationary (금일 가격 - 전일 가격) 으로 변환 
  - 왜 Stationary 데이터? - 평균분산, 공분산이 일정한 데이터 -> 예측 모델을 만들기에 더 적합

<img width="801" alt="스크린샷 2022-07-23 오전 1 47 29" src="https://user-images.githubusercontent.com/90128775/180486557-abb9ddaa-c830-42a5-a495-9cfd80ee41b6.png">

### 2.2. 모델링 & 결과 

- 비트코인의 가격 방향을 예측하기 위해 1). Stationary Data로 가격 예측 모델 개발 2). 이진분류로 가격 상하방 예측 모델 개발 
- 모델의 성능을 높이기 위해 데이터 정규화 진행(0~1 로 변환) 
  - 며칠간의 데이터를 보고 window도 설정 
- 기본적으로 LSTM을 사용
  - LSTM이란?: 이전 데이터 정보 일부를 다음 분석에 넘겨줌 
  - 선정이유: 시계열 데이터에 적합 

- 2.2.1. 첫 번째 모델 
  - Stationary Data 에 대한 LSTM 모델 
<img width="770" alt="스크린샷 2022-07-23 오전 1 04 33" src="https://user-images.githubusercontent.com/90128775/180481895-59407c17-86bf-44d1-882f-815d62fb18d0.png">

- 2.2.2. 두 번째 모델 
  - 이진분류로 진행
<img width="783" alt="스크린샷 2022-07-23 오전 1 04 55" src="https://user-images.githubusercontent.com/90128775/180481910-f4445f92-2529-4824-97dd-0680f5d10e18.png">

- 2.2.3. Evaluation 
<img width="1294" alt="스크린샷 2022-07-23 오전 1 26 47" src="https://user-images.githubusercontent.com/90128775/180483039-9f4dde5a-e5ea-43cb-b154-2b73949e5a53.png">

- 검토 결과 이진분류 모델의 성능이 더 우수한 것으로 판단 (0.644 accuracy) 


# 3. 회고 및 향후 발전방향  
- 시간이 좀 더 있다면 딥러닝 모델 디자인에 좀 더 신경쓸 수 있을 것이고 더 좋은 성능을 낼 수 있을 것으로 기대 
- 추가적인 모델 검증 및 하이퍼 파라미터 튜닝 
- LSTM 말고 시계열 데이터에 적합하기로 알려진 ARIMA, ETS와 같은 다른 모델들로 모델링 해볼 것 



