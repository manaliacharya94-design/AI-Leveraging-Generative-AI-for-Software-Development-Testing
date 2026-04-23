import streamlit as st
from src.factorial import FactorialCalculator

calc = FactorialCalculator()

st.set_page_config(page_title="Factorial App", layout="centered")

st.title("🧮 Factorial Calculator")
st.markdown("Enter a number to compute its factorial")

col1, col2 = st.columns(2)

with col1:
    number = st.number_input("Number", min_value=0, step=1)

with col2:
    st.write("")  # spacing
    st.write("")
    if st.button("Calculate"):
        try:
            result = calc.calculate(number)
            st.success(f"{number}! = {result:,}")
        except Exception as e:
            st.error(str(e))

st.divider()
st.caption("Built using Streamlit + Vertex AI")