import streamlit as st

st.title("My Streamlit App")

col1, col2 = st.columns(2)

with col1:
  st.header("Column 1")
  st.write("Hello")

with col2:
  st.header("Column 2")
  st.write("World")

with st.expander("Expand for more information"):
  st.write("Here you can put in some really explanatory things.")
