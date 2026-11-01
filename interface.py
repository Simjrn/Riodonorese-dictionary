import streamlit as st

query = st.text_input("Search:")

with open ("dictionary.txt") as dict:
  for line in dict:
    if query in line:
      st.write(line)
