import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.mention import mention
import random
import base64
from data import exams
from data import feedback_messages
from data import blue_line
from data import space
from data import grey_line

number_q = 5
def generate_logo_tag():
    logo_url = "https://github.com/Rayan3rb/TestCastle/raw/main/logo.jpg"
    logo_tag = f"""
    <div style="display: flex; justify-content: center;">
        <img src="{logo_url}" width="240" height="329">
    </div>
    """
    return logo_tag

st.markdown(generate_logo_tag(), unsafe_allow_html=True)

def generate_moving_gif_tag():
    gif_url = "https://github.com/Rayan3rb/TestCastle/raw/main/animation_lo2h5zop_small.gif"
    gif_tag = f"""
    <style>
        @keyframes moveFromLeftToRight {{
            0% {{
                transform: translateX(-100%);
            }}
            100% {{
                transform: translateX(100%);
            }}
        }}

        .moving-gif {{
            animation: moveFromLeftToRight 2.5s linear infinite;
        }}
    </style>
    <div style="display: flex; justify-content: center; overflow: hidden;">
        <img class="moving-gif" src="{gif_url}" width="120" height="120">
    </div>
    """
    return gif_tag

st.markdown(generate_moving_gif_tag(), unsafe_allow_html=True)

st.markdown(blue_line, unsafe_allow_html=True)
st.markdown(space, unsafe_allow_html=True)

# Initialize session state if not already present
st.session_state.setdefault('selected_exam', list(exams.keys())[0])
st.session_state.setdefault('selected_topic', list(exams[st.session_state.selected_exam].keys())[0])
st.session_state.setdefault('selected_reading', list(exams[st.session_state.selected_exam][st.session_state.selected_topic].keys())[0])
st.session_state.setdefault('question_indices', [])
st.session_state.setdefault('user_answers', [])
st.session_state.setdefault('show_questions', False)
st.session_state.setdefault('show_score', False)

# Dropdowns for exam, topic, and reading
exam = st.selectbox('Choose the exam:', list(exams.keys()), index=list(exams.keys()).index(st.session_state.selected_exam))
st.session_state.selected_exam = exam
topic = st.selectbox('Choose the topic:', list(exams[exam].keys()), index=list(exams[exam].keys()).index(st.session_state.selected_topic))
if st.session_state.selected_topic != topic:  # If topic changes
    st.session_state.selected_topic = topic
    st.session_state.selected_reading = list(exams[exam][topic].keys())[0]  # Reset reading to first one for new topic
else:
    st.session_state.selected_topic = topic
reading = st.selectbox('Choose the reading:', list(exams[exam][topic].keys()), index=list(exams[exam][topic].keys()).index(st.session_state.selected_reading))
st.session_state.selected_reading = reading

# First submit button to confirm topic selection and display questions
if st.button("Submit"):
    st.session_state.show_questions = True
    st.session_state.show_score = False
    st.session_state.question_indices = random.sample(range(len(exams[exam][topic][reading]['questions'])), number_q)
    st.session_state.correct_answers = [exams[exam][topic][reading]['answers'][i] for i in st.session_state.question_indices]
    st.session_state.user_answers = []

# Welcoming Speech
    video_tag = f"""
    <div style="display: flex; justify-content: center;">
        <video controls width="320" height="240">
            <source src="https://github.com/Rayan3rb/TestCastle/raw/main/Welcome.mp4" type="video/mp4">
        </video>
    </div>
    """
    st.markdown(video_tag, unsafe_allow_html=True)
# Spaces
    st.markdown(space, unsafe_allow_html=True)
    st.markdown(space, unsafe_allow_html=True)    
    st.markdown(blue_line, unsafe_allow_html=True)
if st.session_state.show_questions:
    # Display the two questions and let the user answer
    for i, q_index in enumerate(st.session_state.question_indices):
        st.write(f"**{exams[exam][topic][reading]['questions'][q_index]}**")
        answer = st.radio(f"Answer for question {i+1}:", exams[exam][topic][reading]['choices'][q_index], key=f"question_{i}")
        if len(st.session_state.user_answers) < number_q:
            st.session_state.user_answers.append(answer)
        else:
            st.session_state.user_answers[i] = answer
    
    st.markdown(blue_line, unsafe_allow_html=True)

    if st.button("Submit Answers"):
        st.session_state.show_score = True
