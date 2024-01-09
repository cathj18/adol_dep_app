import streamlit as st
import numpy as np

st.title("Survey Screening for Adolescent Depression")
q1 = st.number_input(
  "How old are you?", min_value = 12, max_value = 17
)
