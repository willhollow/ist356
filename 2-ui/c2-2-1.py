import streamlit as st

st.title("Area and Perimeter Calculator")

length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step=0.1)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, step=0.1)

# Add calculate and clear buttons
calculate_button = st.button("Calculate")
clear_button = st.button("Clear")

# When Calculate button is clicked, compute area and perimeter
if calculate_button:
    area = length * width
    perimeter = 2 * (length + width)
    
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")

# When clear button is clicked, reset the inputs and outputs
if clear_button:
    st.experimental_rerun()
    
