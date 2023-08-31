import random
import streamlit as st
from PIL import Image

from pages.wbs import wbs
from pages.hboc import hboc

st.title(":dna: UaK-WebApp der Humangenetik")

"---"
"Welcher Fall wird bearbeitet?"

tabs = st.tabs([":woman_in_lotus_position: FBREK", ":brain: ID"])

# FBREK case
with tabs[0]:
    hboc.print_hoc_part()


# ID case
with tabs[1]:
    wbs.print_wbs_part()