import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Ayushman Bhava", layout="centered")

BACKEND_URL = "https://ayush-backend-production-29e4.up.railway.app"
RAZORPAY_KEY_ID = "rzp_live_gvdyaC1uttFnEa"

# Title and Header
st.title("Ayushman Bhava")
st.markdown("### Learn Meditation & Kriya Yoga from the Enlightened Teacher.")

# Testimonials
st.markdown("## 🧘‍♂ Student Experiences")
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
earned him the reverence of being called the \"Master of Masters.\"
""")

# Class Selection
st.markdown("## 💸 Join the Class")
st.write("Choose your mode of class and proceed to payment.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🌐 Online Yoga Class")
    st.markdown("\u20b9999")
with col2:
    st.markdown("### 🏡 Offline Yoga Class")
    st.markdown("\u20b9799")

option = st.radio("Select Class Type", ("Online Class - ₹999", "Offline Class - ₹999"))
name = st.text_input("Enter your name")
phone = st.text_input("Enter your phone number")

# Policy Agreement
st.markdown("### 📋 Please agree to the following policies to continue:")
terms = st.checkbox("I agree to the Terms and Conditions")
privacy = st.checkbox("I agree to the Privacy Policy")
refund = st.checkbox("I agree to the Cancellation and Refund Policy")

amount = 99900 if "Online" in option else 99900
description = option

if st.button("Pay Now"):
    if not name or not phone:
        st.warning("Please enter both your name and phone number.")
    elif not (terms and privacy and refund):
        st.warning("Please agree to all the policies before proceeding.")
    else:
        try:
            response = requests.post(f"{BACKEND_URL}/create_order", json={
                "amount": amount,
                "name": name,
                "phone": phone,
                "description": description
            })
            if response.status_code == 200:
                redirect_url = response.json()["redirect_url"]
                st.markdown(f"""
                    <meta http-equiv="refresh" content="0; url={BACKEND_URL}{redirect_url}">
                    <h3>Redirecting to Razorpay...</h3>
                """, unsafe_allow_html=True)
            else:
                st.error("Failed to create order. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Policies
st.markdown("""
#### Terms and Conditions
- Classes are for spiritual and wellness learning only.  
- No sharing of session content or materials.  
- Misconduct may result in termination without refund.
""")

st.markdown("""
#### Privacy Policy
- Your personal data (name, phone) is only used for class-related communication.  
- We do not share your data with third parties.  
- Your data is stored securely.
""")

st.markdown("""
#### Cancellations and Refunds
- Refunds are accepted within 7 working days of registration.  
- After 7 days, rescheduling may be provided for genuine reasons (only once).  
- Organizer-initiated cancellations will be rescheduled or fully refunded.
""")

# Footer
st.markdown("---")
st.markdown("© 2025 Ayushman Bhava | All Rights Reserved  \nContact: ayushmanbhava.help@gmail.com")
