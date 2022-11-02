from multiprocessing import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('タイトル')
st.write('Interactive Widgets')

left_column, right_column = st.columns(2)

button = left_column.button('右からむに表示')
if button :
    right_column.write('右のからむです')

condition = st.sidebar.slider('あなたの今の調子は？', 10, 20, 13)

'コンディション：', condition

# if st.checkbox('show image'):
#     img = Image.open('sample1.png')
#     st.image(img, caption='sample image', use_column_width=True)



df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

#st.table(df.style.highlight_max(axis=0))

st.map(df, zoom=condition)  