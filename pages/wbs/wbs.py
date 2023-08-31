import random
import streamlit as st
from PIL import Image

import settings

def print_wbs_part():
    st.markdown(
        """
        ## Teil 1: Syndromales Kind in der Familie - Einordnung
        
        Die Eltern berichten, dass der Cousin mütterlicherseits eine geistige Behinderung habe.
        Weiterhin habe er im ersten Lebensjahr eine Herzoperation gehabt.
        Eine genetische Untersuchung sei bislang nicht durchgeführt worden.
        """
    )

    wbs_pedigree = Image.open(settings.wbs_images + "wbs_1_pedigree.png")
    st.image(wbs_pedigree, caption='Familienstammbaum')

    with st.expander("*Plötzlich holt die Mutter ein Foto des Jungen aus der Tasche.*"):
        wbs_patient = Image.open(settings.wbs_images + "wbs_2_patient.png")
        st.image(wbs_patient, caption='Foto des Jungen')

    st.markdown(
        """
        Analysieren Sie das Foto mit Hilfe des Phänotypisierungstools [Face2Gene](https://www.face2gene.com/)!  
        Zugangsdaten bekommen Sie von der DozentIn.
        
        :question: Wie lautet die wahrscheinlichste Diagnose?
        """
    )

    wbs_answer_1 = st.text_input("Antwort hier eingeben").lower()

    if wbs_answer_1 == "":
        wbs_part_2 = False
        st.info("Bitte Antwort eingeben")
    elif ("williams" in wbs_answer_1) & ("beuren" in wbs_answer_1) & ("syndrom" in wbs_answer_1):
        st.success("Korrekt, die höchste Übereinstimmung im Gestalt-Score von Face2Gene hat das Williams-Beuren-Syndrom.")
        wbs_part_2 = True
    else:
        wbs_part_2 = False
        st.warning(f"{wbs_answer_1} ist nicht korrekt.")

    if wbs_part_2:
        wbs_face2gene = Image.open(settings.wbs_images + "wbs_1_face2gene.png")
        st.image(wbs_face2gene)
        st.markdown('[Quelle](http://www.williamssyndrome.org.au/about.php?1)')

        st.markdown(
            """
            ## Teil 2: Syndromales Kind in der Familie - Symptomatik und Ursache
            
            Benutzen Sie GeneReviews für Ihre Recherche: https://www.ncbi.nlm.nih.gov/books/NBK1249/

            :question:	Was sind typische Symptome eines Williams-Beuren-Syndroms (7 Angaben)?
            """
        )

        wbs_symptoms = ["Supravalvular aortic stenosis", "Hypercalcemia", "Low birth weight/slow weight gain", "Developemental delay", "Short stature", "Increased incedence of umbilical and inguinal hernias", "Hyperacusis"]
        wbs_symptoms_convoluted = [
            "Low birth weight/slow weight gain",
            "Hyperacusis",
            "High birth weight",
            "Adipositas",
            "Hypercalcemia",
            "Seizures",
            "Increased incedence of umbilical and inguinal hernias",
            "Supravalvular aortic stenosis",
            "Tumor predisposition",
            "Short stature",
            "Polydactyly",
            "Developemental delay"
            ]
        wbs_part_2_answer_1 = st.multiselect("Antwort", wbs_symptoms_convoluted)
        
        wbs_part_2_answer_1.sort()
        wbs_symptoms.sort()

        if wbs_part_2_answer_1 == wbs_symptoms:
            st.success("Korrekt!")
            wbs_part_2_answer_1_correct = True
            wbs_symptoms_image = Image.open(settings.wbs_images + "wbs_3_symptoms.png")
            st.image(wbs_symptoms_image, caption='WBS-Symptome')
        else:
            wbs_part_2_answer_1_correct = False

        if wbs_part_2_answer_1_correct:
            st.markdown(
                """
                :question: Welche Symptome passen zu den beschriebenen Symptomen des Cousins?
                """
            )
            wbs_part_2_answer_2 = st.multiselect("Antwort", wbs_symptoms)
            wbs_symptoms_cousin = ["Supravalvular aortic stenosis", "Developemental delay"]
            wbs_part_2_answer_2.sort()
            wbs_symptoms_cousin.sort()

            if wbs_part_2_answer_2 == wbs_symptoms_cousin:
                st.success("Korrekt!")
                wbs_part_2_answer_2_correct = True
            else:
                wbs_part_2_answer_2_correct = False

            if wbs_part_2_answer_2_correct:
                st.markdown(
                    """
                    :question:	Was ist die wahrscheinlichste genetische Ursache des Williams-Beuren-Syndroms und wie lautet der Erbgang?
                    """
                )
                wbs_part_3_answer_2_cols=st.columns([1,1])
                with wbs_part_3_answer_2_cols[0]:
                    wbs_part_3_answer_2_cause = st.text_input("Ursache", key="wbs_part_3_answer_2_cause").lower()
                    if "7q11.2" in wbs_part_3_answer_2_cause:
                        st.success("Korrekt!")
                        wbs_part_3_answer_2_cause_correct = True
                    else:
                        wbs_part_3_answer_2_cause_correct = False
                with wbs_part_3_answer_2_cols[1]:
                    wbs_part_3_answer_2_inher = st.text_input("Erbgang", key="wbs_part_3_answer_2_inher").lower()
                    if "autosomal dominant" in wbs_part_3_answer_2_inher:
                        st.success("Korrekt!")
                        wbs_part_3_answer_2_inher_correct = True
                    else:
                        wbs_part_3_answer_2_inher_correct = False

                if wbs_part_3_answer_2_cause_correct and wbs_part_3_answer_2_inher_correct:
                    st.info("Ursache: Mikrodeletion 7q11.2 Erbgang: Autosomal dominant")
                    wbs_cause = Image.open(settings.wbs_images + "wbs_3_cause.png")
                    st.image(wbs_cause, caption='WBS-Ursache')


                    st.markdown(
                        """
                        :question:	Wie hoch ist die Wahrscheinlichkeit, dass der Fetus der aktuellen Schwangerschaft ein Williams-Beuren-Syndrom hat? Die lateinische Bezeichnung der Begründung als Antwort eingeben.
                        """
                    )
                    wbs_part_2_3_cols = st.columns([1,1])
                    with wbs_part_2_3_cols[0]:
                        wbs_part_2_answer_3 = st.selectbox("Antwort", ["unbekannt", "hoch", "moderat", "gering"], key="wbs_part_2_answer_3")
                    with wbs_part_2_3_cols[1]:
                        wbs_part_2_answer_3_2 = st.text_input("Begründung")

                    if wbs_part_2_answer_3 == "gering":
                        wbs_part_2_answer_3_correct = True
                    else:
                        wbs_part_2_answer_3_correct = False
                    
                    if wbs_part_2_answer_3_2 == "de novo":
                        wbs_part_2_answer_3_2_correct = True
                    else:
                        wbs_part_2_answer_3_2_correct = False

                    if wbs_part_2_answer_3_correct and wbs_part_2_answer_3_2_correct:
                        st.success("Korrekt, da die Variante *de novo* vorliegt, ist das Wiederholungsrisiko gering!")

                        st.markdown("---")

                        st.markdown("Damit ist die Übung erfolgreich abgeschlossen.")
                        if st.button("Belohnung!"):
                            st.balloons()