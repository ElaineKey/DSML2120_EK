import streamlit as st
from pathlib import Path

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Elaine Key"
PROGRAM = "Data Science and Machine Learning"

INTRO = (
    "Building modeling systems for @Refrag, and visualizing professional "
    "data from @ESL/MDL. I hope to one day do data science for a company "
    "that understands how powerful data aggregation is to the common user, "
    "while celebrating and accepting that connection.\n\n"
    "Data visualization and computing is the routing for all advancement "
    "in computer science and software engineering!"
)

FUN_FACTS = [
    "I love drawing, sports science, and hardware engineering!",
    "I’m learning data science, machine structure, and photography.",
    "I want to build a useful data aggregation tool for @CS2 players to improve their play.",
]


PHOTO_PATH = "your_photo.jpg"  # Put a file in repo root or set a URL


def find_photo(filename=PHOTO_PATH):
    # Try common locations for multipage apps
    try:
        script_dir = Path(__file__).resolve().parent
    except NameError:
        script_dir = Path.cwd()

    candidates = [
        script_dir / "assets" / filename,          # pages/assets/...
        script_dir.parent / "assets" / filename,   # root/assets/... (common)
        Path("assets") / filename,                 # cwd/assets/...
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    return None

photo_src = find_photo(PHOTO_PATH)

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    if photo_src:
        st.image(photo_src, caption=NAME, use_container_width=True)
    else:
        st.info(
            "📷 Place `Your_Photo.jpg` inside an `assets/` folder at the app root "
            "or update the path in `find_photo()`."
        )
        
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
