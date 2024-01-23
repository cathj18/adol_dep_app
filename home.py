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

st.subheader("Activities", divider="blue")

act1 = st.radio(
  "During the past 12 months, in how many different kinds of school-based activities, such as team sports, cheerleading, choir, band, student government, or clubs, have you participated?",
  options = ["0", "1", "2", "3 or more"]
)

act2 = st.radio(
  "During the past 12 months, in how many different kinds of community-based activities, such as volunteer activities, sports, clubs, or groups have you participated?",
   options = ["0", "1", "2", "3 or more"]
)

act3 = st.radio(
  "During the past 12 months, in how many different kinds of church or faith-based activities, such as clubs, youth groups, Saturday or Sunday school, prayer groups, youth trips, service or volunteer activities have you participated?",
  options = ["0", "1", "2", "3 or more"]
)

act4 = st.radio(
  "During the past 12 months, in how many different kinds of other activities, such as dance lessons, piano lessons, karate lessons, or horseback riding lessons, have you participated?",
  options = ["0", "1", "2", "3 or more"]
)

st.subheader("Treatment", divider="green")

trt1 = st.radio(
  "During the past 12 months, did you stay overnight or longer in a residential treatment center to receive treatment or counseling for emotional or behavioral problems that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt2 = st.radio(
  "During the past 12 months, did you stay overnight or longer in foster care or in a therapeutic foster care home because you had emotional or behavioral problems that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt3 = st.radio(
  "During the past 12 months, did you receive treatment or counseling at a partial day hospital or day treatment program because you had problems with your behavior or emotions that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt4 = st.radio(
  "During the past 12 months, did you receive treatment or counseling at a mental health clinic or center because you had problems with your behavior or emotions that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt5 = st.radio(
  "During the past 12 months, did you receive treatment or counseling from a private therapist, psychologist, psychiatrist, social worker, or counselor for emotional or behavioral problems that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt6 = st.radio(
  "During the past 12 months, did you receive treatment or counseling from an in-home therapist, counselor, or family preservation worker for emotional or behavioral problems that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt7 = st.radio(
  "During the past 12 months, did you receive treatment or counseling from a pediatrician or other family doctor for emotional or behavioral problems that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt8 = st.radio(
  "During the past 12 months, did you receive any treatment or counseling from a school social worker, a school psychologist, or a school counselor for emotional or behavioral problems that were not caused by alcohol or drugs?",
  options = ['Yes', 'No']
)

trt9 = st.radio(
  "At any time during the past 12 months, did you attend a school for students with emotional or behavioral problems?",
  options = ['Yes', 'No']
)

trt10 = st.radio(
  "At any time during the past 12 months, did you participate in a school program that was just for students with emotional or behavioral problems?",
  options = ['Yes', 'No']
)

st.subheader("Difficulties", divider="orange")

diff1 = st.radio(
  "Are you deaf or do you have serious difficulty hearing?",
  options = ['Yes', 'No']
)

diff2 = st.radio(
  "Are you blind or do you have serious difficulty seeing, even when wearing glasses?",
  options = ['Yes', 'No']
)

diff3 = st.radio(
  "Because of a physical, mental or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?",
  options = ['Yes', 'No']
)

diff4 = st.radio(
  "Do you have serious difficulty walking or climbing stairs?",
  options = ['Yes', 'No']
)

diff5 = st.radio(
  "Do you have difficulty dressing or bathing?",
  options = ['Yes', 'No']
)

st.subheader("Household", divider="violet")

hh1 = st.radio(
  "Do you have a mother in your household?",
  options = ["Yes", "No", "I don't know"]
)

hh2 = st.radio(
  "Do you have a father in your household?",
  options = ["Yes", "No", "I don't know"]
)

frequency = ["Always", "Sometimes", "Seldom", "Never"]

hh3 = st.radio(
  "During the past 12 months, how often did your parents check on whether you had done your homework?",
  options = frequency
)

hh4 = st.radio(
  "During the past 12 months, how often did your parents make you do chores around the house?",
  options = frequency
)

hh5 = st.radio(
  "During the past 12 months, how often did your parents limit the amount of time you watched TV?",
  options = frequency
)

hh6 = st.radio(
  "During the past 12 months, how often did your parents limit the amount of time you went out with friends on school nights?",
  options = frequency
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
  "During the past 12 months, did you stay overnight or longer in any type of juvenile detention center, sometimes called \"juvie\", prison, or jail?",
  options = ['Yes', 'No']
)
