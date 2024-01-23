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

st.subheader("Education", divider="green")

edu1 = st.radio(
  "Which of the statements below best describes how you felt overall about going to school during the past 12 months?",
  options = ["You liked going to school a lot", "You kind of liked going to school", "You didn t like going to school very much", "You hated going to school"]
)

edu2 = st.radio(
  "During the past 12 months, how often did you feel that the school work you were assigned to do was meaningful and important?",
  options = ["Always", "Sometimes", "Seldom", "Never"]
)

edu3 = st.radio(
  "How important do you think the things you have learned in school during the past 12 months are going to be to you later in life?",
  options = ["Very important", "Somewhat important", "Somewhat unimportant", "Very unimportant"]
)

edu4 = st.radio(
  "How interesting do you think most of your courses at school during the past 12 months have been?",
  options = ["Very interesting", "Somewhat interesting", "Somewhat boring", "Very boring"]
)

q5 = st.radio(
  "Q5: Have you attended any type of school at any time during the past 12 months?",
  options = ['Yes', 'No']
)

st.subheader("Legal History", divider="blue")

legal1 = st.radio(
  "Not counting minor traffic violations, have you ever been arrested and booked for breaking the law?",
  options = ['Yes', 'No']
)

legal2 = st.radio(
  "Were you on probation at any time during the past 12 months?",
  options = ['Yes', 'No']
)

legal3 = st.radio(
  "During the past 12 months, that is, since [DATEFILL], did you stay overnight or longer in any type of juvenile detention center, sometimes called \"juvie\", prison, or jail?",
  options = ['Yes', 'No']
)
