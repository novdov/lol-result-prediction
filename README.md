# League of Legends 게임 결과 분석

## Data
- [OP.GG 랭킹](http://www.op.gg/ranking/ladder/) 1~1000위 (Challenger ~ Diamond 1)의 최근 20게임 중 솔로 랭크 기록
  - 수집 날짜: 2018. 06. 22
  - 총 데이터: 17,172건 (다시 시작을 제외한 승/패)
- 수집한 데이터
  - 게임 결과
  - 플레이 시간
  - 킬/데스/어시스트
  - KDA 비율 (Perfect인 경우 inf로 대체)
  - 킬 관여 비율
  - 와드
  - cs
  - 분당 cs

## Analysis & Modeling

<img src="/src/kda_results.png" width="430"> <img src="/src/heatmap.png" width="430">

- Visualization
- Classification
  - Random Forest
  - Logistic Regression
  - XGBoost
  
## Results
|           | Random Forest | Logistic Regression | XGBoost |
|-----------|---------------|---------------------|---------|
| Precision | 0.88          | 0.90                | 0.90    |
| Recall    | 0.88          | 0.90                | 0.90    |
| F1        | 0.88          | 0.90                | 0.90    |
- 세 모델 모두 0.88~0.90의 precision/recall을 보임
- Random Forest 모델에서 중요한 변수:
  - KDA 수치/킬 관여율/3 이상의 KDA
    - 얼마나 Death가 적으면서
    - 전체 킬에 많이 기여하는 지 (Kill/Assist)
    - KDA는 3을 넘을 것: KDA 3 이상이면 대부분 승리 (첫 번째 왼쪽 이미지)

<img src="/src/rf_fi.png" width="600">

## 고려하지 않은 것
- 포지션/챔피언
  - 게임을 2-3년 플레이 하지 않아 기존의 EU 메타 바텀 조합(원딜/서폿)이 흔들리는 상황에서 포지션 예측이 어려움
  - 현 메타 설명글(OP.GG): [롤 현 메타에 대한 분석글](http://www.op.gg/forum/view/702498)
- 티어별 데이터
  - 현재 고려한 티어는 Challenger ~ Diamond 1 (최상위 1000명)
  - 각 티어별 비교도 유의미할 것으로 보임 (메타/경기 수치 등)
- 팀 데이터
  - 글로벌 골드
  - 전체 킬
  - 입힌/받은 피해량
  - 글로벌 CS

## Future Work:
- 프로팀 경기 데이터를 이용한 모델링
- 데이터: [2015~2018 전세계 리그 경기 전적, (Kaggle)](https://www.kaggle.com/chuckephron/leagueoflegends/data)
