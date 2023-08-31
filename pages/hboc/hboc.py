import streamlit as st
from PIL import Image
from pathlib import Path

import settings

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def print_hoc_part():

    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_1.md"))
    hboc_family_tree = Image.open(settings.hboc_images + "hboc_part_1_family_tree.png")
    st.image(hboc_family_tree)
    st.markdown(":question: **Wann kann ein Tumorprädispositionssyndrom in der Familie vorliegen?**")

    hboc_part_1_options= [
        "Frühes Erkrankungsalter, gehäuftes Auftreten von seltenen Tumorentitäten",
        "Später Erkrankungsalter, gehäuftes Auftreten von seltenen Tumorentitäten",
        "Es gibt keine besonderen Patientenmerkmale"
    ]

    hboc_part_1_answer_0 = st.checkbox(hboc_part_1_options[0], key="hboc_part_1_answer_0")
    hboc_part_1_answer_1 = st.checkbox(hboc_part_1_options[1], key="hboc_part_1_answer_1")
    hboc_part_1_answer_2 = st.checkbox(hboc_part_1_options[2], key="hboc_part_1_answer_2")

    if hboc_part_1_answer_0 and not hboc_part_1_answer_1 and not hboc_part_1_answer_2:
        st.success("Korrekt!")

        st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_2.md"))

        hboc_part_2_options = [
            "Sangersequenzierung",
            "Multigen-Panelanalyse",
            "Genomsequenzierung"
        ]

        hboc_part_2_answer_0 = st.checkbox(hboc_part_2_options[0], key="hboc_part_2_answer_0")
        hboc_part_2_answer_1 = st.checkbox(hboc_part_2_options[1], key="hboc_part_2_answer_1")
        hboc_part_2_answer_2 = st.checkbox(hboc_part_2_options[2], key="hboc_part_2_answer_2")

        if hboc_part_2_answer_1 and not hboc_part_2_answer_0 and not hboc_part_2_answer_2:
            st.success("Korrekt!")

            st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_3.md"))

            hboc_part_3_answer_0 = st.checkbox("Ja", key="hboc_part_3_answer_0")
            hboc_part_3_answer_1 = st.checkbox("Nein", key="hboc_part_3_answer_1")

            if hboc_part_3_answer_1 and not hboc_part_3_answer_0:

                hboc_part_3_reason = st.text_area("Begründe")

                if hboc_part_3_reason != "":

                    # Part 4
                    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_4.md"))

                    hboc_part_4_options = [
                        "Risikominimierende Operation",
                        "Einschluss in ein Vorsorgeprogramm", 
                        "Berechnung des Risikos über das CanRisk-Tool",
                        "keine weiteren Maßnahmen notwendig"
                    ]

                    hboc_part_4_answer_0 = st.checkbox(hboc_part_4_options[0], key="hboc_part_4_answer_0")
                    hboc_part_4_answer_1 = st.checkbox(hboc_part_4_options[1], key="hboc_part_4_answer_1")
                    hboc_part_4_answer_2 = st.checkbox(hboc_part_4_options[2], key="hboc_part_4_answer_2")
                    hboc_part_4_answer_3 = st.checkbox(hboc_part_4_options[3], key="hboc_part_4_answer_3")

                    if hboc_part_4_answer_2 and not hboc_part_4_answer_0 and not hboc_part_4_answer_1 and not hboc_part_4_answer_3:
                        st.success("Korrekt")
                        # Part 5
                        st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_5.md"))
                        
                        hboc_part_5_answer_0 = st.text_area("Antwort")

                        if hboc_part_5_answer_0 != "":
                            st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_5_1.md"))

                            hboc_part_5_1_answer_0 = st.checkbox("Ja", key="hboc_part_5_1_answer_0")
                            hboc_part_5_1_answer_1 = st.checkbox("Nein", key="hboc_part_5_1_answer_1")

                            if hboc_part_5_1_answer_0 or hboc_part_5_1_answer_1:
                                hboc_part_5_2_answer_0 = st.text_area("Begründe!")    
                            

                                if hboc_part_5_2_answer_0 != "":
                                    st.success("Damit ist die Übung abgeschlossen!")

                                    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_6.md"))
                                    hboc_canrisk = Image.open(settings.hboc_images + "hboc_part_6_canrisk.png")
                                    st.image(hboc_canrisk)
                                    hboc_tumor = Image.open(settings.hboc_images + "hboc_part_6_tumorogenesis.png")
                                    st.image(hboc_tumor)

                                    if st.button("Belohnung"):
                                        st.balloons()

                                    # Part 7
                                    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_7.md"))

                                    hboc_part_7_cols = st.columns([1,1])
                                    with hboc_part_7_cols[0]:
                                        with open('pages/hboc/vcfs/low_prs.vcf', 'rb') as f:
                                            st.download_button('Download low_prs.vcf', f, file_name='low_prs.vcf')

                                    with hboc_part_7_cols[1]:
                                        with open('pages/hboc/vcfs/high_prs.vcf', 'rb') as f:
                                            st.download_button('Download high_prs.vcf', f, file_name='high_prs.vcf')

                                    hboc_part_7_answer = st.text_area("Antwort", key="hboc_part_7_answer")


                                    



