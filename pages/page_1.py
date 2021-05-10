import streamlit as st

def print_page():
    st.markdown('# Знакомство с Python')
    st.subheader('Первая программа на Python')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.code("""
    # Приветствие миру - традиционная 
    # первая строка в освоении
    # нового языка программирования 
    print('Привет, Мир!')
        """, language='python')
        st.code('Привет, Мир!', language='out')

    with col2:
        st.write('Любая строчка, начинающаяся с символа `#` — это комментарий, '
                 'примечание для разработчика.')

        st.code("""
    # эта команда показывает ”Zen of Python”
    import this
        """)

    st.subheader('Типы переменных')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.write('Переменные в Python могут быть разного типа — целые числа, дробные числа, строки:')

        st.code("""
    one_hundred = 100
    five_hundred = 500
    print(one_hundred + five_hundred)
            """)
        st.code('600', language='out')

        st.code("""
    first = 87.2
    second = 50.2
    third = 50.242
    print(first + second + third)
            """)
        st.code('187.642', language='out')

        st.code("""
    first = '87.2'
    second = '50.2'
    third = '50.242'
    # оператор + объединяет строки:
    print(first + second + third)
            """)
        st.code('87.250.250.242', language='out')

    with col2:
        st.write('Числа приводятся к строкам функцией `str()`:')
        st.code("""
    # объявляем две переменные разных типов:
    number = 100
    rubles = ' рублей'
    # сложить число и строку невозможно, 
    # поэтому приводим number к строке: 
    print(str(number) + rubles)
        """)
        st.code('100 рублей', language='out')

        st.write('Дробные числа приводятся к целым функцией int(). Она не округляет числа, '
                 'а отбрасывает дробную часть:')

        st.code("""
    # округление вниз, как привыкли
    print(int(3.14))
        """)
        st.code('3', language='out')

        st.code("""
    # а здесь всё равно округление вниз, 
    # хотя вроде бы так быть не должно
    print(int(2.72))
        """)
        st.code('2', language='out')

    st.subheader('Списки')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.write(
            'Списки — это последовательности, похожие на массивы из других языков программирования.'
            ' Они записываются в квадратных скобках через запятую:')
        st.code("""
    bremen_musicians = ['Трубадур', 'Кот', In 'Пёс', 'Осёл', 'Петух']   
    print(bremen_musicians)
            """)
        st.code('[’Трубадур’, ’Кот’, ’Пёс’, ’Осёл’, ’Петух’]', language='out')

        st.write('Чтобы подсчитать, сколько в списке элементов, вызывают стандартную функцию len():')
        st.code("""
    count = len(bremen_musicians)
    print(count)
            """)
        st.code(5, language='out')
    with col2:
        st.write('Список строк можно преобразовать в одну строку. '
                 'Для этого используется метод `join()`:')
        st.code("""
    print('Представляем музыкантов: ' + ', '.join(bremen_musicians))
        """)
        st.code('Представляем музыкантов: Трубадур, Кот, Пёс, Осёл, Петух', language='out')
