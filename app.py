import streamlit as st
import pandas as pd
import joblib
import base64

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Drive Beyond", layout="wide")

# -----------------------------
# Load Models
# -----------------------------
cost_model = joblib.load("models/cost_model.pkl")
time_model = joblib.load("models/time_model.pkl")
efficiency_map = joblib.load("models/vehicle_efficiency.pkl")

battery_capacity = {
    "Tesla Model 3": 60,
    "Nissan Leaf": 40,
    "Hyundai Kona": 64
}

# -----------------------------
# Background Image
# -----------------------------
def set_bg(image):
    with open(image, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("assets/bg.jpg")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

st.sidebar.header("User Inputs")

/* EV Details Panel */
.ev-panel {
    background: rgba(60, 60, 60, 0.75);
    padding: 28px;
    border-radius: 18px;
    color: #ffffff;
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
}

.ev-heading {
    font-size: 22px;
    font-weight: 50;
    color: #ffffff;
    margin-bottom: 1px;
    letter-spacing: 0.5px;
}

/* Header Widget */
.header-box {
    background: rgba(60, 60, 60, 0.75);
    padding: 26px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 40px;
}

/* Drive Beyond Title */
.header-title {
    font-size: 48px;
    font-weight: 900;
    color: #b6ff00; /* neon yellow-green */
    letter-spacing: 2px;
}

/* Subtitle */
.header-sub {
    font-size: 16px;
    color: #eeeeee;
}

/* Section Titles */
.section-title {
    color:#ffffff;
    font-size: 30px;
    font-weight: 900;
    margin-bottom: 15px;
}

/* Big Lavender Buttons */
.big-btn > button {
    background: #c6b7ff ;
    color: #1e1e1e ;
    font-size: 20px ;
    padding: 18px 10px;
    border-radius: 30px ;
    font-weight: 700 ;
    width: 100%;
    border: none;
    margin-top: 10px;
}

/* Button hover */
.big-btn > button:hover {
    background: #b1a1ff;
}

/* Output Box */
.output-box {
    background: rgba(0,0,0,0.75);
    padding: 28px;
    border-radius: 18px;
    margin-top: 40px;
    color: white;
    font-size: 24px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

left, main = st.columns([1.2, 3], gap="large")

# -----------------------------
# LEFT – EV DETAILS PANEL
# -----------------------------
with left:
    st.markdown("<div class='ev-panel'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'> Enter EV Details</div>", unsafe_allow_html=True)

    st.markdown(
    "<div class='ev-heading'>Vehicle Model</div>",
    unsafe_allow_html=True)
    vehicle = st.selectbox("Vehicle Model", battery_capacity.keys())
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
    "<div class='ev-heading'>Charger Type</div>",
    unsafe_allow_html=True)
    charger = st.selectbox("Charger Type", ["Level 1", "Level 2", "DC Fast"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
    "<div class='ev-heading'>User Type</div>",
    unsafe_allow_html=True)
    user = st.selectbox("User Type", ["Residential", "Commercial", "Fleet"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
    "<div class='ev-heading'>State of Charge</div>",
    unsafe_allow_html=True)
    soc = st.number_input("Current State of Charge (%)", 1, 99, 30)
    st.markdown("</div>", unsafe_allow_html=True)
    

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# MAIN AREA
# -----------------------------
with main:
    st.markdown("""
    <div class='header-box'>
        <div class='header-title'>DRIVE BEYOND</div>
        <div class='header-sub'>Smarter EV Charging & Range Prediction</div>
    </div>
    """, unsafe_allow_html=True)

    # Button row (spaced & centered)
    b1, b2, b3 = st.columns([1.2, 1.2, 1.2], gap="large")

    battery = battery_capacity[vehicle]
    energy_needed = battery * (100 - soc) / 100
    available_energy = battery * soc / 100

    if "result" not in st.session_state:
        st.session_state.result = None

    with b1:
        st.markdown("<div class='big-btn'>", unsafe_allow_html=True)
        if st.button("Estimated cost to fully charge"):
            X = pd.DataFrame([{
                "Energy_Needed": energy_needed,
                "Vehicle Model": vehicle,
                "Charger Type": charger,
                "User Type": user
            }])
            value = cost_model.predict(X)[0]
            st.session_state.result = f"Estimated Charging Cost: ${value:.2f}"
        st.markdown("</div>", unsafe_allow_html=True)

    with b2:
        st.markdown("<div class='big-btn'>", unsafe_allow_html=True)
        if st.button("Time required to fully charge"):
            X = pd.DataFrame([{
                "Energy_Needed": energy_needed,
                "Vehicle Model": vehicle,
                "Charger Type": charger,
                "User Type": user
            }])
            value = time_model.predict(X)[0]
            st.session_state.result = f"Charging Time Required: {value:.2f} hours"
        st.markdown("</div>", unsafe_allow_html=True)

    with b3:
        st.markdown("<div class='big-btn'>", unsafe_allow_html=True)
        if st.button("Distance it can cover"):
            efficiency = efficiency_map[vehicle]
            value = available_energy * efficiency
            st.session_state.result = f"Estimated Driving Distance: {value:.1f} km"
        st.markdown("</div>", unsafe_allow_html=True)

    # Output (only when clicked)
    if st.session_state.result:
        st.markdown(
            f"<div class='output-box'>{st.session_state.result}</div>",
            unsafe_allow_html=True
        )

