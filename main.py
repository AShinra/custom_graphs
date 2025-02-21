import streamlit as st
import pandas as pd
from my_barchart import create_barchart
from my_piechart import create_piechart



if __name__ == '__main__':

    st.set_page_config('Custom Charts',layout='wide')

    with st.sidebar:
        data = st.file_uploader('Upload file to use', type='csv')
        if data not in [None, '']:
            selected = st.radio('Select Chart to Create', options=['Bar', 'Pie', 'Line'])

    if data not in [None, '']:
        df = pd.read_csv(data)
        

        if selected == 'Bar':
            create_barchart(df)

        if selected == 'Pie':
            create_piechart(df)


