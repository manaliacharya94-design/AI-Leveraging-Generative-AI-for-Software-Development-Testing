import streamlit as st
import sys
import os

# Get path to src folder
current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
src_path = os.path.join(project_root, "src")

# Add src to Python path
sys.path.insert(0, src_path)

from factorial import FactorialCalculator

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