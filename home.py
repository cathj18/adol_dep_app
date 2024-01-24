import streamlit as st
import numpy as np

st.set_page_config("Survey Screening", page_icon="📝")

st.title("Screening for Adolescent Depression 📝")

yn = ['Yes', 'No']
frequency = ["Always", "Sometimes", "Seldom", "Never"]

q1 = st.number_input(
  "How old are you?", min_value = 12, max_value = 17
)

q2 = st.radio(
  "What gender were you assigned at birth?",
  options = ['Female', 'Male']
)

q3 = st.radio(
  "Which race or ethnicity best describes you?",
  options = ['American Indian or Alaskan Native', 'Black or African American', 'Hispanic', 'Asian', 'Native Hawaiian / Other Pacific Islander', 'White / Caucasian', 'Multiple ethnicity / Other']
)

st.subheader("Education", divider="green")

edu0 = st.radio(
  "Have you attended any type of school at any time during the past 12 months?",
  options = yn
)

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

edu5 = st.radio(
  "During the past 12 months, how often did your teachers at school let you know when you were doing a good job with you school work?",
  options = frequency
)

edu6 = st.radio(
  "What were your grades for the last semester or grading period you completed?",
  options = frequency
)

st.subheader("Programs", divider="blue")

prog1 = st.radio(
  "During the past 12 months have you participated in a problem solving, communication skills or self-esteem group?",
  options = yn
)

prog2 = st.radio(
  "During the past 12 months have you participated in a violence prevention program, where you learn ways to avoid fights and control anger?",
  options = yn
)

st.subheader("Health", divider="blue")

health0 = st.radio(
  "Would you say your health in general is excellent, very good, good, fair, or poor?",
  options = ['Excellent', 'Very good', 'Good', 'Fair', 'Poor']
)

health1 = st.number_input(
  "During the past 12 months, how many different times have you been treated in an emergency room for any reason?", min_value = 0
)

health2 = st.radio(
  "During the past 12 months, have you stayed overnight or longer as an inpatient in a hospital?",
  options = ['Yes', 'No']
)

health3 = st.number_input(
  "During the past 12 months, how many times have you visited a doctor, nurse, physician assistant or nurse practitioner about your own health at a doctor’s office, a clinic, or some other place?",
  min_value = 0
)

st.subheader("Life", divider="blue")

life2 = st.radio(
  "How many times in the past 12 months have you moved? Please include moves from one residence to another within the same city/town as well as those from one city/town to another.",
  options = ['0', '1', '2', '3 or more']
)

life3 = st.radio(
  "How well do you speak English?",
  options = ['Very well', 'Well', 'Not well', 'Not at all']
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

st.subheader("Religion", divider="grey")

disagr = ["Strongly Disagree", "Disagree", "Strongly Agree", "Agree"]

relig1 = st.radio(
  "Your religious beliefs are a very important part of your life.",
  options = disagr
)

relig2 = st.radio(
  "Your religious beliefs influence how you make decisions in your life.",
  options = disagr
)

relig3 = st.radio(
  "It is important that your friends share your religious beliefs.",
  options = disagr
)

st.subheader("Parental Monitoring", divider="blue")

par1 = st.radio(
  "During the past 12 months, how often did your parents check on whether you had done your homework?",
  options = frequency
)

par2 = st.radio(
  "During the past 12 months, how often did your parents make you do chores around the house?",
  options = frequency
)

par3 = st.radio(
  "During the past 12 months, how often did your parents limit the amount of time you watched TV?",
  options = frequency
)

par4 = st.radio(
  "During the past 12 months, how often did your parents limit the amount of time you went out with friends on school nights?",
  options = frequency
)

st.subheader("Parental Interactions", divider="blue")

parint1 = st.radio(
  "During the past 12 months, how often did your parents let you know when you'd done a good job?",
  options = frequency
)

parint2 = st.radio(
  "During the past 12 months, how often did your parents tell you they were proud of you for something you had done?",
  options = frequency
)

parint3 = st.radio(
  "During the past 12 months, how many times have you argued or had a fight with at least one of your parents?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
)

st.subheader("Experiences", divider="green")

exp1 = st.radio(
  "During the past 12 months, how many times have you gotten into a serious fight at school or work?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
)

exp2 = st.radio(
  "During the past 12 months, how many times have you taken part in a fight where a group of your friends fought against another group?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
)

exp3 = st.radio(
  "During the past 12 months, how many times have you carried a handgun?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
)

exp4 = st.radio(
  "During the past 12 months, how many times have you sold illegal drugs?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
)

exp5 = st.radio(
  "During the past 12 months, how many times have you stolen or tried to steal anything worth more than $50?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
)

exp6 = st.radio(
  "During the past 12 months, how many times have you attacked someone with the intent to seriously hurt them?",
  options = ['0', '1 or 2', '3-5', '6-9','10 or more']
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
