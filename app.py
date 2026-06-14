import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("threat_model.pkl","rb"))

st.title("NeuroShield AI")

failed_logins = st.slider("Failed Logins",0,50,5)
data_transfer = st.slider("Data Transfer (MB)",0,1000,100)
unknown_process = st.selectbox("Unknown Process",[0,1])

input_data = pd.DataFrame(
    [[failed_logins,data_transfer,unknown_process]],
    columns=['failed_logins','data_transfer_mb','unknown_process']
)

if st.button("Analyze Threat"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("HIGH THREAT DETECTED")
        st.write("Action:")
        st.write("• Block IP")
        st.write("• Quarantine Device")
        st.write("• Alert Administrator")
    else:
        st.success("System Safe")
