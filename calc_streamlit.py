import streamlit as st
from calc_backend import add_number, subtract_number, divide_number, square_root

st.set_page_config(page_title="Basic Calculator", page_icon="🧮")
st.title("Basic Calculator by Jhalak")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

if st.button("Calculate"):
    st.subheader("Results")
    st.write(f"Addition: {add_number(num1, num2)}")
    st.write(f"Subtraction: {subtract_number(num1, num2)}")

    try:
        st.write(f"Division: {divide_number(num1, num2)}")
    except ValueError as e:
        st.write(f"Division: {e}")


    st.write(f"Square root of first number: {square_root(num1)}")

