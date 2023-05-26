# importation des bibliotheques
import streamlit as st
import pandas as pd 


# fonction globale
def global_function():

    # importation du dataset
    @st.cache_data
    def load_data():
        df = pd.read_csv("train.csv")
        df = df.drop(['id', 'Policy_Sales_Channel', 'Region_Code'], axis=1)
        df_sample = df.sample(300)
        return df_sample

    st.title("PREDICTION DU COMPORTEMENT DES ACHETEURS D'ASSURANCE")

    st.subheader("Par jalil KETOU, ing. logiciel/data scientist")

    st.write("Cette application permet a l'entreprise ANALYTICS VHIDIA de predire le comportement des ses client face a l'achat des assurances des vehcules")

    st.write("Pour nous aider a mieux remplir notre mission, veuillez remplire les informations suivantes.")

    # afficher le dataset
    if st.checkbox("Afficher le dataset")==True:
        df = load_data()
        st.write(df)

    st.write("")
    st.write("")

    # le sex
    gender = st.radio("veuillez nous renseigner sur votre sexe", ['Masculin', 'Feminin'])
    st.write("")
    st.write("")

    #  l'age du client
    age = st.number_input("veuillez nous renseigner sur votre age", step=1)
    st.write("")
    st.write("")

    # le permit de conduire
    driving_licence = st.radio("Disposez-vous d'un permit de conduire?", ['Oui', 'Non'])
    st.write("")
    st.write("")

    # precedent assurance
    previously_insured = st.radio("Avez-vous deja dispioser d'un permit de conduire?", ['Oui', 'Non'])
    st.write("")
    st.write("")

    # age du vehicule
    vehicle_age = st.selectbox("Veuillez nous renseigner sur l'age de votre vehicule", ['Pus de 2 ans', "Moins d'un an", "Entre 1 et 2 ans"])
    st.write("")
    st.write("")

    # l'accident de voiture
    vehicle_damage = st.radio("Le vehicule a deja fait un accident?", ['Oui', 'Non'])
    st.write("")
    st.write("")

    # abonnement annuel
    annual_premium = st.number_input("Veuillez nous renseigner sur le prix de votre abonnement annuel", step=1)
    st.write("")
    st.write("")

    # la dure du client dans l'entreprise
    vintage = st.number_input("Nombre de jour que avez passe avec l'entreprise en tant que client (en jour!)", step=1)


    # telechargement des modeles
    

if __name__=="__main__":
    global_function()