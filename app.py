import streamlit as st

st.title("NeuroSentinel AI")

failed_logins = st.slider("Failed Logins",0,50,5)
data_transfer = st.slider("Data Transfer (MB)",0,1000,100)
unknown_process = st.selectbox("Unknown Process",[0,1])

if st.button("Analyze Threat"):

    score = failed_logins + (data_transfer / 50) + (unknown_process * 20)

    st.metric("Threat Score", round(score, 2))
    st.progress(min(int(score), 100))

    if score > 70:
        st.error("🔴 CRITICAL THREAT DETECTED")
    elif score > 40:
        st.warning("🟠 MEDIUM THREAT DETECTED")
    else:
        st.success("🟢 SYSTEM SAFE")

    st.subheader("Recommended Actions")

    if score > 40:
        st.write("✅ Block Suspicious IP")
        st.write("✅ Quarantine Device")
        st.write("✅ Alert Administrator")
    else:
        st.write("✅ Continue Monitoring")
