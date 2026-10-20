import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults

def main():
    st.set_page_config(
        page_icon="🏋️‍♀️",
        page_title="AI Real-time Gym Coach",
        initial_sidebar_state="expanded",
        layout="centered"
    )
    
    if not render_login_wall():
        return
    
    initial_session_defaults()
    
    
    with st.sidebar:
        st.title("🏋️‍♀️ AI Coach")
        
        if st.session_state.username:
            st.caption(f"👤 Logged in as {st.session_state.username}")

        st.divider()
    
    st.write("Hello")
    
if __name__ == "__main__":
    main()