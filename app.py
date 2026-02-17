import streamlit as st
import plotly.express as px
import pandas as pd

st.subheader("Upload you data")

dataset = st.file_uploader(label="• Only upload csv files",type='csv')


st.sidebar.title("Data Filters")
if dataset is not None:
    df = pd.read_csv(dataset)
    num_var = df.select_dtypes(include='number')
    num_col = num_var.columns
    print("HI")

    with st.sidebar:
        select_col = st.sidebar.multiselect(label='Select features',options=num_col, default=num_col)
        num_col = select_col
        print("BYE")
        
    fig = px.imshow(df[num_col].corr(),text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df[num_col].head())


