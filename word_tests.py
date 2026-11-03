import streamlit as st
from numpy import random

@st.fragment
def word_tests(filename):
    with open (filename, "r", encoding="utf-8") as f:
        f = f.read()
        int = random.randint(len(f.splitlines()))
        counter = 0
        question = f.splitlines()[int]
        index = question.find("/")
        st.header(question[index+1:])
        @st.fragment
        def get_answer(question):
            answer = st.text_input("Input your answer: ", key=question)
            submit_button = st.button(label='Submit')
            if submit_button:
                if answer.lower() == question[:index].lower():
                    st.success("Correct")
                else:
                    st.error(f"No, the correct answer was '{question[index2+1]}'") 
        get_answer(question)  
        st.button("Next")
