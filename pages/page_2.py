import streamlit as st


def print_page():
    st.markdown("# Нелинейные алгоритмы")

    st.subheader("Циклы")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Пример цикла `for` в Python:")
        st.code(
            """
    bremen_musicians = ['Трубадур', 'Петух',
                        'Кот', 'Пёс', 'Осёл']
    print('Представляем музыкантов:') 
    for musician in bremen_musicians:
        print(musician)
        """
        )
        st.code(
            """
    Представляем музыкантов:
    Трубадур
    Петух
    Кот 
    Пёс 
    Осёл
        """,
            language="out",
        )

        st.write(
            "Переменная `musician` принимает последовательно "
            "значения всех элементов из списка `bremen_musicians`."
        )
    with col2:
        st.write("Ещё пример. Как пройтись по числам подряд:")
        st.code(
            """
    for i in range(1, 6): # range - диапазон 
        print(i)
    print('я иду тебя искать')
        """
        )
        st.code(
            """
    1
    2
    3
    4
    5
    я иду тебя искать
        """
        )

        st.write(
            "Внимание: `range(a, b)` возвращает числа от $a$ до $b-1$. Функция `reversed()` "
            "«переворачивает» списки и диапазоны значений:"
        )
        st.code(
            """
    for i in reversed(range(1, 6)):
        print(i)
    print('Поехали!')
        """
        )
        st.code(
            """
    5
    4
    3
    2
    1 
    Поехали!
        """,
            language="out",
        )

    st.subheader("Ветвления")
    st.write(
        "Логические выражения могут принимать логические значения "
        "`True` («истина») и `False` («ложь»)."
    )
    col1, col2 = st.columns(2)
    with col1:
        st.write("Условный оператор `if` для записи ветвления «если – то»:")
        st.code(
            """
    # в переменной beaufort хранится 
    # скорость ветра по шкале Бофорта 
    if beaufort == 0:
        print('штиль')
        """
        )

        st.write("Конструкция `if`-`else` для записи ветвления «если – то – иначе»:")
        st.code(
            """
    if beaufort == 0:
        print('штиль')
    else:
        print('есть ветер')
        """
        )

    with col2:
        st.write("Множественное ветвление:")
        st.code(
            """
    if beaufort == 0:
        print('штиль')
    elif beaufort == 1:
        print('тихий ветер')
    elif beaufort == 2:
        print('лёгкий ветер')
    elif beaufort == 3:
        print('слабый ветер')
    elif beaufort == 4:
        print('умеренный ветер')
    elif beaufort == 5:
        print('свежий ветер')
    elif beaufort == 6:
        print('сильный ветер')
        """
        )

        st.write(
            "Как только выполняется одно из условий — все нижеследующие elif и else пропускаются."
        )

    st.subheader("Логические выражения")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
        Операторы сравнения: 
        - равно `==`
        - меньше `<`
        - больше `>`
        - большеилиравно `>=`
        - меньшеилиравно `<=` 
        - неравно `!=`
        """
        )

    with col2:
        st.markdown(
            """
        Логические операторы:
        - `or` («или») — логическое сложение
        """
        )

        st.code(
            """
    if beaufort == 7 or beaufort == 8:
        print('крепкий ветер')
        """
        )

        st.markdown(
            """
        - `and` («и») — логическое умножение
        - `not` («не») — отрицание
        """
        )
