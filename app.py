import streamlit as st

st.set_page_config(page_title="What's Your Vibe?", page_icon="✨", layout="centered")

# ---------- EDIT THIS PART TO MAKE IT PERSONAL ----------

VIBES = {
    "cozy": {
        "title": "Cozy Chaos 🧸",
        "text": "You're warm, funny, and somehow always have snacks. Your plans change "
                "five times but the fun never does. People feel at home around you.",
    },
    "main": {
        "title": "Main Character Energy 🌟",
        "text": "You walk into a room and it gets more interesting. Bold, spontaneous, "
                "and always up for an adventure. Your life has a soundtrack.",
    },
    "sunshine": {
        "title": "Calm Sunshine ☀️",
        "text": "Easygoing and kind, you make everyone around you relax. You notice the "
                "small good things and make them feel bigger.",
    },
    "dreamer": {
        "title": "Midnight Dreamer 🌙",
        "text": "Thoughtful, creative, and a little mysterious. Your best ideas come at "
                "night, and your playlists are unreasonably good.",
    },
}

# Each option is (text shown, which vibe it points to)
QUESTIONS = [
    (
        "Pick a perfect weekend plan:",
        [
            ("Blankets, snacks, and a movie", "cozy"),
            ("Spontaneous trip somewhere new", "main"),
            ("Brunch and a long walk outside", "sunshine"),
            ("Music, art, or a late-night drive", "dreamer"),
        ],
    ),
    (
        "Your go-to snack:",
        [
            ("Anything sweet", "cozy"),
            ("Whatever my friend is having", "main"),
            ("Fresh fruit or something light", "sunshine"),
            ("Coffee or chai, always", "dreamer"),
        ],
    ),
    (
        "How do you reply to texts?",
        [
            ("Voice notes and memes", "cozy"),
            ("Instantly, with lots of emojis", "main"),
            ("Eventually, but with kind words", "sunshine"),
            ("Late at night, in long paragraphs", "dreamer"),
        ],
    ),
    (
        "Pick a song mood:",
        [
            ("Feel-good throwbacks", "cozy"),
            ("Loud and fun, windows down", "main"),
            ("Soft and happy acoustic", "sunshine"),
            ("Slow, moody, and deep", "dreamer"),
        ],
    ),
    (
        "A friend needs cheering up. You:",
        [
            ("Show up with food", "cozy"),
            ("Plan something wild to distract them", "main"),
            ("Listen and give the best hug", "sunshine"),
            ("Send a thoughtful message that hits just right", "dreamer"),
        ],
    ),
]

CLOSING_LINE = "Screenshot your result and send it to me. I'm curious if it's right 😄"

# ---------- APP CODE (no need to edit below) ----------

st.title("✨ What's Your Vibe?")
st.caption("5 quick questions. No wrong answers.")

if "result" not in st.session_state:
    st.session_state.result = None

if st.session_state.result is None:
    with st.form("quiz"):
        name = st.text_input("Your name (optional)")
        answers = []
        for i, (question, options) in enumerate(QUESTIONS):
            choice = st.radio(
                question,
                [o[0] for o in options],
                index=None,
                key=f"q{i}",
            )
            answers.append(choice)
        submitted = st.form_submit_button("Show my vibe ✨", use_container_width=True)

    if submitted:
        if None in answers:
            st.warning("Answer all 5 questions first 🙂")
        else:
            scores = {key: 0 for key in VIBES}
            for (question, options), choice in zip(QUESTIONS, answers):
                for text, vibe in options:
                    if text == choice:
                        scores[vibe] += 1
            winner = max(scores, key=scores.get)
            st.session_state.result = (name.strip(), winner)
            st.rerun()
else:
    name, winner = st.session_state.result
    vibe = VIBES[winner]
    st.balloons()
    greeting = f"{name}, your vibe is" if name else "Your vibe is"
    st.subheader(greeting)
    st.header(vibe["title"])
    st.write(vibe["text"])
    st.info(CLOSING_LINE)
    if st.button("Take it again", use_container_width=True):
        st.session_state.result = None
        for i in range(len(QUESTIONS)):
            st.session_state.pop(f"q{i}", None)
        st.rerun()
