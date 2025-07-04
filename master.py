import streamlit as st
import requests
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(page_title="Ayushman Bhava", layout="centered")

BACKEND_URL = "https://ayush-backend-production-29e4.up.railway.app"  # Change to deployed backend URL
RAZORPAY_KEY_ID = "rzp_test_eT9lCdOnYfweo9"  # Public key only for checkout

# Title and Header
st.title("Ayushman Bhava")
st.markdown("### Learn Meditation & Kriya Yoga from the Enlightened Teacher.")

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
earned him the reverence of being called the \"Master of Masters.\"
""")

# Class Selection
st.markdown("## 💸 Join the Class")
st.write("Choose your mode of class and proceed to payment.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🌐 Online Yoga Class")
    st.markdown("₹999")
with col2:
    st.markdown("### 🏡 Offline Yoga Class")
    st.markdown("₹799")

option = st.radio("Select Class Type", ("Online Class - ₹999", "Offline Class - ₹799"))
name = st.text_input("Enter your name")
phone = st.text_input("Enter your phone number")

# Checkboxes for policies
st.markdown("### 📋 Please agree to the following policies to continue:")
terms = st.checkbox("I agree to the Terms and Conditions")
privacy = st.checkbox("I agree to the Privacy Policy")
refund = st.checkbox("I agree to the Cancellation and Refund Policy")

amount = 99900 if "Online" in option else 79900

description = option

if st.markdown("<style>div.stButton > button {width: 100%; font-size: 18px; padding: 12px; background-color: #f37254; color: white;}</style>", unsafe_allow_html=True):
    pass

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
                order_id = response.json()["order_id"]

                st.markdown("### 🔒 Payment Gateway")
                html(f"""
    <button id="rzp-button" style="
        background-color: #f37254;
        color: white;
        padding: 14px 28px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        cursor: pointer;">
        Pay securely through razorpay ₹{amount // 100} Now
    </button>

    <script src="https://checkout.razorpay.com/v1/checkout.js"></script>
    <script>
        var options = {{
            "key": "{RAZORPAY_KEY_ID}",
            "amount": "{amount}",
            "currency": "INR",
            "name": "Ayushman Bhava",
            "description": "{description}",
            "order_id": "{order_id}",
            "prefill": {{
                "name": "{name}",
                "contact": "{phone}"
            }},
            "theme": {{
                "color": "#F37254"
            }},
            "modal": {{
                "ondismiss": function() {{
                    console.log("Checkout form closed");
                }}
            }}
        }};

        var rzp = new Razorpay(options);
        document.getElementById('rzp-button').onclick = function(e) {{
            rzp.open();
            e.preventDefault();
        }};
    </script>
""", height=100)

            else:
                st.error("Failed to create order. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Policy Sections
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
st.markdown("© 2025 Ayushman Bhava | All Rights Reserved  \nContact: ayushmanbhava@gmail.com")
