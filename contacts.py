import streamlit as st

def show_contacts_page():

    st.title("Trusted Contacts")
    st.caption("Yeh log SOS pe alert honge")

    st.info("SOS press hone pe inhe turant location aur alert milega")

    st.markdown("---")

    # Session state se contacts store karo
    if "contacts" not in st.session_state:
        st.session_state.contacts = [
            {"name": "Mummy", "phone": "+91 98765 43210", "relation": "Mother"},
            {"name": "Aayushi", "phone": "+91 91234 56789", "relation": "Best Friend"},
            {"name": "Priya Didi", "phone": "+91 99887 76655", "relation": "Sister"},
        ]

    # Contacts dikhao
    for i, contact in enumerate(st.session_state.contacts):
        col1, col2, col3 = st.columns([3, 3, 1])
        with col1:
            st.markdown(f"### {contact['name']}")
            st.caption(contact['relation'])
        with col2:
            st.markdown(f"📞 {contact['phone']}")
        with col3:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.contacts.pop(i)
                st.rerun()
        st.markdown("---")

    # Add Contact
    st.markdown("### Add New Contact")
    new_name = st.text_input("Name")
    new_phone = st.text_input("Phone Number")
    new_relation = st.selectbox("Relation", ["Mother", "Father", "Sister", "Brother", "Friend", "Other"])

    if st.button("Add Contact", type="primary", use_container_width=True):
        if new_name and new_phone:
            st.session_state.contacts.append({
                "name": new_name,
                "phone": new_phone,
                "relation": new_relation
            })
            st.success(f"{new_name} added to trusted contacts!")
            st.rerun()
        else:
            st.error("Enter name and phone number!")
