import re
from collections import Counter

def score_text(text: str):
    text_lower = text.lower()
    words = re.findall(r"\b\w+\b", text_lower)
    total_words = len(words)

    # Salutation Score
    salutations = ["hello", "hi", "good morning", "good afternoon", "good evening"]
    salutation_score = 4 if any(text_lower.startswith(s) for s in salutations) else 0

    # Mandatory Field Rubric 
    mandatory_criteria = {
        "name": [r"my name is", r"myself", r"\bi am\b"],
        "age": [r"\b\d{1,2}\s?years? old\b"],
        "school/class": [r"class", r"standard", r"grade", r"school"],
        "family": ["family", "parents", "mother", "father"],
        "hobby/interest": ["hobby", "like to", "enjoy", "favorite", "play"]
    }

    mandatory_score = 0
    for patterns in mandatory_criteria.values():
        if any(re.search(p, text_lower) for p in patterns):
            mandatory_score += 4

    # Optional
    optional_criteria = {
        "origin": ["from", "born in", "native"],
        "goal": ["goal", "wish", "dream", "future"],
        "unique fact": ["fun fact", "one thing", "special", "interesting"],
        "achievements": ["prize", "won", "achievement", "certificate"],
        "strength": ["i am good at", "strength", "confident", "skill"]
    }

    optional_hits = sum(1 for patterns in optional_criteria.values()
                        if any(p in text_lower for p in patterns))

    optional_score = min(optional_hits * 2, 10)

    # Flow (Based on sentence smoothness)
    sentences = list(filter(None, re.split(r"[.!?]", text_lower)))
    avg_sentence = total_words / len(sentences) if sentences else 0

    if avg_sentence >= 12:
        flow_score = 5
    elif avg_sentence >= 8:
        flow_score = 4
    elif avg_sentence >= 5:
        flow_score = 3
    else:
        flow_score = 2

    # Speech Rate Score (Based on length range)
    speech_rate_score = 10 if total_words >= 80 else 8

    # Grammar Score
    grammar_penalties = text.count("..") + text.count("??") + text.count("!!")
    grammar_score = max(10 - grammar_penalties * 2, 6)

    # Vocabulary Richness (TTR Scale)
    unique_words = len(set(words))
    ttr = unique_words / total_words if total_words else 0

    if ttr >= 0.7:
        vocabulary_score = 8
    elif ttr >= 0.5:
        vocabulary_score = 6
    elif ttr >= 0.3:
        vocabulary_score = 4
    else:
        vocabulary_score = 2

    # Clarity (Filler Words reduction)
    filler_words = ["umm", "uh", "like", "basically", "actually", "you know"]
    filler_count = sum(text_lower.count(f) for f in filler_words)
    clarity_score = max(15 - filler_count * 3, 5)

    # Engagement Score
    engagement_markers = ["fun fact", "i enjoy", "i like", "one thing", "thank you"]
    engagement_hits = sum(text_lower.count(p) for p in engagement_markers)
    engagement_score = min(engagement_hits * 3, 12)

    # Final Calculation
    breakdown = {
        "Salutation": salutation_score,
        "Mandatory Keywords": mandatory_score,
        "Optional Keywords": optional_score,
        "Flow": flow_score,
        "Speech Rate": speech_rate_score,
        "Grammar": grammar_score,
        "Vocabulary": vocabulary_score,
        "Clarity (Filler Words)": clarity_score,
        "Engagement": engagement_score
    }

    overall_score = sum(breakdown.values())  # ← FIXED (no scaling)

    return {"overall_score": overall_score, "breakdown": breakdown}


# ----------- Test with sample text -----------
if __name__ == "__main__":
    sample = """Hello everyone, myself Muskan, studying in class 8th B section from Christ Public School. 
    I am 13 years old. I live with my family. There are 3 people in my family, me, my mother and my father.
    One special thing about my family is that they are very kind hearted to everyone and soft spoken. One thing I really enjoy is play, playing cricket and taking wickets.
    A fun fact about me is that I see in mirror and talk by myself. One thing people don't know about me is that I once stole a toy from one of my cousin.
    My favorite subject is science because it is very interesting. Through science I can explore the whole world and make the discoveries and improve the lives of others. 
    Thank you for listening."""
    
    print(score_text(sample))
