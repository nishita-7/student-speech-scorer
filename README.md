# Transcript Rubric Scorer

This project evaluates a spoken or written self-introduction transcript using a fixed scoring rubric.  
The scoring system assigns values based on key criteria such as clarity, fluency, engagement, grammar, vocabulary richness, and required information presence.

The scoring logic is fully rule-based (not machine learning) and matches the rubric provided.

---

## Features

- Paste text directly into the UI
- Automated scoring based on a predefined rubric
- Provides:
  - Total score (out of 100)
  - Per-criterion breakdown
- No external NLP or AI library required
- Runs locally through **Streamlit**

---

## Rubric Criteria & Max Scores

| Category | Max Score |
|----------|-----------|
| Salutation | 4 |
| Mandatory Details (Name, Age, School/Class, Family, Hobby) | 20 |
| Optional Details (Origin, Goal, Unique fact, Achievement, Strength) | 10 |
| Flow / Sentence Smoothness | 5 |
| Speech Length / Rate | 10 |
| Grammar | 10 |
| Vocabulary Richness (TTR) | 8 |
| Clarity (No filler words) | 15 |
| Engagement | 12 |
| **Total** | **100** |
