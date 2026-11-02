import streamlit as st
from numpy import random

def cloze(filename):
    with open (filename, "r", encoding="utf-8") as f:
        f = f.read()
        int = random.randint(len(f.splitlines()))
        counter = 0
        question = f.splitlines()[int]
        index = question.find("~")
        index2 = question.find("#")
        st.header(question[:index])
        st.write(question[index+1:index2])
        ans = st.text_input("Enter the missing word:")
        if ans:
            if ans.lower() == question[index2+1:].lower():
                st.success("Correct")
            else:
                st.error("Incorrect")
        st.button("Next")