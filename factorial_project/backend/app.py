import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from factorial import FactorialCalculator

calc = FactorialCalculator()

st.title("Factorial Calculator")

number = st.number_input("Enter a non-negative integer", min_value=0, max_value=1000, step=1)

if st.button("Calculate"):
    result = calc.calculate(number)
    st.success(f"Result: {result:,}")