import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# --- Page Config ---
st.set_page_config(page_title="Bio Data & Salary Predictor", layout="centered")

# --- App Title ---
st.title("👤💼 Salary Prediction App")
st.markdown("Fill out the form, and we'll predict your estimated salary based on your experience!")

# --- Create a Form ---
with st.form("bio_form", clear_on_submit=False):
    st.header("📋 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        age = st.number_input("Your Age", 0, 100, 30, 1)

    with col2:
        last_name = st.text_input("Last Name")
        dob = st.date_input("Your Birthday")
        marital_status = st.radio("Marital Status", ["Single", "Married"])

    years_of_experience = st.slider("💼 Years of Experience", 0, 40)
    
    profile_pic = st.file_uploader("📷 Upload Profile Picture", type=["jpg", "png", "jpeg"])

    submitted = st.form_submit_button("Submit")

# --- Handle Form Submission ---
if submitted:
    st.success("✅ Your bio data has been submitted!")

    # Display image if uploaded
    if profile_pic:
        st.image(profile_pic, caption="Profile Picture", width=150)

    # Display formatted bio data
    st.subheader("🧾 Bio Summary")
    st.markdown(f"""
    - *Name:* {first_name} {last_name}  
    - *Gender:* {gender}  
    - *Age:* {age}  
    - *Date of Birth:* {dob.strftime('%B %d, %Y')}  
    - *Marital Status:* {marital_status}  
    - *Years of Experience:* {years_of_experience}  
    """)

    # Save user data to CSV
    user_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Gender": gender,
        "Age": age,
        "Date of Birth": str(dob),
        "Marital Status": marital_status,
        "Years of Experience": years_of_experience
    }

    df = pd.DataFrame([user_data])
    df.to_csv("user_data.csv", mode="a", header=False, index=False)
    st.success("💾 Your data has been saved!")

# --- Salary Prediction Section ---
st.header("📈 Predict Your Salary")

# Sample training data
salary_data = pd.DataFrame({
    "Years of Experience": [1, 3, 5, 7, 10, 12, 15, 18, 20],
    "Salary": [30000, 45000, 60000, 90000, 105000, 120000, 135000, 150000, 175000]
})

model = LinearRegression()
X = salary_data[["Years of Experience"]]
y = salary_data["Salary"]
model.fit(X, y)

if st.button("Predict Salary"):
    predicted_salary = model.predict(np.array([[years_of_experience]]))[0]
    st.success(f"💰 Estimated Salary: *${predicted_salary:,.2f}*")