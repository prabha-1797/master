import streamlit as st

# Set page config
st.set_page_config(page_title="Master of Masters", layout="centered")

# Title and Image
st.title("Ayushman Bhava")
st.markdown("### Learn Meditation & Kriya Yoga from the Enlightened Guide")
st.image("https://via.placeholder.com/300", caption="B. Venkateshwar Rao", use_container_width=False)

# YouTube testimonials section
st.markdown("## 🧘‍♂️ Student Experiences")
with st.container():
    st.markdown("""
    <iframe width="100%" height="315" src="https://www.youtube.com/embed/rCl1wvD479Y?si=l-GK3Nr_b-3jIUUm" 
    title="YouTube video" frameborder="0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# About section
st.markdown("## 🙏 About the Yoga Teacher")
st.write("""
B. Venkateshwar Rao is a seasoned master in the fields of Meditation and Kriya Yoga Sadhana. 
With decades of spiritual dedication and transformative experiences, he has guided hundreds 
towards inner peace and true consciousness. His unique energy and divine understanding have 
earned him the reverence of being called the "Master of Masters."
""")

# Pricing & Payment (Dummy Mode)
st.markdown("## 💸 Join the Class")
st.write("Choose your mode of class and proceed (simulated).")

option = st.radio("Select Class Type", ("Online Class - ₹999", "Offline Class - ₹799"))

name = st.text_input("Enter your name")
phone = st.text_input("Enter your phone number")

# Terms and conditions checkboxes
st.markdown("### 📋 Agreements")

terms = st.checkbox("I agree to the [Terms and Conditions](#terms)", help="You must agree to the terms to proceed.")
cancellation = st.checkbox("I understand the [Cancellations and Refunds](#cancellation-policy)", help="Please confirm you’ve read the cancellation policy.")
privacy = st.checkbox("I agree to the [Privacy Policy](#privacy-policy)", help="Your data will be handled with care.")

# Payment simulation
if st.button("Pay Now (Simulation Only)"):
    if not (name and phone):
        st.warning("Please enter both name and phone number.")
    elif not (terms and cancellation and privacy):
        st.warning("Please agree to all the terms to proceed.")
    else:
        st.success("Thank you! This is a test payment simulation only.")
        st.info("Live payment will be enabled once Razorpay approves the website.")

# Terms content
st.markdown("""
---
## 📄 Terms and Conditions
- The classes are intended for spiritual and wellness development only.
- Sharing of session content or links is strictly prohibited.
- Misconduct during classes (online/offline) may result in termination without refund.

## 🔄 Cancellations and Refunds
- No refunds will be provided after registration.
- In case of technical issues or cancellation from the organizer, rescheduling will be offered.
- If you are unable to attend, please inform 24 hours in advance for rescheduling eligibility (only once).

## 🔐 Privacy Policy
- Your personal data (name, phone) will only be used for class communication purposes.
- We do not share your information with third-party vendors or marketing agencies.
- All data is stored securely and used in accordance with applicable privacy laws.
""")

# Footer
st.markdown("""
---
<center>
    © 2025 Ayushman Bhava | All Rights Reserved  \n
    Contact: ayushmanbhava@gmail.com
</center>
""", unsafe_allow_html=True)
