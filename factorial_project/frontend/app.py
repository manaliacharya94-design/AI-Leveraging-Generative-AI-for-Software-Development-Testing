import streamlit as st
import sys
import os

st.set_page_config(
    page_title="Factorial Calculator",
    page_icon="∫",
    layout="centered"
)

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
src_path = os.path.join(project_root, "src")
sys.path.insert(0, src_path)

from factorial import FactorialCalculator

calc = FactorialCalculator()

# --- Header ---
st.markdown("""
    <div style='text-align: center; padding: 20px 0'>
        <h1 style='font-size: 72px; font-weight: 900; letter-spacing: -2px; margin: 0'>n!</h1>
        <p style='letter-spacing: 4px; font-size: 11px; color: gray; text-transform: uppercase; margin: 4px 0'>
            FACTORIAL CALCULATOR — VERTEX AI ASSIGNMENT
        </p>
    </div>
""", unsafe_allow_html=True)

# --- Session state for history ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Input ---
st.markdown("**ENTER A NON-NEGATIVE INTEGER**")
number = st.number_input("", min_value=0, max_value=1000, step=1, value=0)

# --- Calculate ---
if st.button("Calculate →"):
    try:
        result = calc.calculate(number)

        st.markdown(f"""
            <div style='border: 1px solid #333; border-radius: 10px; padding: 20px; margin-top: 16px'>
                <p style='color: gray; font-size: 11px; letter-spacing: 3px; text-transform: uppercase'>RESULT</p>
                <p style='font-size: 14px; color: gray; margin: 4px 0'>{int(number)}! =</p>
                <h2 style='font-size: 42px; font-weight: 800; color: #d4f500; margin: 0'>{result:,}</h2>
            </div>
        """, unsafe_allow_html=True)

        st.session_state.history.append({"n": int(number), "Result": f"{result:,}"})
        if len(st.session_state.history) > 8:
            st.session_state.history = st.session_state.history[-8:]

    except Exception as e:
        st.error(str(e))

# --- History ---
if st.session_state.history:
    st.markdown("---")
    st.markdown("**HISTORY**")
    st.table(st.session_state.history)
    if st.button("Clear history"):
        st.session_state.history = []
        st.rerun()