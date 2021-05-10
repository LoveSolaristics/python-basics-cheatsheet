import streamlit as st


def print_page():
    st.markdown('# Словари и множества')
    st.subheader('Словари')

    col1, col2 = st.beta_columns(2)
    with col1:
        st.write('Словарь (`dict`) оформляется фигурными скобками. Его заполняют пары, '
                 'записанные через запятую. Первый элемент в паре называется ключ, '
                 'а второй — значение, они разделяются между собой двоеточием.')
    with col2:
        st.code("""
    english = {
        'рука': 'hand',
        'нога': 'leg',
        'разработчик': 'developer'
    }
    # доступ по ключу: как по-английски рука?
    print(english['рука'])
    english['рука'] = 'arm'
    # значение для ключа 'рука'
    # поменялось с 'hand' на 'arm'
        """)

    st.write('Пройти по всем элементам словаря можно циклом `for`, причём есть несколько вариантов:')
    st.code("""
    favorite_songs = {
        'Тополиный пух': 'Иванушки international', 
        'Город золотой': 'Аквариум',
        'Звезда по имени Солнце': 'Кино',
        'Группа крови': 'Кино'
    }

    for track in favorite_songs:
        print(track + ' это песня группы ' + favorite_songs[track]) 

    for music_band in favorite_songs.values():
        print('Доктор, я больше не могу слушать группу ' + music_band) 

    for track, music_band in favorite_songs.items():
        print(track + ' это песня группы ' + music_band)
    """)

    st.write('Метод `.keys()` возвращает все ключи словаря, а метод `.values()` — все значения.')

    st.subheader('Множества')
    col1, col2 = st.beta_columns(2)
    with col1:
        st.markdown("""
        Тип `set` похож на список, но есть два важных отличия:
        - элементы во множестве не повторяются;
        - не гарантируется, что при выводе элементов на экран \
        будет соблюден какой-то определённый порядок.
        """)

        st.code("word_set = {'hand', 'leg', 'developer'}")

        st.write('Метод `.union()` объединяет два множества:')

        st.code("""
    songs1 = {
        'Три белых коня',
        'Happy new year',
        'Снежинка'
    }
    songs2 = {
        'Last christmas',
        'Снежинка',
        'Happy new year'
    }
    print(songs1.union(songs2))
    # 'Три белых коня', 'Снежинка',
    # 'Last christmas', 'Happy new year'
        """)

    with col2:
        st.code("""
    # получаем сет unique_band_names
    # (с англ. «уникальные названия групп») 
    unique_band_names = set(bands)
    for band in unique_band_names:
        print('Не могу больше слушать', band)
        """)

        st.write('Проверка наличия элемента')
        st.code("""
    if 'Аквариум' in unique_band_names:
        print('есть такое!')
    if 'body' not in word_set:
        print('нету')
        """)

        st.write('Метод `.difference()` возвращает разницу множеств, '
                 'а метод `.intersection()` — их пересечение.')
