import streamlit as st

# Streamlit app title
st.title("🧮 Calculator App")

# Input fields for numbers
st.write("### Enter two numbers:")
num1 = st.number_input("Enter first number:", step=1.0, format="%.2f", key="num1")
num2 = st.number_input("Enter second number:", step=1.0, format="%.2f", key="num2")

# Select operation
operation = st.selectbox(
    "Select operation:",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Perform calculation based on the selected operation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed!")

# Display result
if result is not None:
    st.write(f"### Final Result: **{result}**")
