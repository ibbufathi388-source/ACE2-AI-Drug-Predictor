
import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ACEPredict AI",
    page_icon="🧬",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

MODEL_PATH = "../Models/best_model.pkl"
DATA_PATH = "../Output/Final_AI_Dataset.xlsx"

model = joblib.load(MODEL_PATH)
dataset = pd.read_excel(DATA_PATH)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("🧬 ACEPredict AI")

st.markdown(
"""
### AI Powered Drug Binding Affinity Prediction

Predict the binding affinity of drugs against ACE mutations
using an optimized Extra Trees Machine Learning model.
"""
)

st.markdown("---")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("Project Information")

st.sidebar.success("Model : Extra Trees")

st.sidebar.info("Cross Validation MAE : 0.39")

st.sidebar.write("Developer")
st.sidebar.write("Hajeera Hajji")

st.sidebar.markdown("---")


# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

st.header("Prediction")

mutation_list = sorted(dataset["Mutation"].unique())

drug_list = sorted(dataset["Drug_Name"].unique())

col1, col2 = st.columns(2)

with col1:
    mutation = st.selectbox(
        "Select Mutation",
        mutation_list
    )

with col2:
    drug = st.selectbox(
        "Select Drug",
        drug_list
    )



# -------------------------------------------------
# PREDICTION
# -------------------------------------------------

if st.button("🚀 Predict Binding Affinity"):

    row = dataset[
        (dataset["Mutation"] == mutation) &
        (dataset["Drug_Name"] == drug)
    ]

    if row.empty:

        st.error("No matching Mutation-Drug combination found.")

    else:

        feature_columns = [
            'Position',
            'WT_Charge',
            'WT_Hydrophobicity',
            'WT_Molecular_Weight',
            'WT_SideChain_Volume',
            'WT_Aromatic',
            'WT_H_Bond_Donor',
            'WT_H_Bond_Acceptor',
            'Mut_Charge',
            'Mut_Hydrophobicity',
            'Mut_Molecular_Weight',
            'Mut_SideChain_Volume',
            'Mut_Aromatic',
            'Mut_H_Bond_Donor',
            'Mut_H_Bond_Acceptor',
            'Charge_Diff',
            'Hydrophobicity_Diff',
            'MW_Diff',
            'Volume_Diff',
            'HBond_Donor_Diff',
            'HBond_Acceptor_Diff',
            'Aromatic_Changed',
            'MolecularWeight',
            'LogP',
            'TPSA',
            'HBondDonor',
            'HBondAcceptor',
            'RotatableBonds',
            'HeavyAtomCount',
            'RingCount'
        ]

        X = row[feature_columns]

        prediction = model.predict(X)[0]



        st.success("Prediction Completed")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Predicted Binding Affinity",
                f"{prediction:.2f} kcal/mol"
            )

        with col2:

            if prediction <= -9:

                st.success("🟢 Strong Binder")

            elif prediction <= -7:

                st.warning("🟡 Moderate Binder")

            else:

                st.error("🔴 Weak Binder")

        st.markdown("---")

        st.subheader("Drug Information")

        st.write("Drug Name :", row["Drug_Name"].values[0])
        st.write("Drug Class :", row["Drug_Class"].values[0])
        st.write("PubChem CID :", row["PubChem_CID"].values[0])



st.markdown("---")

st.caption("ACEPredict AI")

st.caption("Powered by Extra Trees Machine Learning Model")

