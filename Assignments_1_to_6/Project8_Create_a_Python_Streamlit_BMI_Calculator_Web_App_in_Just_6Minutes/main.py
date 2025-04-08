'''
BMI Calculator
Ask for the user's weight and height.
Display the result with a BMI category.


'''
import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to convert pounds to kilograms
def pounds_to_kg(pounds):
    return pounds * 0.453592

# Function to convert inches to meters
def inches_to_meters(inches):
    return inches * 0.0254

# Streamlit app
def app():
    st.title("BMI Calculator")

    st.write("Enter your weight and height to calculate your BMI:")

    # Weight input
    weight_unit = st.selectbox("Select weight unit:", ["Kilograms (kg)", "Pounds (lbs)"])
    weight = st.number_input(f"Weight ({weight_unit}):", min_value=1.0, step=0.1)

    # Height input
    height_unit = st.selectbox("Select height unit:", ["Meters (m)", "Centimeters (cm)", "Inches (in)"])
    if height_unit == "Meters (m)":
        height = st.number_input("Height (in meters):", min_value=0.1, step=0.01)
    elif height_unit == "Centimeters (cm)":
        height = st.number_input("Height (in centimeters):", min_value=1.0, step=0.1) / 100  # Convert to meters
    elif height_unit == "Inches (in)":
        height = st.number_input("Height (in inches):", min_value=1.0, step=0.1) * 0.0254  # Convert to meters

    # Convert weight to kilograms if necessary
    if weight_unit == "Pounds (lbs)":
        weight = pounds_to_kg(weight)

    # Calculate BMI when inputs are valid
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")

        # BMI categories
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Please enter valid weight and height.")

# Run the app
if __name__ == "__main__":
    app()