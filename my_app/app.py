
import streamlit as st

st.markdown("""
<style>
/* Limit main page width to 80% */
.stMainBlockContainer {
    max-width: 80%;
    margin-left: auto;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Juno Thiensirisak",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Home page
home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="",
    default=True
)

# Academic pages
academic_pages = [
    st.Page(
        "pages/academic/academic.py",
        title="Educational History",
        icon=""
    ),
    st.Page(
        "pages/academic/mrp.py",
        title="Major Research Paper",
        icon=""
    ),
    st.Page(
        "pages/academic/research_assistantship.py",
        title="Research Assistantship",
        icon=""
    ),
    st.Page(
        "pages/academic/lions_risk.py",
        title="LiON's Risk",
        icon=""
    ),
]

# Portfolio pages
portfolio_pages = [
    st.Page(
        "pages/portfolio/cultural_dimensions.py",
        title="Hofstede’s Cultural Dimensions",
        icon=""
    )
]

# Navigation
pg = st.navigation({
    "": [home_page],
    "Academic": academic_pages,
    "Portfolio": portfolio_pages
})

pg.run()