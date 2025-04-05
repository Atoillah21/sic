import streamlit as st
import numpy as np
import pandas as pd

st.title('Coba Streamlit')
st.write("Data suhu pada hari ini:")
st.write(pd.DataFrame({
    'Waktu (jam)': [6, 7, 8, 9],
    'Suhu (°C)': [23, 25, 26, 33]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 1),
     columns=['Suhu (°C)'])

st.line_chart(chart_data)
    
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)