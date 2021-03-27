import streamlit as st
from  datetime import datetime

st.title("Thoughts Dashboard")

author = st.text_input("Autor:in:")
txt = st.text_area("Seg mir dini gedanke:")
dt = datetime.now().strftime("%c")
st.markdown(author + " " + dt)
st.markdown(txt)
st.button("Zur ablag")