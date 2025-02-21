import streamlit as st
import plotly.express as px





def create_bar_chart(df):

    st.dataframe(df,use_container_width=True,height=200)

    x_data = st.selectbox('Select Data for x axis', options=df.columns)
    y_data = st.multiselect('Select Data for y axis', options=df.columns)

    cola, colb, colc = st.columns(3, border=True)
    

    with cola:
        title_text = st.text_input('Chart Title', placeholder='Chart Title')
        # cola1, colb1 = st.columns(2)
        # st.write('Title Settings')
        # with cola1:
        title_f_size = st.number_input("Font Size",min_value=8)
        # with colb1:
        title_f_color = st.color_picker("Font Color", '#0C09F1')
        title_f_style = st.radio('Font Style', options=['Normal', 'Italic'])

        if title_text in [None, '']:
            title_text = 'Chart Title'
        if title_f_style == 'Normal':
            f_style = 'normal'
        if title_f_style == 'Italic':
            f_style = 'italic'
    
    with colb:
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
        title=title_text,
        orientation='v',
        barmode=bar_mode
        )

    fig.update_layout(
        title_font=dict(
            size=title_f_size,
            family='Arial',
            color=title_f_color,
            style=f_style)
        )

    st.plotly_chart(fig)

    


    return