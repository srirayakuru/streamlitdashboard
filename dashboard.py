import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
guanyuan_df = pd.read_csv('guanyuan.csv')



# Sidebar - Filter data
st.sidebar.header('Filter Data')
ambang_batas = st.sidebar.slider('Ambang Batas O3 (µg/m³)', min_value=100, max_value=300, value=180)

# Main dashboard
st.title('Dashboard Interaktif - Polusi Udara di Guanyuan')

# Correlation analysis
st.header('Korelasi PM2.5 dengan CO dan NO2')
correlation = guanyuan_df[['CO', 'NO2', 'PM2.5']].corr()
st.write(correlation)

# Scatter plots
st.subheader('Scatter Plot antara PM2.5 dan CO')
fig, ax = plt.subplots()
sns.scatterplot(x='CO', y='PM2.5', data=guanyuan_df, ax=ax)
ax.set_title('Scatter Plot antara PM2.5 dan CO')
st.pyplot(fig)

st.subheader('Scatter Plot antara PM2.5 dan NO2')
fig, ax = plt.subplots()
sns.scatterplot(x='NO2', y='PM2.5', data=guanyuan_df, ax=ax)
ax.set_title('Scatter Plot antara PM2.5 dan NO2')
st.pyplot(fig)

# O3 Analysis
above_threshold = guanyuan_df[guanyuan_df['O3'] > ambang_batas].shape[0]
below_threshold = guanyuan_df[guanyuan_df['O3'] <= ambang_batas].shape[0]

st.subheader(f'Analisis O3 - Ambang Batas: {ambang_batas} µg/m³')
st.write(f"Jumlah data dengan konsentrasi O3 di atas ambang batas: {above_threshold}")
st.write(f"Jumlah data dengan konsentrasi O3 di bawah ambang batas: {below_threshold}")

# Bar chart
categories = ['Above Threshold', 'Below Threshold']
values = [above_threshold, below_threshold]

fig, ax = plt.subplots()
ax.bar(categories, values, color=['red', 'green'])
ax.set_title(f'Konsentrasi O3 Di Atas dan Di Bawah Ambang Batas ({ambang_batas} µg/m³)')
ax.set_ylabel('Jumlah Data')
st.pyplot(fig)

st.sidebar.write('Streamlit dashboard by [Raya]')
