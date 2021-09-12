import streamlit as st


def print_page():
    st.markdown("# Строки и библиотеки")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("split() — разделение строк")

        st.write("Как разбить фразу на слова по пробелам:")

        st.code(
            """
    blok_string = 'Ночь. Улица.  Фонарь. Аптека.'
    blok_list = blok_string.split()
    # ['Ночь.', 'Улица.', 'Фонарь.', 'Аптека.']
        """
        )

        st.write("Можно указать, какой разделитель использовать для разбиения:")
        st.code(
            """
    blok_string = 'Ночь. Улица.  Фонарь. Аптека.'
    blok_list = blok_string.split('. ')
    # ['Ночь', 'Улица', 'Фонарь', 'Аптека']
        """
        )

        st.markdown(
            "Последнее слово можно взять в списке не только по индексу `len(blok_list) - 1`, "
            "но и проще, по индексу `-1`. Отрицательные индексы устроены вот так "
            "(индексы сверху и снизу — эквивалентны):"
        )

        st.code(
            """
       0       1        2         3
    ['Ночь', 'Улица', 'Фонарь', 'Аптека']
      -4      -3       -2        -1
        """
        )

    with col2:
        st.subheader("f-строки")
        st.write("Как ещё можно собирать строки из нескольких частей:")

        st.code(
            """
    one_hundred = 100
    rubles = 'рублей'
    friends = 'друзей'
    print(f'Не имей {one_hundred} {rubles}, а имей {one_hundred} {friends}.')
    # Не имей 100 рублей, а имей 100 друзей.
        """
        )

        st.write(
            "В f-строки можно подставлять не только переменные, но и результаты вычислений:"
        )
        st.code(
            """
    one_hundred = 100
    five_hundred = 500
    print(f'{one_hundred} + {five_hundred} = {one_hundred + five_hundred}')
    # 100 + 500 = 600
        """
        )

        st.write("Можно обратиться к элементам списка:")

        st.code(
            """
    russian_alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н'\
    ,'о','п', 'р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    print(f'{russian_alphabet[-1]} - последняя буква в алфавите.')
        """
        )

        st.write("К элементам словаря можно обратиться по ключу:")
        st.code(
            """
    favorite_songs = {
    'Тополиный пух': 'Иванушки international', 
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино'
    }
    song = 'Город золотой'
    print(f'{song} - одна из известных пеcен группы {favorite_songs[song]}.')
        """
        )

    st.subheader("Библиотеки")
    st.write(
        "Библиотека или модуль — это набор готовых функций, объединённых общей темой. "
        "Команда `import` в начале файла импортирует библиотеку — «подключает модуль». "
        "После чего можно вызывать функции из библиотеки."
    )

    col1, col2 = st.columns(2)
    col1.markdown("__Импортируем библиотеку целиком__")
    col2.markdown("__Импортируем только нужные функции__")

    st.write("В библиотеке math собраны функции для подсчёта математических величин:")
    col1, col2 = st.columns(2)
    col1.code(
        """
    import math
    value = math.sqrt(16)
        """
    )
    col2.code(
        """
    from math import sqrt
    value = sqrt(16)
    """
    )

    st.write("Модуль random используется для работы со случайными числами:")
    col1, col2 = st.columns(2)
    col1.code(
        """
    import random
    dice = random.randint(1, 6)
    """
    )

    col2.code(
        """
    from random import randint
    dice = randint(1, 6)
    """
    )
