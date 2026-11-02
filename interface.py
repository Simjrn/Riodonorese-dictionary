import streamlit as st

st.header(":rainbow[The internet's best way to learn Riodonorese!]")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dictionary", 'Text', 'Pronunciation and writing', 'Course', 'Roadmap'])

with tab1:
  query = st.text_input("", type="search", placeholder="Search dictionary entries", live="0ms")
  counter = 0
  if query:
    st.write(f"**Dictionary entries containing ':blue[{query}]'**:")
    with open ("dictionary.txt") as dict:
      for line in dict:
        if query.lower() in line.lower():
          container = st.container(border=True, key=str(counter))
          index = line.find("/")
          index2 = line.find("#")
          if not index2 == -1:
            container.write(f"**{line[:index]}** = {line[index+1:index2]} :green[-> {line[index2+1:]}]")
          else:
            container.write(f"**{line[:index]}** = {line[index+1:index2]}")
        counter = counter + 1

with tab2:
  with open("text.txt", "r", encoding = "utf-8") as txt:
    text = txt.read()
    st.audio("text.mp3", format="audio/mp3")
    st.write(text)

with tab3:
  with open("pronunciation.md","r" ,encoding="utf-8") as md:
    md = md.read()
    st.markdown(md)

with tab4:
  with st.expander("Lesson 1"):
    with open("course/L1.md","r" ,encoding="utf-8") as md:
      md = md.read()
      st.markdown(md)

with tab5:
  with open("roadmap.md","r" ,encoding="utf-8") as md:
    md = md.read()
    st.markdown(md)