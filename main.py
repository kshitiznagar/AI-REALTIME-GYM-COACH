import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS
from services.config.exercise_metrics import show_exercise_metrics
from services.ui.style_loader import load_css, inject_local_font
from services.persistence.exercise_repository import init_db
from streamlit_webrtc import webrtc_streamer, WebRtcMode
import os
def main():
    st.set_page_config(
        page_icon="🏋️‍♀️",
        page_title="AI Real-time Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered"
    )
    
    load_css(os.path.join(os.getcwd(), "static", "style.css"))
    inject_local_font(os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean")
    
    init_db()
    
    if not render_login_wall():
        return
    
    initial_session_defaults()

    
    workout_started = st.session_state.get("workout_started", False)
    
    with st.sidebar:
        st.title("🏋️‍♀️ AI Coach")
        
        if st.session_state.username:
            st.caption(f"👤 Logged in as {st.session_state.username}")

        st.divider()
        st.subheader("Workout plan")
        if not workout_started:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")
            st.number_input("Sets", min_value=1, max_value=10, key="plan_sets", step=1)
            st.number_input("Reps", min_value=0, max_value=50, key="plan_reps", step=1)
            
            st.markdown("")
            
            start_session_button = st.button("Start workout", width="stretch", key="start_session_button")
            if start_session_button:
                st.session_state["workout_started"] = True
                st.rerun()
        else:
            exercise = st.session_state.get("plan_exercise")
            sets = st.session_state.get("plan_sets")
            reps = st.session_state.get("plan_reps")
            st.info(f"**{exercise}** -- {sets} Sets x {reps} Reps")
            end_session_button = st.button("End workout", key="end_session_button", width="stretch")
            
            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()
        
        if workout_started:
            st.divider()
            
            
            exercise = st.session_state.get("plan_exercise")
            total_reps = st.session_state.get("reps")
            current_set_reps = st.session_state.get("current_set_reps")
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets = st.session_state.get("plan_sets")
            
            
            st.subheader("Progress")

            st.metric("Total Reps", f"{total_reps}")
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")
            
            st.divider()
            
            
            show_exercise_metrics(exercise)

    
    st.title("AI Real-time GYM Coach")
    st.markdown("#### Real-time pose detection with proactive AI voice coaching")
    
    
    if not workout_started:
        st.markdown(
            """
            <div style="
                border: 10px dashed #444;
                border-radius: 0px;
                padding: 48px 32px;
                text-align: center;
                color: #888;
                margin-top: 32px;
                margin-bottom: 32px;
            ">
                <h2 style="color:#ccc; margin-bottom:8px;">👈 Set your workout plan</h2>
                <p style="font-size:1.05rem;">
                    Choose your exercise, sets and reps in the sidebar,<br>
                    then click <strong>Start Workout</strong> to activate the camera and AI coach.
                </p>
            </div>
            """,
            unsafe_allow_html=True
    )
    
    else:
        context = webrtc_streamer(
            key = "exercise-analysis",
            mode = WebRtcMode.SENDRECV,
            video_processor_factory=None,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
            media_stream_constraints={
                "video" : True,
                "audio" : False
            },
            async_processing=True
        )
    
    st.divider()
    
    st.markdown("#### Workout history")
    
    
    
if __name__ == "__main__":
    main()