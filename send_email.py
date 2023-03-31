import smtplib, ssl
import os
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"  # specifically for a gmail account.
    port = 465  # standard port
    username = "donnacha.mcgrath2@gmail.com"
    # Note: password is obtained from your gmail account. Security - two factor - app passwords.
    # try:
    password = os.getenv("PASSWORD")  # access the environment variable password is in.
    # except:
    #     password = st.secrets["PASSWORD"]
    receiver = "donnacha.mcgrath2@gmail.com"
    context = ssl.create_default_context()  # variable holds context for sending emails securely.

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
