import streamlit as st

# Set page config
st.set_page_config(page_title="Master of Masters", layout="centered")

# Title and Image
st.title("Master of Masters My Dear God Master")
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

if st.button("Pay Now (Simulation Only)"):
    if name and phone:
        st.success("Thank you! This is a test payment simulation only.")
        st.info("Live payment will be enabled once Razorpay approves the website.")
    else:
        st.warning("Please enter both name and phone number.")

# Footer
st.markdown("""
---
<center>
    © 2025 Master of Masters My Dear God Master | All Rights Reserved  \n
    Contact: masterofmastersmydeargodmaster@gmail.com
</center>
""", unsafe_allow_html=True)
