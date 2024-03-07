import streamlit as st

# Dictionary containing email and password pairs
a = {
    "FE23AI001@gmail.com": "12345",
    "FW23AI001@gmail.com": "12345",
    "FE23AI002@gmail.com": "12345",
    "FS23AI001@gmail.com": "12345"
}

email = st.text_input('Enter email - ')
password = st.text_input('Enter Password - ', type='password')  # Password field
btn = st.button('Login')

if btn:
    if email in a and password == a[email]:  # Check if email exists as a key and password matches
        st.balloons()
        st.success("Logged In ")
    else:
        st.error('Login Failed')
