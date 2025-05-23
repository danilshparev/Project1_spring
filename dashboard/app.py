import streamlit as st
import pandas as pd



st.set_page_config(layout="wide")
st.title("Корреляция: Топ-5 Криптовалют и Топ-10 Акций Йоу Тралалеро тралала")

# Загрузка данных
df = pd.read_csv('./data/processed/merged_prices.csv', index_col=0, parse_dates=True)
df = df.dropna()

# Навигация
menu = ["Данные", "EDA", "Тренды и Закономерности", "Выводы"]
choice = st.sidebar.selectbox("Меню", menu)

if choice == "Данные":
    st.subheader(" Исходные данные")
    st.dataframe(df)
    st.write(f"Общее количество записей: {df.shape[0]}")
    st.write(f"Количество пропущенных значений: {df.isnull().sum().sum()}")

elif choice == "EDA":
    st.subheader(" Первичный анализ данных")
    st.write("Типы данных:")
    st.write(df.dtypes)
    st.write("Описание данных:")
    st.write(df.describe())

elif choice == "Тренды и Закономерности":
    st.subheader("Тренды и закономерности")
    selected_assets = st.multiselect("Выберите активы для отображения", df.columns.tolist(), default=df.columns[:5])
    if selected_assets:
        st.line_chart(df[selected_assets])



elif choice == "Выводы":
    st.subheader("Выводы")
    st.markdown("""
    - **Высокая корреляция** наблюдается между некоторыми криптовалютами (bitсoin, ethereum, solana, binance coin: в промежутке 0.61-0.84), что может свидетельствовать о схожих рыночных тенденциях. Binance Coin показывает наибольшую среднюю корреляцию — чуть менее 0.10.
Далее идут Solana и Ethereum, с корреляцией около 0.07 и 0.06 соответственно.
Bitcoin демонстрирует более низкую корреляцию (около 0.05), несмотря на свою популярность как актива.
Tether имеет самую низкую среднюю корреляцию (около 0.03).
Разброс средних значений корреляции также указывает на то, что даже в рамках криптовалют уровень зависимости от акций варьируется.
    - **Низкая корреляция** между криптовалютами и акциями указывает на их независимое поведение на рынке. Кроме того, между самими акциями тоже низкая и средняя корреляция.
    - Тепловая карта показала высокую положительную корреляцию среди большинства криптовалют (см. график “Матрица корреляций между активами”).
    - Акции крупнейших технологических компаний также продемонстрировали сильную взаимную связь.
    - Между криптовалютами и традиционными акциями корреляция низкая (0.02–0.12), что видно по скромным значениями в блоке “Корреляционная матрица” и на тепловой карте. При этом только между акциями корреляция выше, чем между акциями и криптовалютами. Максимальное значение коэффицента корреляции у акций достигает 0.71 у META/AMZN и MSFT/AMZN соответственно, в то время как максимальный коэффициент пары акция/криптовалюта достигает лишь 0.18 у TSLA/ethereum и TSLA/binancecoin.
    - **Трендовые особенности:** синхронные всплески 

В апреле–мае 2024 г. наблюдались локальные максимумы цен как криптовалют, так и технологических акций.

Линейные графики демонстрируют, что этот период был связан с общим “рисково-ориентированным” поведением рынка.

Расхождение трендов

В июне–июле 2024 г. цены криптовалют снизились сильнее, чем акции, что может быть объяснено повышением волатильности рынка цифровых активов при сравнительно стабильных отчётах корпораций.
    """)

