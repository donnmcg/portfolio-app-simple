import streamlit as st
from send_email import send_email

st.header("Contact Me")

# Create a form for the web user to contact us on
with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email address")  # place to input your email
    raw_message = st.text_area("Your message")  # allows multiline text input for an email-like message
    message = f"""\
Subject: Contact Us Page {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")  # submit form button
    if button:
        send_email(message)
        st.info("Your message was sent successfully")
