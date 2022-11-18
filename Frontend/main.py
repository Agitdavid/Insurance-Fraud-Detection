import streamlit as st
import json
import requests as re
from PIL import Image
st.title("Insurance Claims Fraud Detection Web App")

image = Image.open('fraud.jpeg')
st.image(image, width=400)


st.write("""
## About
Insurance fraud is a deliberate deception perpetrated against or by an insurance company or agent for financial gain. Fraud may be committed at different points by applicants, policyholders, third-party claimants, or professionals who provide services to claimants.

**This Streamlit App utilizes a Machine Learning API in order to detect fraudulent insurance claims  based on the following criteria: Deductible, AccidentArea, Fault,PastNumberOfClaims, BasePolicy, FraudFound and etc.** 


""")


st.sidebar.header('Input Features of The Claim')

Deductible = st.sidebar.text_input("""Input the Amount Deducted""")
AccidentArea = st.sidebar.selectbox("""Input Area of Accident""", ('Urban', 'Rural'))
Fault = st.sidebar.selectbox("""Input the fault""", ('Policy Holder', 'Third-party'))
BasePolicy = st.sidebar.selectbox("""Input the Base Policy""", ('Liability', 'Collision', 'All Perils'))
PastNumberOfClaims = st.sidebar.text_input("""How many previous claims""")
FraudFound= st.sidebar.selectbox("""Specify if this was flagged as Fraud by your System: """,(0,1))


if  st.button("Predict"):
    values = {
    "Deductible": Deductible,
    "AccidentArea": AccidentArea,
    "Fault": Fault,
    "BasePolicy": BasePolicy,
    "PastNumberOfClaims": PastNumberOfClaims,
    "FraudFound": FraudFound
    }


    st.write(f"""### These are the Claim details:\n
    
    1. The area the amount deducted: {Deductible}\n
    2. The area of the accident: {AccidentArea}\n
    3. The fault was: {Fault}\n
    4. The Base Policy: {BasePolicy}\n
    5. The number of past claims: {PastNumberOfClaims}\n
    6. System Flag Fraud Status: {FraudFound}
                """)

    res = re.post(f"http://backend.docker:8000/predict/",json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    






