## Anaylsis of League of Legends Matches

### Notebooks on nbviewer (for plotly plots)
- [eda_tier.ipynb](http://nbviewer.jupyter.org/github/novdov/lol-result-prediction/blob/master/eda_tier.ipynb)
- [modeling.ipynb](http://nbviewer.jupyter.org/github/novdov/lol-result-prediction/blob/master/modeling.ipynb)

## Data
- Recent 20 solo ranked games of  [OP.GG rank](http://www.op.gg/ranking/ladder/) 1~1,000 (Challenger ~ Diamond 2)
  - Collection Dates: 2018. 06. 22/26(with tier)
  - Total Data: 17,172 (Victory/Defeat except regame)
- Data collected
  - Results (Victory/Defeat)
  - Tier
  - Play time
  - Kill/Death/Assist
  - KDA ratio (Assigned infinity number to Perfect KDA)
  - Contribution to Kill
  - Wards
  - CS
  - CS per minutes

## Analysis & Modeling

<img src="/src/pyplot_kda_range.png" width="430"> <img src="/src/pyplot_tier.png" width="430">

<img src="/src/kda_tier.png" width="430"> <img src="/src/pkill_tier.png" width="430">

- Visualization (with/without tier)
  - Relationships between Victory/Defeat and other variables
  - seaborn & plot.ly used
- Classification (without tier)
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

<img src="/src/rf_fi_plotly.png" width="800">

## Those not analyzed
- Position/Champion
  - Diffuculites with anayzing current meta which especially bottom is different wit previous EU meta
  - Description of current meta: [롤 현 메타에 대한 분석글](http://www.op.gg/forum/view/702498)
- Team Data
  - Global Gold
  - Global CS
  - Total Kill
  - Damage

## Future Work
- Anaysis using data of pro league (LCK, LCS ..)
- Data: [League of Legends Competitive matches, 2015 to 2018 (Kaggle)](https://www.kaggle.com/chuckephron/leagueoflegends/data)

