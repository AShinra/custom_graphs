import streamlit as st




def create_pie_chart(df):

    st.dataframe(df,use_container_width=True,height=200)

    return