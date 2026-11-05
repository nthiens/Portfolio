import streamlit as st

st.title("Educational History")
st.markdown("""
<p style="font-size: 1.75rem; font-weight: 600; margin: 0;">
    University of Waterloo (2025)
</p>
""", unsafe_allow_html=True)
st.markdown("""
<p style="font-size: 18px; font-weight: 500; margin: 0;">
    BMath Major in Mathematical Studies, Minor in Computing
</p>
""", unsafe_allow_html=True)
st.write("Graduated with distinction. This is where I learned statistical fundamentals, programming, and machine learning.")


st.markdown("""
<p style="font-size: 1.75rem; font-weight: 600; margin: 0;">
    Toronto Metropolitan University (2027)
</p>
""", unsafe_allow_html=True)
st.markdown("""
<p style="font-size: 18px; font-weight: 500; margin: 0;">
    MSA Master of Spatial Analysis
</p>
""", unsafe_allow_html=True)
st.write("I am continually adding more geospatial skills, software, and technologies to my toolbelt.")

st.subheader("Here's a map of where I went to school")

st.image("https://i.imgur.com/qbT6ihp.png", width=400)