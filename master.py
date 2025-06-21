import streamlit as st

# Page configuration
st.set_page_config(page_title="Master of Masters", layout="centered")

# Initialize session state flags for viewing policies
for key in ["terms_viewed", "refund_viewed", "privacy_viewed"]:
    if key not in st.session_state:
        st.session_state[key] = False

# Title and Header
st.title("Ayushman Bhava")
st.markdown("### Learn Meditation & Kriya Yoga from the Enlightened Guide")
st.image("https://via.placeholder.com/300", caption="B. Venkateshwar Rao", use_container_width=False)

# Testimonials
st.markdown("## 🧘‍♂️ Student Experiences")
st.markdown("""
<iframe width="100%" height="315" src="https://www.youtube.com/embed/rCl1wvD479Y?si=l-GK3Nr_b-3jIUUm" 
title="YouTube video" frameborder="0" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# About the Teacher
st.markdown("## 🙏 About the Yoga Teacher")
st.write("""
B. Venkateshwar Rao is a seasoned master in the fields of Meditation and Kriya Yoga Sadhana. 
With decades of spiritual dedication and transformative experiences, he has guided hundreds 
towards inner peace and true consciousness. His unique energy and divine understanding have 
earned him the reverence of being called the "Master of Masters."
""")

# Class Selection
st.markdown("## 💸 Join the Class")
option = st.radio("Select Class Type", ("Online Class - ₹999", "Offline Class - ₹799"))
name = st.text_input("Enter your name")
phone = st.text_input("Enter your phone number")

# Policy Modal Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("View Terms"):
        with st.modal("📄 Terms and Conditions"):
            st.session_state.terms_viewed = True
            st.markdown("""
            - Classes are for spiritual and wellness learning only.  
            - No sharing of session content.  
            - Misconduct leads to termination without refund.
            """)

with col2:
    if st.button("View Refund Policy"):
        with st.modal("🔄 Cancellations and Refunds"):
            st.session_state.refund_viewed = True
            st.markdown("""
            - No refunds post-registration.  
            - Rescheduling available for valid reasons (once only).  
            - Organizer cancellations = full reschedule.
            """)

with col3:
    if st.button("View Privacy Policy"):
        with st.modal("🔐 Privacy Policy"):
            st.session_state.privacy_viewed = True
            st.markdown("""
            - Your data is used only for communication.  
            - No sharing with third parties.  
            - Stored securely and treated confidentially.
            """)

# Acknowledgment Status
st.markdown("### ✅ Policy Acknowledgment Status")
st.write(f"✔️ Terms & Conditions: {'Viewed ✅' if st.session_state.terms_viewed else '❌ Not viewed'}")
st.write(f"✔️ Cancellations & Refunds: {'Viewed ✅' if st.session_state.refund_viewed else '❌ Not viewed'}")
st.write(f"✔️ Privacy Policy: {'Viewed ✅' if st.session_state.privacy_viewed else '❌ Not viewed'}")

# Simulated Payment Button
st.markdown("### 🚀 Confirm Payment")
if st.button("Pay Now (Simulation Only)"):
    if not (name and phone):
        st.warning("Please enter your name and phone number.")
    elif not (st.session_state.terms_viewed and st.session_state.refund_viewed and st.session_state.privacy_viewed):
        st.warning("Please view and acknowledge all policies before proceeding.")
    else:
        st.success("Thank you! This is a test payment simulation only.")
        st.info("Live payment will be enabled once Razorpay approves the website.")

# Footer (safe HTML)
st.markdown("""
---
<div style="text-align: center;">
    © 2025 Ayushman Bhava | All Rights Reserved<br>
    Contact: <a href="mailto:ayushmanbhava@gmail.com">ayushmanbhava@gmail.com</a>
</div>
""", unsafe_allow_html=True)
