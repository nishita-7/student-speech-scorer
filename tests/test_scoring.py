# tests/test_scoring.py
from scoring import word_count, keyword_match_score, length_score
from scoring import score_criterion, score_transcript
from sentence_transformers import SentenceTransformer
import pytest

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def test_word_count():
    assert word_count('Hello world') == 2

def test_keyword_match_score():
    frac, found = keyword_match_score('My name is Ananya and I study CS', ['ananya', 'math'])
    assert frac == pytest.approx(0.5)
    assert 'ananya' in found

def test_length_score():
    assert length_score(15, 10, 20) == 1.0
    assert length_score(5, 10, 20) < 1.0

def test_score_transcript_basic():
    rubric = [
        {'id': 'Intro', 'description': 'Introduce yourself and your background', 'keywords': ['name', 'background'], 'weight': 1.0, 'min_words': 5, 'max_words': 50}
    ]
    t = 'Hi, my name is Ananya and I am studying computer science.'
    out = score_transcript(t, rubric, MODEL)
    assert 'overall_score' in out
    assert out['words'] > 0
