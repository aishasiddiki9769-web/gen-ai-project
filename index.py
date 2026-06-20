import streamlit as st

st.title("BMI Health Calculator")
st.write("Apna weight aur height daalo, apna BMI aur health score jaano!")

weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=60.0)
height_cm = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=165.0)

if st.button("Calculate BMI"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write(f"### Tumhara BMI hai: {bmi:.1f}")

    if bmi < 18.5:
        st.warning("Category: Underweight — thoda weight badhana chahiye.")
    elif bmi < 25:
        st.success("Category: Healthy — bahut badhiya, isi tarah maintain karo!")
    elif bmi < 30:
        st.warning("Category: Overweight — thoda dhyan do diet aur exercise pe.")
    else:
        st.error("Category: Obese — doctor se consult karna sahi rahega.")
