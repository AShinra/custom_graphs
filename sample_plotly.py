import streamlit as st
import pandas as pd
from my_barchart import create_barchart



if __name__ == '__main__':

    with st.sidebar:
        data = st.file_uploader('Upload file to use', type='csv')
        if data not in [None, '']:
            selected = st.radio('Select Chart to Create', options=['Bar', 'Pie', 'Line'])

    if data not in [None, '']:
        df = pd.read_csv(data)
        st.subheader('Yamaha Data')
        st.dataframe(df)

        if selected == 'Bar':
            create_barchart(df)


