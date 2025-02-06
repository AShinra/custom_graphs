import streamlit as st
import pandas as pd
import plotly.express as px


def create_barchart(df):

    x_data = st.selectbox('Select Data for x axis', options=df.columns)
    y_data = st.multiselect('Select Data for x axis', options=df.columns[1:])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write('Title Settings')
        title_f_size = st.number_input("Font Size",min_value=8)
        title_f_color = st.color_picker("Font Color", '#0C09F1')
    
    with col2:
        group_selected = st.radio('Bar Mode', options=['Stack', 'Group', 'Overlay', 'Relative'])
        if group_selected == 'Stack':
            bar_mode = 'stack'
        elif group_selected == 'Group':
            bar_mode = 'group'
        elif group_selected == 'Overlay':
            bar_mode = 'overlay'
        elif group_selected == 'Relative':
            bar_mode = 'relative'    

   

    fig = px.bar(
        df,
        x=x_data,
        y=y_data,
        labels={'value':'Article Count', 'variable':''},
        title='Share of Voice - December 2024',
        orientation='v',
        barmode=bar_mode
        )

    fig.update_layout(
        title_font=dict(
            size=title_f_size,
            family='Arial',
            color=title_f_color
            )
        )

    st.plotly_chart(fig)

    