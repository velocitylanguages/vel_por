"""VELOCITY PORTUGUESE - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY PORTUGUESE"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "PORTUGUESE"
HANDLE = "@velocityportuguese"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "pt",
    "name": "Portuguese",
    "native_name": "Português",
    "history_key": "portuguese",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "pt-BR-AntonioNeural",
    "native_fallback_voice": "pt-BR-FranciscaNeural",
    "native_engine": "edge",
    "native_lang_code": "pt",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "PORTUGUÊS",
    "translit_label": "SAY IT LIKE",
    "greeting": "Olá!",
    "encouragement": "Excelente!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Motivation", "Motivação", "rocket", "#A560E8"),
    ("Love", "Amor", "heart", "#FF4B4B"),
    ("Success", "Sucesso", "trophy", "#F5A700"),
    ("Wisdom", "Sabedoria", "book", "#A560E8"),
    ("Happiness", "Felicidade", "smile", "#F5A700"),
    ("Self Improvement", "Desenvolvimento Pessoal", "leaf", "#58CC02"),
    ("Gratitude", "Gratidão", "heart", "#FF7A00"),
    ("Friendship", "Amizade", "users", "#00A889"),
    ("Hope", "Esperança", "sun", "#FF7A00"),
    ("Creativity", "Criatividade", "palette", "#E056A0"),
    ("Inner Peace", "Paz Interior", "lotus", "#00A889"),
    ("Confidence", "Confiança", "shield", "#1CB0F6"),
    ("Perseverance", "Perseverança", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiração", "sparkles", "#A560E8"),
    ("Positive Life", "Vida Positiva", "sun", "#58CC02"),
    ("Courage", "Coragem", "shield", "#FF4B4B"),
    ("Kindness", "Bondade", "heart", "#E056A0"),
    ("Patience", "Paciência", "hourglass", "#00A889"),
    ("Forgiveness", "Perdão", "hands", "#FF7A00"),
    ("Strength", "Força", "dumbbell", "#FF4B4B"),
    ("Joy", "Alegria", "smile", "#F5A700"),
    ("Balance", "Equilíbrio", "scale", "#00A889"),
    ("Growth", "Crescimento", "sprout", "#58CC02"),
    ("Purpose", "Propósito", "target", "#A560E8"),
    ("Mindfulness", "Atenção Plena", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnportuguese",
    "#portugueselessons",
    "#portugueseforbeginners",
    "#languagelearning",
    "#portuguesevocabulary",
    "#velocityportuguese",
    "#dailyportuguese",
    "#portuguese",
    "#learnlanguages",
    "#speakportuguese",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
