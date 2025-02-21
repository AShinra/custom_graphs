import streamlit as st
import pandas as pd
from bar_chart import create_bar_chart
from pie_chart import create_pie_chart


def main_window():

    with st.container(border=True):
        col1, col2 = st.columns(2, border=True)

        with col1:
            st.title('Bar Chart')
            st.file_uploader('Bar Data', key='bar_csv')

            if st.session_state['bar_csv'] not in [None, '']:
                bar_df = pd.read_csv(st.session_state['bar_csv'])
                create_bar_chart(bar_df)

                

        
        with col2:
            st.title('Pie Chart')
            st.file_uploader('Pie Data', key='pie_csv')

            if st.session_state['pie_csv'] not in [None, '']:
                pie_df = pd.read_csv(st.session_state['pie_csv'])
                create_pie_chart(pie_df)

    return






if __name__ == '__main__':

    st.set_page_config('Custom Charts',layout='wide')
    main_window()

