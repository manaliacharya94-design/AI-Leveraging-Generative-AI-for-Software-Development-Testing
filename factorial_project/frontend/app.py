import streamlit as st
import sys
import os

# Get absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add src folder to Python path
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_PATH)

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