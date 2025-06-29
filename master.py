import streamlit as st
import smtplib
import razorpay
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(page_title="Ayushman Bhava", layout="centered")

# Razorpay keys (replace with actual keys in production)
RAZORPAY_KEY_ID = "rzp_test_eT9lCdOnYfweo9"
RAZORPAY_KEY_SECRET = "1BIW3EN9r4igx1VvKirXnABf"

# Email credentials
EMAIL = "teja230704@gmail.com"
APP_PASSWORD = "hsim nlcm byyk mkuw"
MASTER_EMAIL = "prabhavathigunda2@gmail.com"

# Razorpay client
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

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

if st.markdown("<style>div.stButton > button {width: 100%; font-size: 18px; padding: 12px; background-color: #f37254; color: white;}</style>", unsafe_allow_html=True):
    pass

if st.button("Pay Now"):
    if not name or not phone:
        st.warning("Please enter both your name and phone number.")
    elif not (terms and privacy and refund):
        st.warning("Please agree to all the policies before proceeding.")
    else:
        try:
            # Create Razorpay order
            order = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture": "1"
            })

            st.markdown("### 🔒 Payment Gateway")
            st.markdown(f"""
            <form action="https://checkout.razorpay.com/v1/checkout.js" method="POST">
                <script
                    src="https://checkout.razorpay.com/v1/checkout.js"
                    data-key="{RAZORPAY_KEY_ID}"
                    data-amount="{amount}"
                    data-currency="INR"
                    data-order_id="{order['id']}"
                    data-buttontext="Pay Now"
                    data-name="Ayushman Bhava"
                    data-description="{option}"
                    data-prefill.name="{name}"
                    data-prefill.contact="{phone}"
                    data-theme.color="#F37254"
                ></script>
            </form>
            """, unsafe_allow_html=True)

            # Send confirmation email
            msg = MIMEMultipart()
            msg['From'] = EMAIL
            msg['To'] = MASTER_EMAIL
            msg['Subject'] = "New Course Enrollment Notification"

            body = f"""
            A new user has enrolled in: {option}
            Name: {name}
            Phone: {phone}
            Payment Amount: ₹{amount // 100}
            """
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL, APP_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL, MASTER_EMAIL, text)
            server.quit()

            st.success("Confirmation email sent to Ayushman Bhava.")

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
