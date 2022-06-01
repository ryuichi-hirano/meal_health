import pandas as pd
import numpy as np
import streamlit as st

st.title('食事採点アプリ')

df = pd.read_csv('csv/standard.csv')
st.markdown('**各栄養素の一食当たりの推奨摂取量**')
st.dataframe(df)

sex = st.selectbox('性別を選択してください', ('男性', '女性', 'その他'))

kcal = st.text_input(label='カロリー(kcal): ', value=0)
try:
    kcal = float(kcal)
    st.write('kcal: ', kcal)
except:
    st.warning('数字(整数 or 小数)を入力してください')
    
protein = st.text_input(label='タンパク質(g): ', value=0)
try:
    protein = float(protein)
    st.write('protein: ', protein)
except:
    st.warning('数字(整数 or 小数)を入力してください')
    
fat = st.text_input(label='脂質(g): ', value=0)
try:
    fat = float(fat)
    st.write('fat: ', fat)
except:
    st.warning('数字(整数 or 小数)を入力してください')
    
carbohydrate = st.text_input(label='炭水化物(g): ', value=0)
try:
    carbohydrate = float(carbohydrate)
    st.write('carbohydrate: ', carbohydrate)
except:
    st.warning('数字(整数 or 小数)を入力してください')
    
standard = np.array([[900, 21, 18, 450],
                     [683, 16, 13, 333]])

standard = np.array([1/s for s in standard])

input_ = np.array([kcal, protein, fat, carbohydrate]).astype('float')

if sex == '男性':
    score = [np.dot(s, input_) for s in standard][0]
    
elif sex == '女性':
    score = [np.dot(s, input_) for s in standard][1]
    
elif sex == 'その他':
    score_m = [np.dot(s, input_) for s in standard][0]
    score_f = [np.dot(s, input_) for s in standard][1]
    
if sex == '男性' or sex == '女性':
    if score >= 4:
        t_score = int((4/score) * 100)
    else:
        t_score = int(score/4 * 100)
    st.write('この食事は', t_score, '点です')

elif sex == 'その他':
    if score_m >= 4 and score_f >= 4:
        t_score_m = int((4/score_m) * 100)
        t_score_f = int((4/score_f) * 100)
        
    elif score_m >= 4 and score_f < 4:
        t_score_m = int((4/score_m) * 100)
        t_score_f = int(score_f/4 * 100)
        
    else:
        t_score_m = int(score_m/4 * 100)
        t_score_f = int(score_f/4 * 100)
    st.write('この食事の男性スコアは', t_score_m, '点', ', 女性スコアは', t_score_f, '点です')