if st.session_state.show_score:
    score = sum([1 for user_ans, correct_ans in zip(st.session_state.user_answers, st.session_state.correct_answers) if user_ans[0] == correct_ans[0]]) 
    feedback = random.choice(feedback_messages[score])
    result = f"""
<style>
    /* Additional styles for centering */
    .center-container {{
        display: flex;
        justify-content: space-between;  /* change this to space-between for separation */
        align-items: center;
        height: 15vh;  /* takes the full height of the viewport */
    }}

    .score-display {{
        border: 2px solid #335575;
        padding: 10px 20px;
        border-radius: 8px;
        background-color: #ffffff;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        display: inline-flex;
        align-items: center;
        margin-right: 10px;  /* Added this line to create space */
    }}

    .score, .number_q {{
        font-size: 20px;
        font-weight: bold;
        color: #335575;
    }}

    .label {{
        margin: 0 10px;
    }}

    .feedback-text {{
        font-size: 20px;
        color: #335575;
        font-weight: bold;
    }}
</style>

<div class="center-container">
    <div class="score-display">
        <span class="score">{score}</span>
        <span class="label">/</span>
        <span class="number_q">{number_q}</span>
    </div>
    <div class="feedback-text">{feedback}</div>
</div>
"""
    st.markdown(result, unsafe_allow_html=True)
    
    if score == number_q:
        rain(
        emoji="🎈 🎊 ",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    total_questions = 0
    for reading, content in exams[exam][topic].items():
        total_questions += len(content["questions"])
    st.markdown(space, unsafe_allow_html=True)
    from streamlit_extras.buy_me_a_coffee import button
    button(username="rayan3rab7", floating=False, width=221)
    st.markdown(grey_line, unsafe_allow_html=True)
    cta = []
    if topic == "QUANTITATIVE METHODS":
        cta.append("https://rayanrab.gumroad.com/l/taxwc")
    elif topic == "Economics":
        cta.append("https://rayanrab.gumroad.com/l/llzeni")
    elif topic == "PORTFOLIO MANAGEMENT (PART ONE)":
        cta.append("https://rayanrab.gumroad.com/l/utniy")
    elif topic == "CORPORATE ISSUERS":
        cta.append("https://rayanrab.gumroad.com/l/pmlqg")
    elif topic == "FINANCIAL STATEMENT ANALYSIS":
        cta.append("https://rayanrab.gumroad.com/l/cckck")
    elif topic == "EQUITY INVESTMENTS":
        cta.append("https://rayanrab.gumroad.com/l/psjtg")
    elif topic == "FIXED INCOME":
        cta.append("https://rayanrab.gumroad.com/l/tgirr")
    elif topic == "DERIVATIVES":
        cta.append("https://rayanrab.gumroad.com/l/ibrrn")
    elif topic == "ETHICAL AND PROFESSIONAL STANDARDS":
        cta.append("https://rayanrab.gumroad.com/l/rnlkel")
    else:
        cta.append(" ")   
    st.markdown(f"""
<p style='color: #4A4A4A ; font-size: 16px;'>
Greetings! I noticed your interest in <strong>{topic}</strong> from <strong>{exam}</strong>. 
Dive deeper into this topic with our comprehensive manual solution, 
covering over <strong>{total_questions} multiple choice questions</strong>.
</p>
""", unsafe_allow_html=True)
    CTA = mention(
    label=f"Buy the manual solution of <strong>{topic}</strong>",
    icon="https://uploads-ssl.webflow.com/6336b5e34c850996471eb5e4/63463bf70877f116ba283efd_www.gumroad.png",
    url=cta[0],
    write=False,
    )            
    st.write(CTA,unsafe_allow_html=True)
with st.expander("Get the solution manual"):
    st.markdown("""
    <style>
    .custom-text {
        color: #4A4A4A ;
        font-size: 16px;
    }
    .custom-text a {
        text-decoration: none;
        color: #557AB1;  # A blue color to make the links stand out
    }
    </style>
    <style>
    .custom-text {
        display: flex;
        align-items: center; /* Vertically center the content */
    }

    .custom-text img {
        margin-right: 20px; /* Add some space between the image and the text */
    }
    </style>

    <div class="custom-text">
        <img src="https://uploads-ssl.webflow.com/6336b5e34c850996471eb5e4/63463bf70877f116ba283efd_www.gumroad.png" alt="Gumroad Image" width="50" height="50">
        Buy the solution manual for any topic with only $10
    </div>
        <a href="https://rayanrab.gumroad.com/l/taxwc" target="_blank">CFA I: QUANTITATIVE METHODS (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/llzeni" target="_blank">CFA I: Economics (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/utniy" target="_blank">CFA I: PORTFOLIO MANAGEMENT (PART ONE) (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/pmlqg" target="_blank">CFA I: CORPORATE ISSUERS (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/cckck" target="_blank">CFA I: FINANCIAL STATEMENT ANALYSIS (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/psjtg" target="_blank">CFA I: EQUITY INVESTMENTS (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/tgirr" target="_blank">CFA I: FIXED INCOME (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/ibrrn" target="_blank">CFA I: DERIVATIVES (Solution & Reference)</a><br>
        <a href="https://rayanrab.gumroad.com/l/rnlkel" target="_blank">CFA I: ETHICAL AND PROFESSIONAL STANDARDS (Solution & Reference)</a><br>    
    </div>
    """, unsafe_allow_html=True)