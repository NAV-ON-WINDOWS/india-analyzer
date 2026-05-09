import streamlit as st
from mainclone import df, analyze

st.set_page_config(
    page_title="India Beyond Headlines",
    layout="centered",
)

st.markdown(
    """
    <div style="
        display: flex; 
        flex-direction: column; 
        align-items: center; 
        justify-content: center;
        width: 100%;
        line-height: 1.1;
    ">
        <h1 style="
            margin: 0; 
            padding: 0; 
            color: white; 
            font-size: 3.5rem;
        ">
            India Beyond Headlines
        </h1>
        <p style="
            margin: 5px 0 0 0; 
            padding: 0; 
            color: #E0E0E0; 
            font-size: 1.8rem; 
            font-weight: 300;
        ">
            3.8M Headlines Over 22 Years
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .centered-header {
        text-align: center;
    }

    [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
        font-size: 26px !important;
        font-weight: 600 !important;
        color: white !important;
        width: 100% !important; 
        margin-bottom: 0px !important;
    }

    div[data-testid="stTextInput"] {
        margin-top: 20px;
        margin-bottom: 5px;
    }

    /* Fixed sub-label styling */
    .sub-text {
        font-size: 16px !important;
        color: #AAAAAA !important;
        margin-top: -10px !important;
        margin-bottom: 20px !important;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                              url("https://i.pinimg.com/736x/30/da/f4/30daf4c4f81f907dc58d22c1bbc3464a.jpg");
            background-size: cover;
            background-attachment: fixed;
            backdrop-filter: blur(8px);           
            -webkit-backdrop-filter: blur(8px);
        }}
        </style>""",
        unsafe_allow_html=True,
    )

add_bg_from_url()

fact1 = st.text_input("Enter the factor you want to compare")
# Sub-label for Fact 1
st.markdown('<span class="sub-text">'
            'Example: Education, Cricket, Economy, Dollar</span>',
            unsafe_allow_html=True)

fact2 = st.text_input("Enter the factor you want to compare with")
# Sub-label for Fact 2
st.markdown('<span class="sub-text">'
            'Example: Employment, Football, Inflation, Rupee</span>',
            unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    analyzer = st.button("Analyze")

if analyzer:
    if not fact1 or not fact2:
        st.warning("Please enter both topics.")
    elif fact1.strip().lower() == fact2.strip().lower():
        st.warning("Please enter two different topics.")
    else:
        with st.spinner("Analyzing 3.8M headlines..."):
            fig, peak_fact1_val, peak_fact1_year, peak_fact2_value, peak_fact2_year = analyze(
                fact1.strip().lower(), fact2.strip().lower()
            )
            st.pyplot(fig)
            st.caption(
                f"📌 {fact1.title()} peaked at {peak_fact1_val} headlines in {peak_fact1_year}. "
                f"{fact2.title()} peaked at {peak_fact2_value} headlines in {peak_fact2_year}.")

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Total Headlines", "3,876,557")
col2.metric("Years Covered", "2001 – 2023")
col3.metric("Unique Categories", "1,024")

st.markdown("---")
st.markdown("<center>Built by Arnav Salgarkar &nbsp;|&nbsp; Data: Kaggle &nbsp;|&nbsp; https://github.com/NAV-ON-WINDOWS/india-analyzer</center>",
            unsafe_allow_html=True)