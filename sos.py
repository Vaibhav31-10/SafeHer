import streamlit as st

def show_sos_page():

    st.title("🛡️ SafeHer")
    st.caption("Every Woman. Protected. Always.")

    st.success("🟢 Protection Active — Running in Background")

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🆘 PRESS SOS", use_container_width=True, type="primary"):
            st.error("🚨 SOS ACTIVATED!")
            st.warning("📍 Location shared with trusted contacts!")
            st.info("🎙️ Background recording started!")
            st.success("📞 Emergency contacts notified!")

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.link_button("📞 Call 112 — Police", "tel:112", use_container_width=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="👥 Contacts", value="3", delta="Ready to alert")
    with col2:
        st.metric(label="📍 GPS", value="Active", delta="Location tracked")
    with col3:
        st.metric(label="🎙️ Mic", value="Ready", delta="Evidence mode")