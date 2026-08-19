import os
from typing import Optional
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
def generate_workout_plan(
    goal: str,
    level: str,
    days: int,
    equipment: str,
    injuries: Optional[str] = None
) -> str:
    """Queries the Groq LLM API to generate a structured workout plan."""
    # Input validation guard
    if days < 1 or days > 7:
        return "Error: Please select a valid number of days (1 to 7)."

    api_key = os.getenv("GROQ_API_KEY")
    model_name= os.getenv("GROQ_MODEL")
    if not api_key:
        return "API Key Error: GROQ_API_KEY environment variable is not set."

    # System prompt enforcing strict constraints and formatting rules
    system_prompt = (
        "You are an expert personal trainer. Create a highly structured, realistic weekly workout plan.\n"
        "Rules:\n"
        "1. Strictly adhere to the selected equipment access. Do not suggest gear not listed.\n"
        "2. Structure output cleanly by day (e.g., Day 1, Day 2) with explicit exercises, sets, and rep ranges.\n"
        "3. Design precisely the exact number of workout days requested.\n"
        "4. If limitations/injuries are noted, modify exercise selection to avoid strain.\n"
        "5. Include a short medical disclaimer at the bottom if injuries/limitations are present, "
        "and avoid making medical claims."
    )

    user_prompt = f"""
    Client Specs:
    - Goal: {goal}
    - Level: {level}
    - Days per week: {days}
    - Equipment: {equipment}
    - Injuries/Limitations: {injuries if injuries else 'None'}
    """

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.3,
        )
        
        result = response.choices[0].message.content
        if not result or not result.strip():
            return "Error: The model returned an empty response. Please try again."
            
        return result

    except Exception as e:
        return f"API Error: Failed to generate plan. Details: {str(e)}"

# Streamlit UI Construction
st.set_page_config(page_title="Workout Plan Generator", layout="centered")
st.title("🏋️ Workout Plan Generator")

with st.form("workout_form"):
    goal = st.selectbox(
        "Fitness Goal", 
        ["Build muscle", "Lose fat", "General fitness", "Improve endurance"]
    )
    level = st.selectbox(
        "Experience Level", 
        ["Beginner", "Intermediate", "Advanced"]
    )
    days = st.slider("Days available per week", min_value=1, max_value=7, value=3)
    equipment = st.selectbox(
        "Equipment Access", 
        ["No equipment", "Home dumbbells", "Full gym"]
    )
    injuries = st.text_input("Injuries or limitations (optional)", placeholder="e.g., bad knees, lower back pain")
    
    submitted = st.form_submit_button("Generate Plan")

if submitted:
    with st.spinner("Designing your tailored plan..."):
        plan = generate_workout_plan(goal, level, days, equipment, injuries)
        st.markdown("### Your Custom Plan")
        st.write(plan)