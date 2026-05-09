import streamlit as st

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

    /* This targets the label container AND the paragraph tag specifically */
    [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
        font-size: 26px !important;
        font-weight: 600 !important;
        color: white !important;
        width: 100% !important; 
    }

    div[data-testid="stTextInput"] {
        margin-top: 20px;
        margin-bottom: 20px;
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

fact1 = st.text_input("Enter the factor you want compare")
fact2 = st.text_input("Enter the factor you want compare with")
