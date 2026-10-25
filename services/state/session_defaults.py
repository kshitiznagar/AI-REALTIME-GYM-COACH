import streamlit as st


def initial_session_defaults():
    defaults = {
        "reps": 0,
        "target_sets": 0,
        "reps_per_set": 0,
        "sets_completed": 0,
        "current_set_reps": 0,
        "workout_complete": False,
        "last_notified_sets_completed": 0,
        "last_notified_workout_complete": False,
        "last_saved_sets_completed": 0,
        "set_cycle_started_at": 0.0,
        "last_exercise_type": "Barbell Squat",

        # Workout plan (set before starting)
        "workout_started": False,
        "plan_exercise": "Barbell Squat",
        "plan_sets": 3,
        "plan_reps": 10,

        # Common Angles
        "knee_angle": 0,
        "back_angle": 0,
        "elbow_angle": 0,
        "front_knee_angle": 0,
        "rear_knee_angle": 0,
        "hip_angle": 0,
        "shoulder_angle": 0,
        "left_shoulder_angle": 0,
        "right_shoulder_angle": 0,
        "left_elbow_angle": 0,
        "right_elbow_angle": 0,
        "left_knee_angle": 0,
        "right_knee_angle": 0,
        "ankle_angle": 0,
        "left_ankle_angle": 0,
        "right_ankle_angle": 0,
        "wrist_angle": 0,
        "neck_angle": 0,
        "torso_angle": 0,
        "spine_angle": 0,
        "body_angle": 0,
        "hip_extension_angle": 0,
        "hip_flexion_angle": 0,
        "arm_angle": 0,
        "upper_arm_angle": 0,
        "forearm_angle": 0,
        "leg_angle": 0,

        # Status fields
        "depth_status": "N/A",
        "body_alignment": "N/A",
        "hip_status": "N/A",
        "shoulder_status": "N/A",
        "swing_status": "N/A",
        "extension_status": "N/A",
        "back_arch_status": "N/A",
        "balance_status": "N/A",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value