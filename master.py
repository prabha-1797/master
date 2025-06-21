import streamlit as st

# Page configuration
st.set_page_config(page_title="Master of Masters", layout="centered")

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

# Checkboxes for policies
st.markdown("### 📋 Please agree to the following policies to continue:")

terms = st.checkbox("I agree to the Terms and Conditions")
privacy = st.checkbox("I agree to the Privacy Policy")
refund = st.checkbox("I agree to the Cancellation and Refund Policy")

# Display policy content inline
if terms:
    st.markdown("""
    #### Terms and Conditions
    - Classes are for spiritual and wellness learning only.  
    - No sharing of session content or materials.  
    - Misconduct may result in termination without refund.
    """)

if privacy:
    st.markdown("""
    #### Privacy Policy
    - Your personal data (name, phone) is only used for class-related communication.  
    - We do not share your data with third parties.  
    - Your data is stored securely.
    """)

if refund:
    st.markdown("""
    #### Cancellation and Refund Policy
    - No refunds after registration.  
    - Rescheduling may be provided for genuine reasons (only once).  
    - Organizer-initiated cancellations will be rescheduled.
    """)

# Simulated Payment Button
if st.button("Pay Now (Simulation Only)"):
    if not name or not phone:
        st.warning("Please enter both your name and phone number.")
    elif not (terms and privacy and refund):
        st.warning("Please agree to all the policies before proceeding.")
    else:
        st.success("Thank you! This is a test payment simulation only.")
        st.info("Live payment will be enabled once Razorpay approves the website.")

# Footer
st.markdown("---")
st.markdown("© 2025 Ayushman Bhava | All Rights Reserved  \nContact: ayushmanbhava@gmail.com")
