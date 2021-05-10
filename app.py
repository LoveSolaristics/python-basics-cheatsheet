import streamlit as st
from pages import page_4 as p4, page_3 as p3, page_5 as p5, page_2 as p2, page_1 as p1

from pathlib import Path
import base64


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


st.set_page_config(page_title='Python Basics',
                   layout='wide',
                   initial_sidebar_state='expanded')

with st.sidebar:
    st.title('Шпоргалка по Python')

    st.markdown("""
    Выжимка основных сведений о языке, необходимых для сдачи ЕГЭ по информатике
    с использованием Python.
    """)

    st.markdown("""
    ## Программное обеспечение
    
    Для комфортной работы с языком программирования следует скачать и установить следующие программы:
    - [Python](https://www.python.org/downloads/)
    - [Pycharm](https://www.jetbrains.com/pycharm/download/)
    
    ## Изучение языка
    """, unsafe_allow_html=True)

    page_names = ['Знакомство с Python',
                  'Нелинейные алгоритмы',
                  'Функции',
                  'Словари и множества',
                  'Строки и библиотеки']

    page = st.selectbox('Выберите часть, которую хотите изучить',
                        page_names)

    st.markdown('## Ресурсы')

    st.markdown(
        '''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://www.python.org) <small>Python 3.9.5 | Oct 2020</small>'''.format(
            img_to_bytes("images/python-logo.png")), unsafe_allow_html=True)

    st.markdown(
        '''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://streamlit.io) <small>Streamlit 0.81.1 | May 2021</small>'''.format(
            img_to_bytes("images/streamlit-logo.png")), unsafe_allow_html=True)

    st.markdown(
        '''
        ## Прочее
        [<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://vk.com/lovesolaristics) <small>Вопросы и предложения</small>'''.format(
            img_to_bytes("images/brain.png")), unsafe_allow_html=True)

    st.markdown(
        '''
        [<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
        (https://github.com/LoveSolaristics/python-basics-cheatsheet) <small>Исходный код</small>'''
        .format(img_to_bytes("images/github-logo.png")), unsafe_allow_html=True)

if page == page_names[0]:
    p1.print_page()
elif page == page_names[1]:
    p2.print_page()
elif page == page_names[2]:
    p3.print_page()
elif page == page_names[3]:
    p4.print_page()
elif page == page_names[4]:
    p5.print_page()
