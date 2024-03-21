import streamlit as st

def main():
    st.title("Button Demo")
    
    # Button 1
    button1_state = st.button("Button 1")
    if button1_state:
        st.write("Button 1 is clicked!")
    else:
        st.write("Button 1 is not clicked.")
    
    # Button 2
    button2_state = st.button("Button 2")
    if button2_state:
        st.write("Button 2 is clicked!")
    else:
        st.write("Button 2 is not clicked.")

if __name__ == "__main__":
    main()