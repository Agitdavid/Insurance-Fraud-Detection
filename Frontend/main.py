import streamlit as st
import json
import requests as re

st.title("Insurance Claims Fraud Detection Web App")

st.image("fraud.jpeg")

st.write("""
## About
Insurance fraud is a deliberate deception perpetrated against or by an insurance company or agent for financial gain. Fraud may be committed at different points by applicants, policyholders, third-party claimants, or professionals who provide services to claimants.

**This Streamlit App utilizes a Machine Learning API in order to detect fraudulent insurance claims  based on the following criteria: AccidentArea, PoliceReportFiled, WitnessPresent, AgentType, BasePolicy, FraudFound and etc.** 

The notebook, model and documentation(Dockerfiles, FastAPI script, Streamlit App script) will soon be available on [GitHub.]()     

**Made by Ochieng' David Agit**

**Contributors:** 
- **William Otieno**
""")


st.sidebar.header('Input Features of The Claim')

PolicyNumber = st.sidebar.text_input("""Input the policy number""")
Deductible = st.sidebar.text_input("""Input the Amount Deducted""")\
Fault = st.sidebar.text_input("""Input the c""")
AccidentArea = st.sidebar.text_input("""Input Area of Accident""")
BasePolicy = st.sidebar.text_input("""Input the Base Policy""")
AgentType = st.sidebar.text_input("""Input the Agent Type""")

PoliceReportFiled = st.sidebar.subheader(f"""
                 Enter Reply:\n\n\n\n
                 0 for 'No' \n 
                 1 for 'Yes' \n """)
PoliceReportFiled = st.sidebar.selectbox("",(0,1))
x = ''
if PoliceReportFiled == 0:
    x = 'Wait for a go Ahead with the check'
if PoliceReportFiled == 1:
    x = 'Go ahead with the check and confirmation'


WitnessPresent = st.sidebar.subheader(f"""
                 Enter Reply:\n\n\n\n
                 0 for 'No' \n 
                 1 for 'Yes' \n """)
WitnessPresent = st.sidebar.selectbox("",(0,1))
x = ''
if WitnessPresent == 0:
    x = 'Wait for a go Ahead with the check'
if WitnessPresent== 1:
    x = 'Go ahead with the check and confirmation'


FraudFound= st.sidebar.selectbox("""Specify if this was flagged as Fraud by your System: """,(0,1))


if  st.button("Detection Result"):
    values = {
    "AccidentArea": AccidentArea,
    "AgentType": AgentType,
    "PoliceReportFiled": PoliceReportFiled,
    "WitnessPresent": WitnessPresent,
    "BasePolicy": BasePolicy,
    "FraudFound": FraudFound
    }


    st.write(f"""### These are the Claim details:\n
    
    1. The area the accident took place: {AccidentArea}\n
    2. Police report filed: {x}\n
    3. Witness Present: {x}\n
    4. Type of Agent: {AgentType}\n
    5. The Base Policy: {BasePolicy}\n
    6. System Flag Fraud Status: {FraudFound}
                """)

    res = re.post(f"http://backend.docker:8000/predict/",json=values)
    json_str = json.dumps(res.json())
    resp = json.loads(json_str)
    
    






