# app.py
import streamlit as st
import json
from scoring import score_text
from pathlib import Path

st.set_page_config(page_title="Transcript Rubric Scorer", layout="centered")
st.title("Transcript Rubric Scorer (Rubric-based)")

st.markdown(
    """
    Paste a transcript or upload a `.txt` file. Click **Score** to compute per-criterion scores and an overall score.
    This app uses the rubric you provided and the exact scoring logic in `scoring.py`.
    """
)

# Transcript input
st.subheader("Paste transcript text")
transcript = st.text_area("Enter transcript here", height=280)

if st.button("Score"):
    if not transcript.strip():
        st.error("Please paste a transcript or upload a .txt file.")
    else:
        with st.spinner("Scoring transcript..."):
            result = score_text(transcript)

        # Show overall
        st.success(f"Overall score: {result['overall_score']} / 100 (rubric-scale)")

        # Per-criterion breakdown (nice display)
        st.subheader("Per-criterion breakdown")
        breakdown = result.get("breakdown", {})
        for name, val in breakdown.items():
            st.markdown(f"**{name}** — {val}")
        st.write("---")