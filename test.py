import streamlit as st 
import pandas as pd
import streamlit_authenticator as sat 
import re

userDetails = pd.DataFrame(columns = ["Username", "Email", "Password"])

def unameval(uname):
    return bool(re.match(r"^[a-zA-Z0-9_-]{1, 20}$", uname))

def emailval(email):
    return "@" in email and 2 < len(email) < 320 and bool(re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2, 7}\b", email))

def pwordval(pword):
    return 8 < len(pword) < 20 and bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", pword))

def register():
    with st.form("register_form"):
        uname = st.text_input("Username")
        pword = st.text_input("Password", type = "password")
        email = st.text_input("Email")
        submit = st.form_submit_button("Register")

        if submit:
            if (unameval(uname) and emailval(email) and pwordval(pword)):
                userDetails = userDetails.append({"Username": uname, "Email": email, "Password": pword}, ignore_index = True)
            
            else:
                st.write("Please re-enter your details.")
    
    return uname, pword, email

def login():
    with st.form("login_form"):
        uname = st.text_input("Username")
        pword = st.text_input("Password", type = "password")
        submit = st.form_submit_button("Login")

        if submit:
            if uname in userDetails["Username"].values:
                user = userDetails[userDetails["Username"] == uname].iloc[0]

                if user["Password"] == pword:
                    st.write("Welcome back!")
                    return True
                
                else:
                    st.write("Incorrect password entered.")

            else:
                st.write("Username not found. Please register before continuing.")
        
        return False

def main():
    st.title("Login/Register")

    if not login():
        uname, pword, email = register()

        if uname and pword and email:
            global userDetails
            userDetails = userDetails.append({"Username": uname, "Email": email, "Password": pword}, ignore_index = True)



#with st.form("login_form"):
#    uname = st.text_input("Username")
#    pword = st.text_input("Password", type="password")    
#    submit = st.form_submit_button("Submit")

#    if submit:

#        if uname not in userDetails:
#            st.write("Username not found. Please register before continuing.")
#            st.write("Please enter email and name to register.")
#            email = st.text_input("Email")
#            name = st.text_input("Name")
#            submit2 = st.form_submit_button("Register")

#            if submit2:
#                if unameval(uname) and emailval(email) and nameval(name) and pwordval(pword):
#                    userDetails = userDetails.append({"Username": uname, "Email": email, "Password": pword}, ignore_index=True)
                
#                else:
#                    st.write("Please re-enter your details.")
        
#        else:
#            st.write("Welcome back!")
#            st.write(userDetails[uname])


main()