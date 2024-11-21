
import streamlit as st
from datetime import datetime
import time
import random
import pandas as pd
from streamlit_webrtc import webrtc_streamer

# Global Variables
is_workout_active = False
calories = 0.0
seconds = 0
poses = [
    "Exercise detected",
    "Exercise not detected",
    "Pose detected",
    "Pose not detected",
    "Yoga detected",
    "Yoga not detected",
    "None"
]
workout_history = []

# Format time as HH:MM:SS
def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Simulate Pose Detection
def simulate_pose_detection():
    detected_pose = random.choice(poses)
    accuracy = random.randint(80, 100)
    return detected_pose, accuracy

# UI Setup
st.set_page_config(page_title="FitFusion - AI Workout & Pose Detection", layout="wide")

# Sidebar
st.sidebar.title("FitFusion")
st.sidebar.markdown("AI-Powered Workout and Pose Detection App")

# Main App
st.title("FitFusion - AI Workout & Pose Detection")
st.markdown("### Live Workout Feed")
placeholder = st.empty()

# Webcam Feed
st.markdown("#### Webcam Feed (Simulated)")
webrtc_streamer(key="webcam")

# Start/Stop Button
if "is_workout_active" not in st.session_state:
    st.session_state.is_workout_active = False

col1, col2 = st.columns(2)
with col1:
    if st.session_state.is_workout_active:
        if st.button("Stop Workout", key="stop"):
            st.session_state.is_workout_active = False
    else:
        if st.button("Start Workout", key="start"):
            st.session_state.is_workout_active = True

# Timer and Stats
if st.session_state.is_workout_active:
    start_time = time.time()
    detected_pose, accuracy = simulate_pose_detection()
    with st.container():
        st.markdown("### Current Workout Stats")
        st.markdown(f"**Detected Pose:** {detected_pose}")
        st.markdown(f"**Accuracy:** {accuracy}%")
        st.markdown(f"**Calories Burned:** {calories}")
        elapsed_time = time.time() - start_time
        st.markdown(f"**Time Elapsed:** {format_time(int(elapsed_time))}")

# History Table
st.markdown("### Workout History")
history_df = pd.DataFrame(
    workout_history, columns=["Date", "Calories Burned", "Duration"]
)
st.dataframe(history_df)
