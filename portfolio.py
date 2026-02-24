import streamlit as st
import base64

st.set_page_config(page_title="Vishvashwarran | Portfolio", layout="wide")

# ---------- GLOBAL STYLING ----------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

/* remove extra space under headings */
h1, h2, h3, h4 {
    margin-bottom: 0.3rem;
}

/* glass card */
.glass {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,0,0,0.25);
    margin-bottom: 20px;
}

/* center text */
.center {
    text-align: center;
}

/* badge */
.badge {
    background-color: #00FFD1;
    color: black;
    padding: 6px 12px;
    border-radius: 20px;
    margin: 3px;
    display: inline-block;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("<h1 class='center'>Vishvashwarran V B</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='center'>Aspiring Data Scientist | ML • DL • GenAI</h4>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    st.markdown("""
    <div class="glass" style="display:flex; justify-content:center; padding:15px;">
        <img src="data:image/jpg;base64,{}" width="200"
        style="border-radius:12px; box-shadow:0 0 20px rgba(0,255,209,0.35);">
    </div>
    """.format(
        base64.b64encode(open("profile.jpg", "rb").read()).decode()
    ), unsafe_allow_html=True)

st.markdown("""
<p class='center'>
<a href="mailto:vellorevishva@gmail.com">📧 Email</a> |
<a href="tel:+918825785420">📞 Call</a> |
<a href="https://www.linkedin.com/in/vishvashwarranvb">LinkedIn</a> |
<a href="https://github.com/Vishvashwarran">GitHub</a>
</p>
""", unsafe_allow_html=True)

with open("resume.pdf", "rb") as file:
    st.download_button("📄 Download Resume", file, "Vishvashwarran_Resume.pdf")

st.divider()

# ---------- ABOUT ----------
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.header("About Me")

st.write("""
Aspiring Data Scientist with hands-on experience in Machine Learning, Deep Learning, and
LLM-based applications. Skilled in building end-to-end intelligent systems using Python,
Streamlit, and MySQL for real-time analytics in smart city and healthcare domains.
""")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ---------- SKILLS ----------
st.header("Technical Skills")

skills = [
    "Python", "Machine Learning", "Deep Learning",
    "MySQL", "Streamlit", "LLM & RAG",
    "Scikit-learn", "Pandas", "NumPy"
]

cols = st.columns(3)

for i, skill in enumerate(skills):
    cols[i % 3].markdown(f"<div class='glass center'>{skill}</div>", unsafe_allow_html=True)

st.divider()

# ---------- PROJECTS ----------
st.header("Projects")

col1, col2 = st.columns(2)

# SMART CITY
with col1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("Smart City Analytics System")
    st.caption("AI • Machine Learning • Deep Learning • LLM • Real-Time Analytics")

    st.markdown("""
• Developed an end-to-end Smart City Analytics platform for real-time urban data monitoring  
• Implemented ML & DL models for traffic, AQI, pothole, overcrowding & complaints  
• Built interactive Streamlit dashboard for live insights  
• Integrated MySQL for real-time data operations  
• Implemented LLM-powered RAG for intelligent query handling  
""")

    st.markdown("#### Tech Stack")
    st.markdown("""
<span class='badge'>Python</span>
<span class='badge'>Streamlit</span>
<span class='badge'>MySQL</span>
<span class='badge'>Machine Learning</span>
<span class='badge'>Deep Learning</span>
<span class='badge'>LLM</span>
<span class='badge'>RAG</span>
""", unsafe_allow_html=True)

    st.link_button("💻 GitHub Repo", "https://github.com/Vishvashwarran/UrbanBot-SmartCity-Analytics")

    st.markdown("**Impact:** Real-time urban intelligence & smart decision support")

    st.markdown("</div>", unsafe_allow_html=True)

# DISEASE
with col2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("Multiple Disease Prediction System")
    st.caption("Machine Learning • Healthcare Analytics • Streamlit App")

    st.markdown("""
• Built ML system for Parkinson’s, kidney & liver disease prediction  
• Performed preprocessing, encoding & feature scaling  
• Trained Logistic Regression, Random Forest & XGBoost  
• Evaluated using F1-score, ROC-AUC & confusion matrix  
• Developed Streamlit app for real-time prediction  
""")

    st.markdown("#### Tech Stack")
    st.markdown("""
<span class='badge'>Python</span>
<span class='badge'>Scikit-learn</span>
<span class='badge'>Pandas</span>
<span class='badge'>NumPy</span>
<span class='badge'>Streamlit</span>
""", unsafe_allow_html=True)

    st.link_button("💻 GitHub Repo", "https://github.com/Vishvashwarran/Multiple-Disease-Prediction")

    st.markdown("**Impact:** ML-based early disease risk detection")

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ---------- CERTIFICATIONS ----------
st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.header("Certifications")

st.write("Master Data Science Program – GUVI (IITM Pravartak incubated)")
st.caption("Machine Learning • Deep Learning • Data Analytics • End-to-End Projects")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ---------- FOOTER ----------
st.markdown("<p class='center'>© 2026 Vishvashwarran V B | Data Science Portfolio</p>", unsafe_allow_html=True)