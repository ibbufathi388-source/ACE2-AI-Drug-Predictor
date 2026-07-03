import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ACE2Predict AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Animated Background */

.stApp{
background:linear-gradient(
135deg,
#040B1A,
#081F45,
#3B0A62,
#004D66);

background-size:400% 400%;

animation:gradientBG 15s ease infinite;

color:white;
}

@keyframes gradientBG{

0%{
background-position:0% 50%;
}

50%{
background-position:100% 50%;
}

100%{
background-position:0% 50%;
}

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:rgba(8,15,35,.85);

backdrop-filter:blur(18px);

border-right:1px solid rgba(255,255,255,.08);

}

/* Buttons */

.stButton > button{

width:100%;

height:60px;

border:none;

border-radius:18px;

font-size:18px;

font-weight:700;

color:white;

background:linear-gradient(
90deg,
#00D4FF,
#7B61FF);

box-shadow:0 0 30px rgba(0,212,255,.45);

transition:.35s;

}

.stButton > button:hover{

transform:scale(1.02);

box-shadow:0 0 45px cyan;

}

/* Selectbox */

div[data-baseweb="select"]{

border-radius:15px;

}

/* Metric Card */

div[data-testid="stMetric"]{

background:rgba(255,255,255,.08);

padding:20px;

border-radius:18px;

border:1px solid rgba(255,255,255,.15);

backdrop-filter:blur(18px);

}

/* Horizontal Line */

hr{

border:1px solid rgba(255,255,255,.15);

}

/* Headings */

h1,h2,h3,h4{

color:white;

}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "Models" / "best_model.pkl"
DATA_PATH = BASE_DIR / "Output" / "Final_AI_Dataset.xlsx"

model = joblib.load(MODEL_PATH)
dataset = pd.read_excel(DATA_PATH)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------

st.markdown("""
<div style="background:rgba(255,255,255,0.06);
padding:35px;border-radius:25px;
backdrop-filter:blur(20px);
border:1px solid rgba(255,255,255,0.12);
box-shadow:0 0 35px rgba(0,212,255,.18);
text-align:center;">

<h1 style="font-size:55px;color:white;margin-bottom:10px;">
🧬 ACE2Predict AI
</h1>

<h3 style="color:#BBD8FF;font-weight:400;">
AI Powered Drug Binding Affinity Prediction Platform
</h3>

<p style="font-size:18px;color:#D8E7FF;">
Bioinformatics • Machine Learning • Explainable AI • Drug Discovery
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

with st.sidebar:

    st.markdown("""
    <h2 style='text-align:center;color:#00E5FF;'>
    🧬 ACE2Predict AI
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("Machine Learning Model")
    st.write("**Extra Trees Regressor**")

    st.info("📈 R² Score : **0.993**")

    st.info("📊 Cross Validation MAE : **0.39**")

    st.markdown("---")

    st.markdown("### Developer")

    st.success("Hajeera • Avanthy • Durga")

    st.markdown("---")

    st.markdown("### Technologies")

    st.markdown("""
  Python

  Machine Learning

  Bioinformatics

  Explainable AI (SHAP)

  Streamlit

  GitHub

  Molecular Docking
""")

    st.markdown("---")

    st.caption("ACE2Predict AI v2.1")
# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

st.markdown("""

<div style="background:rgba(255,255,255,.07);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,.12);
backdrop-filter:blur(15px);
box-shadow:0 0 25px rgba(0,212,255,.15);">
<h2 style="color:white;text-align:center;">

🧪 Drug Binding Affinity Prediction

</h2>

<p style="text-align:center;color:#D6E8FF;">

Choose a mutation and a drug to predict the binding affinity using our trained AI model.

</p>

</div>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

mutation_list = sorted(dataset["Mutation"].unique())

drug_list = sorted(dataset["Drug_Name"].unique())

left, right = st.columns(2)

with left:

    mutation = st.selectbox(
        "🧬 Select Mutation",
        mutation_list
    )

with right:

    drug = st.selectbox(
        "💊 Select Drug",
        drug_list
    )

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# PREDICTION
# -------------------------------------------------

if st.button("🚀 Predict Binding Affinity"):

    row = dataset[
        (dataset["Mutation"] == mutation) &
        (dataset["Drug_Name"] == drug)
    ]

    if row.empty:

        st.error("❌ No matching Mutation-Drug combination found.")

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

        st.markdown("---")

        st.markdown("## 🎯 Prediction Result")

        c1, c2 = st.columns([2,1])

        with c1:

            st.metric(
                "🧬 Predicted Binding Affinity",
                f"{prediction:.2f} kcal/mol"
            )

        with c2:

            if prediction <= -9:
                st.success("🟢 Strong Binder")

            elif prediction <= -7:
                st.warning("🟡 Moderate Binder")

            else:
                st.error("🔴 Weak Binder")

        st.markdown("---")

        st.markdown("## 💊 Drug Properties")

        d1, d2 = st.columns(2)

        with d1:

            st.info(f"**Drug Name**\n\n{row['Drug_Name'].values[0]}")
            st.info(f"**Drug Class**\n\n{row['Drug_Class'].values[0]}")
            st.info(f"**PubChem CID**\n\n{row['PubChem_CID'].values[0]}")
            st.info(f"**Molecular Weight**\n\n{row['MolecularWeight'].values[0]}")
            st.info(f"**LogP**\n\n{row['LogP'].values[0]}")

        with d2:

            st.info(f"**TPSA**\n\n{row['TPSA'].values[0]}")
            st.info(f"**H-Bond Donor**\n\n{row['HBondDonor'].values[0]}")
            st.info(f"**H-Bond Acceptor**\n\n{row['HBondAcceptor'].values[0]}")
            st.info(f"**Rotatable Bonds**\n\n{row['RotatableBonds'].values[0]}")
            st.info(f"**Heavy Atom Count**\n\n{row['HeavyAtomCount'].values[0]}")
            st.info(f"**Ring Count**\n\n{row['RingCount'].values[0]}")


st.markdown("""
<div style="
background:linear-gradient(
90deg,
rgba(0,212,255,.15),
rgba(123,97,255,.15)
);
padding:18px;
border-radius:20px;
border:1px solid rgba(255,255,255,.12);
text-align:center;
margin-bottom:25px;
">
<h4 style="color:white;">
🧬 AI • Bioinformatics • Machine Learning • Explainable AI
</h4>
</div>
""", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
<div style="
background:rgba(255,255,255,.06);
padding:20px;
border-radius:18px;
text-align:center;
border:1px solid rgba(255,255,255,.10);
">
<h3 style="color:#00D4FF;">🧬 ACE2Predict AI</h3>
<p style="color:white;font-size:20px;line-height:1.8;">
 Developed by<br>
<b>Hajeera</b> • <b>Avanthy</b> • <b>Durga</b>
</p>
<p style="color:#C7D2FE;">
AI Powered Drug Binding Affinity Prediction Platform
</p>
</div>
""", unsafe_allow_html=True)

