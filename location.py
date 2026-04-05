import streamlit as st

def show_location_page():

    st.title("Live Location")
    st.caption("Real-time GPS tracking")

    st.markdown("---")

    # Location Status
    col1, col2 = st.columns(2)
    with col1:
        sharing = st.toggle("Location Sharing ON/OFF")
        if sharing:
            st.success("Location shared")
        else:
            st.warning("Location sharing stopped")

    with col2:
        stealth = st.toggle("Stealth Mode ON/OFF")
        if stealth:
            st.info("Stealth mode ON ")
        else:
            st.info("Normal mode ")

    st.markdown("---")

    # Fake Map
    st.markdown("### Current Location")
    st.map()

    st.markdown("---")

    # Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Alert Time", value="3 sec", delta="Fast")
    with col2:
        st.metric(label="Alert Radius", value="500m", delta="Active")
    with col3:
        st.metric(label="Battery Use", value="Low", delta="Optimized")

    st.markdown("---")
    st.caption("Location data is end-to-end encrypted and only shared with trusted contacts when SOS is activated.")