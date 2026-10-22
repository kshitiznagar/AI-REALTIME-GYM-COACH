
import streamlit as st


EXERCISE_METRICS = {
    # Chest
    "Bench Press": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Incline Bench Press": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Decline Bench Press": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Dumbbell Bench Press": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Chest Fly": [
        "elbow_angle", "shoulder_angle", "arm_angle"
    ],
    "Cable Crossover": [
        "elbow_angle", "shoulder_angle", "arm_angle"
    ],
    "Push-ups": [
        "elbow_angle", "body_angle", "hip_angle", "body_alignment"
    ],

    # Back
    "Lat Pulldown": [
        "elbow_angle", "shoulder_angle", "torso_angle"
    ],
    "Pull-ups": [
        "elbow_angle", "shoulder_angle", "torso_angle"
    ],
    "Seated Cable Row": [
        "elbow_angle", "shoulder_angle", "back_angle"
    ],
    "Barbell Row": [
        "elbow_angle", "shoulder_angle", "back_angle"
    ],
    "T-Bar Row": [
        "elbow_angle", "shoulder_angle", "back_angle"
    ],
    "Dumbbell Row": [
        "elbow_angle", "shoulder_angle", "back_angle"
    ],
    "Deadlift": [
        "hip_angle", "knee_angle", "back_angle", "torso_angle"
    ],

    # Biceps
    "Bicep Curl": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Hammer Curl": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Preacher Curl": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Concentration Curl": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],

    # Triceps
    "Tricep Pushdown": [
        "elbow_angle", "shoulder_angle", "extension_status"
    ],
    "Tricep Dips": [
        "elbow_angle", "shoulder_angle", "body_alignment"
    ],
    "Skull Crushers": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],
    "Overhead Tricep Extension": [
        "elbow_angle", "shoulder_angle", "wrist_angle"
    ],

    # Shoulders
    "Shoulder Press": [
        "elbow_angle", "shoulder_angle", "arm_angle"
    ],
    "Dumbbell Shoulder Press": [
        "elbow_angle", "shoulder_angle", "arm_angle"
    ],
    "Arnold Press": [
        "elbow_angle", "shoulder_angle", "arm_angle"
    ],
    "Lateral Raises": [
        "shoulder_angle", "elbow_angle", "arm_angle"
    ],
    "Front Raises": [
        "shoulder_angle", "elbow_angle", "arm_angle"
    ],
    "Reverse Fly": [
        "shoulder_angle", "elbow_angle", "arm_angle"
    ],

    # Legs
    "Barbell Squat": [
        "knee_angle", "hip_angle", "back_angle", "depth_status"
    ],
    "Goblet Squat": [
        "knee_angle", "hip_angle", "torso_angle", "depth_status"
    ],
    "Leg Press": [
        "knee_angle", "hip_angle", "ankle_angle", "depth_status"
    ],
    "Leg Extension": [
        "knee_angle", "hip_angle", "extension_status"
    ],
    "Leg Curl": [
        "knee_angle", "hip_angle", "extension_status"
    ],
    "Romanian Deadlift": [
        "hip_angle", "knee_angle", "back_angle", "torso_angle"
    ],
    "Lunges": [
        "front_knee_angle", "rear_knee_angle",
        "hip_angle", "balance_status"
    ],
    "Calf Raises": [
        "ankle_angle", "knee_angle", "balance_status"
    ],
    "Hip Thrust": [
        "hip_angle", "knee_angle", "hip_status"
    ],
    "Glute Bridge": [
        "hip_angle", "knee_angle", "hip_status"
    ],

    # Core
    "Cable Crunch": [
        "torso_angle", "hip_angle", "neck_angle"
    ],
    "Abdominal Crunch": [
        "torso_angle", "hip_angle", "neck_angle"
    ],
    "Hanging Leg Raise": [
        "hip_angle", "knee_angle", "swing_status"
    ],
    "Plank": [
        "body_angle", "hip_angle", "body_alignment"
    ],
    "Russian Twist": [
        "torso_angle", "shoulder_angle", "hip_angle"
    ],
    "Back Extension": [
        "back_angle", "hip_angle", "back_arch_status"
    ],

    # Cardio
    "Treadmill Running": [
        "knee_angle", "hip_angle", "ankle_angle", "torso_angle"
    ],
    "Incline Walking": [
        "knee_angle", "hip_angle", "ankle_angle", "torso_angle"
    ],
    "Stationary Cycling": [
        "knee_angle", "hip_angle", "ankle_angle"
    ],
    "Elliptical Training": [
        "knee_angle", "hip_angle", "elbow_angle"
    ],
    "Rowing Machine": [
        "knee_angle", "hip_angle", "elbow_angle", "back_angle"
    ],
    "Stair Climber": [
        "knee_angle", "hip_angle", "ankle_angle", "torso_angle"
    ],
}


def show_exercise_metrics(exercise):
    metrics = EXERCISE_METRICS.get(exercise)

    if not metrics:
        st.info("No metrics configured for this exercise.")
        return

    st.subheader(f"{exercise} Metrics")

    # Display three metrics per row
    for start in range(0, len(metrics), 1):
        row_metrics = metrics[start:start + 1]
        columns = st.columns(len(row_metrics))

        for column, key in zip(columns, row_metrics):
            value = st.session_state.get(key, "N/A")
            label = key.replace("_", " ").title()

            if key.endswith("_angle"):
                if isinstance(value, (int, float)):
                    value = f"{value:.1f}°"
                else:
                    value = str(value)

            with column:
                st.metric(label=label, value=value, width="stretch")
