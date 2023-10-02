import streamlit as st
from PIL import Image
from pathlib import Path

import settings

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def print_hoc_part(show_answers):

    if show_answers:
        answers = {
            "hboc_part_1_answer_0" : True,
            "hboc_part_2_answer_1" : True,
            "hboc_part_3_answer_1" : True,
            "hboc_part_3_reason" : "Keine ursächliche Variante identifiziert.",
            "hboc_part_4_answer_2" : True,
            "hboc_part_5_answer_0" : 4.2,
            "hboc_part_5_1_answer_1" : True,
            "hboc_part_5_2_answer_0" : "Das Lebenszeitrisiko liegt unter 5%.",
            "hboc_part_7_answer_0" : 8.6,
            "hboc_part_7_answer_1" : True,
            "hboc_part_7_answer_3" : "Das Lebenszeitrisiko liegt jetzt über 5%."
        }
    else:
        answers = {
            "hboc_part_1_answer_0" : False,
            "hboc_part_2_answer_1" : False,
            "hboc_part_3_answer_1" : False,
            "hboc_part_3_reason" : "",
            "hboc_part_4_answer_2" : False,
            "hboc_part_5_answer_0" : 0.0,
            "hboc_part_5_1_answer_1" : False,
            "hboc_part_5_2_answer_0" : "",
            "hboc_part_7_answer_0" : 0.0,
            "hboc_part_7_answer_1" : False,
            "hboc_part_7_answer_3" : ""
        }



    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_1.md"))
    with open('pages/hboc/pdfs/Mertens_et_al_2022.pdf', 'rb') as f:
        st.download_button('Download', f, file_name='Mertens_et_al_2022.pdf')
    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_1_2.md"))
    
    hboc_family_tree = Image.open(settings.hboc_images + "hboc_part_1_family_tree.png")
    st.image(hboc_family_tree)
    with st.expander("Infobox - Kriterien"):
        hboc_infobox_1 = Image.open(settings.hboc_images + "hboc_part_1_infobox_1.png")
        st.image(hboc_infobox_1, "aus Mertens et al., 2022")

    st.markdown(":question: **Wann kann ein Tumorprädispositionssyndrom in der Familie vorliegen?**")

    
    hboc_part_1_options= [
        "Frühes Erkrankungsalter, gehäuftes Auftreten von seltenen Tumorentitäten",
        "Später Erkrankungsalter, gehäuftes Auftreten von seltenen Tumorentitäten",
        "Es gibt keine besonderen Patientenmerkmale"
    ]

    hboc_part_1_answer_0 = st.checkbox(hboc_part_1_options[0], key="hboc_part_1_answer_0", value=answers["hboc_part_1_answer_0"])
    hboc_part_1_answer_1 = st.checkbox(hboc_part_1_options[1], key="hboc_part_1_answer_1")
    hboc_part_1_answer_2 = st.checkbox(hboc_part_1_options[2], key="hboc_part_1_answer_2")

    if hboc_part_1_answer_0 and not hboc_part_1_answer_1 and not hboc_part_1_answer_2:
        st.success("Korrekt!")

        st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_2.md"))

        with st.expander("Infobox - Methodik"):
            hboc_infobox_2 = Image.open(settings.hboc_images + "hboc_part_2_methods.png")
            st.image(hboc_infobox_2, "aus Mertens et al., 2022")

        st.markdown("❓ Welche bevorzugte Möglichkeit der Testung wird der Patientin angeboten?")

        hboc_part_2_options = [
            "Sangersequenzierung",
            "Multigen-Panelanalyse",
            "Genomsequenzierung"
        ]

        hboc_part_2_answer_0 = st.checkbox(hboc_part_2_options[0], key="hboc_part_2_answer_0")
        hboc_part_2_answer_1 = st.checkbox(hboc_part_2_options[1], key="hboc_part_2_answer_1", value=answers["hboc_part_2_answer_1"])
        hboc_part_2_answer_2 = st.checkbox(hboc_part_2_options[2], key="hboc_part_2_answer_2")

        if hboc_part_2_answer_1 and not hboc_part_2_answer_0 and not hboc_part_2_answer_2:
            st.success("Korrekt!")

            st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_3.md"))

            hboc_part_3_answer_0 = st.checkbox("Ja", key="hboc_part_3_answer_0")
            hboc_part_3_answer_1 = st.checkbox("Nein", key="hboc_part_3_answer_1", value=answers["hboc_part_3_answer_1"])

            if hboc_part_3_answer_1 and not hboc_part_3_answer_0:

                hboc_part_3_reason = st.text_area("Begründe", value=answers["hboc_part_3_reason"])

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
                    hboc_part_4_answer_2 = st.checkbox(hboc_part_4_options[2], key="hboc_part_4_answer_2", value=answers["hboc_part_4_answer_2"])
                    hboc_part_4_answer_3 = st.checkbox(hboc_part_4_options[3], key="hboc_part_4_answer_3")

                    if hboc_part_4_answer_2 and not hboc_part_4_answer_0 and not hboc_part_4_answer_1 and not hboc_part_4_answer_3:
                        st.success("Korrekt")
                        # Part 5
                        st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_5.md"))

                        with open('pages/hboc/vcfs/pedigree.txt', 'rb') as f:
                            st.download_button('Download family tree file', f, file_name='pedigree.txt')

                        st.markdown("❓ Wie hoch ist das 10-Jahres-Risiko der Patientin an Brustkrebs zu erkranken?")
                        hboc_part_5_answer_0 = round(st.number_input("Antwort", step=0.1, format="%0.1f", value=answers["hboc_part_5_answer_0"]), 1)
                        
                        if hboc_part_5_answer_0 == 4.2:
                            st.success("Korrekt")
                            st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_5_1.md"))

                            with st.expander("Entscheidungsbaum"):
                                hboc_dec_tree = Image.open(settings.hboc_images + "hboc_part_5_decision_tree.png")
                                st.image(hboc_dec_tree)

                            hboc_part_5_1_answer_0 = st.checkbox("Ja", key="hboc_part_5_1_answer_0")
                            hboc_part_5_1_answer_1 = st.checkbox("Nein", key="hboc_part_5_1_answer_1", value = answers["hboc_part_5_1_answer_1"])

                            if hboc_part_5_1_answer_0 or hboc_part_5_1_answer_1:
                                hboc_part_5_2_answer_0 = st.text_area("Begründe!", value = answers["hboc_part_5_2_answer_0"])    
                            

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
                                    hboc_prs_distr = Image.open(settings.hboc_images + "hboc_part_7_prs_distr.png")
                                    st.image(hboc_prs_distr)
                                    st.markdown(read_markdown_file(settings.hboc_markdown + "hboc_part_7_2.md"))

                                    hboc_part_7_cols = st.columns([1,1])
                                    with hboc_part_7_cols[0]:
                                        with open('pages/hboc/vcfs/prs.vcf', 'rb') as f:
                                            st.download_button('Download prs.vcf', f, file_name='prs.vcf')

                                    hboc_part_7_answer_0 = round(st.number_input("Antwort", step=0.1, format="%0.1f", key="hboc_part_7_answer_0", value = answers["hboc_part_7_answer_0"]), 1)
                                    
                                    if hboc_part_7_answer_0 == 8.6:
                                        st.success("Korrekt")
                                        st.markdown(":question: Ändert sich die Vorsorgeempfehlung?")
                                        hboc_part_7_answer_1 = st.checkbox("Ja", key="hboc_part_7_answer_1", value = answers["hboc_part_7_answer_1"])
                                        hboc_part_7_answer_2 = st.checkbox("Nein", key="hboc_part_7_answer_2")

                                        if hboc_part_7_answer_1 or hboc_part_7_answer_2:
                                            hboc_part_7_answer_3 = st.text_area("Begründe", key="hboc_part_7_answer_3", value = answers["hboc_part_7_answer_3"])

                                            if hboc_part_7_answer_3 != "":
                                                st.success("Zusatzaufgabe abgeschlossen. Ausgezeichnet! :star:")


                                    



