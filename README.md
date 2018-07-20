## Anaylsis of League of Legends Matches

## Data
- Recent 20 solo ranked games of  [OP.GG rank](http://www.op.gg/ranking/ladder/) 1~1,000 (Challenger ~ Diamond 1)
  - Collection Dates: 2018. 06. 22
  - Total Data: 17,172 (Victory/Defeat except regame)
- Data collected
  - Results (Victory/Defeat)
  - Play time
  - Kill/Death/Assist
  - KDA ratio (Assigned infinity number if it is Perfect)
  - Contribution to Kill
  - Wards
  - CS
  - CS per minutes

## Analysis & Modeling

<img src="/src/pyplot_kda_range.png" width="430"> <img src="/src/pyplot_tier.png" width="430">

<img src="/src/kda_tier.png" width="430"> <img src="/src/pkill_tier.png" width="430">

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
- Precision/Recall of all models are 0.88~0.90.
- Feature importance in Random Forest:
  - KDA ration/Kill contribution/KDA over 3
    - How players don't die,
    - How much players contribute to total kill (kill/assist)
    - KDA ratio over 3: High probability for Victory when KDA exceed 3

<img src="/src/rf_fi.png" width="600">

## Those not analyzed
- Position/Champion
  - Diffuculites with anayzing current meta which especially bottom is different wit previous EU meta
  - Description of current meta: [롤 현 메타에 대한 분석글](http://www.op.gg/forum/view/702498)
- Tier Differences
  - Current data are results of Challenger ~ Diamond 1
  - Comparison by Tier would be meaningful.
- Team Data
  - Global Gold
  - Global CS
  - Total Kill
  - Damage

## Future Work
- Anaysis using data of pro league (LCK, LCS ..)
- Data: [League of Legends Competitive matches, 2015 to 2018 (Kaggle)](https://www.kaggle.com/chuckephron/leagueoflegends/data)

