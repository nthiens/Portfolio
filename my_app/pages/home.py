import streamlit as st
import time
import pydeck as pdk
import pandas as pd

# Reserve title position at the top
title_placeholder = st.empty()

# Everything else appears

st.markdown(
    """
    <div style="text-align: left; font-size: 25px; font-weight: 600;">
        <span style="color: #A78BFA;">Geospatial Analytics</span>
        <span style="color: #666666;">- </span>
        <span style="color: #60A5FA;">Data Science</span>
        <span style="color: #666666;"> - </span>
        <span style="color: #5DB6A4;">Machine Learning</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("Beyond Traditional Analytics")
st.write("I integrate GIS and spatial analysis with advanced data analytics and machine learning to uncover deeper insights, identify hidden patterns, and reveal geographic relationships often overlooked by traditional analytical approaches. I excel at translating complex analytical findings into clear, accessible insights for both technical and non technical audiences through interactive maps, presentations, and dashboards. I'll help you make data-driven, informed decisions.")

st.subheader("Some of my skills")
st.markdown("""
- **Python**
    - Pandas, Numpy, Scikit-learn, PyTorch, PySpark
- **Spatial Analysis**
    - ArcGIS Pro, ArcGIS Online, ArcGIS StoryMaps
- **Machine Learning**
    - Traditional Machine Learning, Deep Learning
""")

st.subheader("Cool things I've worked on")
import streamlit as st

st.markdown("""
<style>
.project-card {
    border: 1px solid #444;
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
    margin-top: -30px;
}
.project-card:hover {
    transform: translateY(-4px);
}
.project-card img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    display: block;
}
.project-info {
    padding: 15px;
}
.project-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 5px;
}
.project-description {
    font-size: 13px;
    color: #999;
}
</style>
""", unsafe_allow_html=True)

# Project card function
def project_card(title, description, image, link):
    st.markdown(f"""
    <a href="{link}" target="_blank"
       style="text-decoration:none; color:inherit;">
        <div class="project-card">
            <img src="{image}">
            <div class="project-info">
                <div class="project-title">{title}</div>
                <div class="project-description">{description}</div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Row 2
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    project_card(
        "UFC Fight Prediction",
        "Machine learning and predictive analytics",
        "https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/51fe71a3-cb12-4ac2-882f-45955401dd53/Golden+Retrievers+dans+pet+care.jpeg",
        "https://github.com/nthiens/UFCData"
    )

with col2:
    project_card(
        "Geospatial Analysis",
        "GIS and spatial modelling",
        "https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/51fe71a3-cb12-4ac2-882f-45955401dd53/Golden+Retrievers+dans+pet+care.jpeg",
        "https://github.com/"
    )

with col3:
    project_card(
        "Sports Analytics",
        "Athlete performance analysis",
        "https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/51fe71a3-cb12-4ac2-882f-45955401dd53/Golden+Retrievers+dans+pet+care.jpeg",
        "https://github.com/"
    )

st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# Row 1
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    project_card(
        "UFC Fight Prediction",
        "Machine learning and predictive analytics",
        "https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/51fe71a3-cb12-4ac2-882f-45955401dd53/Golden+Retrievers+dans+pet+care.jpeg",
        "https://github.com/nthiens/UFCData"
    )

with col2:
    project_card(
        "Geospatial Analysis",
        "GIS and spatial modelling",
        "https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/51fe71a3-cb12-4ac2-882f-45955401dd53/Golden+Retrievers+dans+pet+care.jpeg",
        "https://github.com/"
    )

with col3:
    project_card(
        "Sports Analytics",
        "Athlete performance analysis",
        "https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/51fe71a3-cb12-4ac2-882f-45955401dd53/Golden+Retrievers+dans+pet+care.jpeg",
        "https://github.com/"
    )


st.subheader("Connect with me!")

st.markdown("""
<div style="
    background-color: #f0f0f0;
    border-radius: 12px;
    padding: 15px;
    max-width: 280px;
">
    <h4 style="margin: 0 0 8px 0; font-size: 18px;">
        Juno Thiensirisak
    </h4>
    <a href="mailto:junothiensirisak@gmail.com"
       style="font-size: 14px; text-decoration: none; color: inherit;">
        📩 junothiensirisak@gmail.com
    </a>
    <br>
    <a href="https://linkedin.com/in/n2thiens"
       style="font-size: 14px; text-decoration: none; color: inherit;">
        💼 linkedin.com/in/n2thiens
    </a>
    <br>
    <a href="https://github.com/nthiens"
       style="font-size: 14px; text-decoration: none; color: inherit;">
        💻 github.com/nthiens
    </a>
</div>
""", unsafe_allow_html=True)


# Animate title at the top, after everything else has appeared
text = "Hi there! I'm Juno..."
typed_text = ""

for char in text:
    typed_text += char

    title_placeholder.markdown(
        f"""
        <style>
        @keyframes blink {{
            50% {{ opacity: 0; }}
        }}
        .cursor {{
            animation: blink 1.4s step-end infinite;
        }}
        </style>

        <h1 style="margin: 0; white-space: nowrap;">
            {typed_text}<span class="cursor">|</span>
        </h1>
        """,
        unsafe_allow_html=True
    )

    time.sleep(0.04)



