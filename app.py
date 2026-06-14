import streamlit as st

st.title("NeuroSentinel AI")

failed_logins = st.slider("Failed Logins",0,50,5)
data_transfer = st.slider("Data Transfer (MB)",0,1000,100)
unknown_process = st.selectbox("Unknown Process",[0,1])

if st.button("Analyze Threat"):
    score = failed_logins + (data_transfer/50) + (unknown_process*20)

    if score > 40:
        st.error("HIGH THREAT DETECTED")
        st.write("Recommended Actions:")
        st.write("• Block suspicious IP")
        st.write("• Quarantine device")
        st.write("• Alert administrator")
    else:
        st.success("System Safe")
