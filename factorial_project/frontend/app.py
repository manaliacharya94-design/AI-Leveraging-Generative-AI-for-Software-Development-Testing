import streamlit as st
import sys
import os

# Correct path for deployment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(BASE_DIR, "src")

sys.path.append(SRC_PATH)

from factorial import FactorialCalculator