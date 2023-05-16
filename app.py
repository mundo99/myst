import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x*x)

st.title("하이하이")
st.markdown("hihi")
st.code("x=2021")
st.latex(r'''
  a + a r ^1+ a r^2 + r^3 ''')
