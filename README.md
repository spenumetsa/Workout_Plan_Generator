# Workout Plan Generator

Generate Personalized Workout Plans. This is a Streamlit web application that generates personalized weekly workout plans using the Groq API (LLM). 

## Features
- **Customizable Inputs:** Define your fitness goal, experience level, days available per week, equipment access, and any injuries/limitations.
- **AI-Powered Plans:** Uses the Groq LLM (e.g., Llama 3) to generate structured, realistic, and tailored workout plans based on your constraints.
- **Responsive UI:** Built with Streamlit for a fast and interactive user experience.

## Prerequisites
- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (for fast Python package management)
- A Groq API Key

## Setup and Installation

1. **Clone or Download the Repository**

2. **Set up the Environment Variable**
   Create a `.env` file in the root directory and add your Groq API key and the model you wish to use:
   ```env
   GROQ_API_KEY=your_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   ```

3. **Install Dependencies**
   This project uses `uv` for dependency management. To install the required packages, run:
   ```bash
   uv sync
   ```

4. **Run the Application**
   Start the Streamlit server using `uv`:
   ```bash
   uv run streamlit run workout_plan.py
   ```

## Usage
Once the server is running, open the provided local URL (typically `http://localhost:8501`) in your web browser. Fill out the form with your fitness details and click "Generate Plan" to get your customized workout routine.
