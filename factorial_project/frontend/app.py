import streamlit as st

from src.factorial import FactorialCalculator

calc = FactorialCalculator()

st.title("Factorial Calculator")

number = st.number_input(
    "Enter a non-negative integer",
    min_value=0,
    max_value=1000,
    step=1
)

if st.button("Calculate"):
    try:
        result = calc.calculate(number)
        st.success(f"Result: {result:,}")
    except Exception as e:
        st.error(str(e))