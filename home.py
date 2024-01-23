import streamlit as st
import numpy as np

st.set_page_config("Survey Screening", page_icon="📝")

st.title("Screening for Adolescent Depression 📝")
q1 = st.number_input(
  "Q1: How old are you?", min_value = 12, max_value = 17
)

q2 = st.number_input(
  "Q2: During the past 12 months, how many different times have you been treated in an emergency room for any reason?", min_value = 0
)

q3 = st.radio(
  "Q3: During the past 12 months, have you stayed overnight or longer as an inpatient in a hospital?",
  options = ['Yes', 'No']
)

q4 = st.number_input(
  "Q4: During the past 12 months, how many times have you visited a doctor, nurse, physician assistant or nurse practitioner about your own health at a doctor’s office, a clinic, or some other place?",
  min_value = 0
)

st.header("Educational History")

q5 = st.radio(
  "Q5: Have you attended any type of school at any time during the past 12 months?",
  options = ['Yes', 'No']
)
