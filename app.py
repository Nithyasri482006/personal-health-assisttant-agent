import streamlit as st
from agent import ask_health_question

st.set_page_config(
    page_title="Personal Health Assistant",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Personal Health Assistant Agent")

menu = st.sidebar.selectbox(
    "Choose a Feature",
    [
        "Home",
        "Health Q&A",
        "BMI Calculator",
        "Water Intake Calculator",
        "Medicine Reminder",
        "Daily Health Tips",
        "Health Risk Checker",
        "Food Suggestions"
    ]
)

if menu == "Home":
    st.markdown("""
    ## Welcome 👋

    This AI-powered Personal Health Assistant helps you manage your daily health.

    ### Available Features

    - 🤖 Health Q&A
    - ⚖️ BMI Calculator
    - 💧 Water Intake Calculator
    - 💊 Medicine Reminder
    - 🍎 Daily Health Tips
    - 🩺 Health Risk Checker
    - 🥗 Food Suggestions
    """)

elif menu == "BMI Calculator":
    st.header("⚖️ BMI Calculator")

    weight = st.number_input("Enter your weight (kg)", min_value=1.0)

    height = st.number_input("Enter your height (meters)", min_value=0.1)

    if st.button("Calculate BMI"):

        bmi = weight / (height ** 2)

        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.info("Category: Underweight")
        elif bmi < 25:
            st.success("Category: Normal Weight")
        elif bmi < 30:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")

elif menu == "Water Intake Calculator":
    st.header("💧 Water Intake Calculator")

    weight = st.number_input("Enter your weight (kg)", min_value=1.0, key="water")

    if st.button("Calculate Water Intake"):

        water = weight * 35 / 1000

        st.success(f"You should drink approximately {water:.2f} liters of water per day.")
elif menu == "Medicine Reminder":
    st.header("💊 Medicine Reminder")

    medicine = st.text_input("Enter Medicine Name")

    reminder_time = st.time_input("Select Reminder Time")

    if st.button("Set Reminder"):

        st.success(
            f"✅ Reminder Set!\n\nTake **{medicine}** at **{reminder_time.strftime('%I:%M %p')}**."
        )

elif menu == "Daily Health Tips":
    st.header("🍎 Daily Health Tips")

    import random

    health_tips = [
        "🥗 Eat more fruits and vegetables every day.",
        "💧 Drink at least 2 liters of water daily.",
        "🏃 Exercise for at least 30 minutes every day.",
        "😴 Get 7–8 hours of quality sleep.",
        "🚭 Avoid smoking and excessive alcohol consumption.",
        "🧘 Practice meditation or yoga to reduce stress.",
        "🚶 Take short walking breaks if you sit for long hours.",
        "🍽️ Avoid junk food and eat balanced meals."
    ]

    if st.button("Get Health Tip"):
        tip = random.choice(health_tips)
        st.success(tip)
elif menu == "Health Risk Checker":
    st.header("🩺 Health Risk Checker")

    age = st.number_input("Enter your Age", min_value=1, max_value=100)

    smoker = st.selectbox(
        "Do you smoke?",
        ["No", "Yes"]
    )

    exercise = st.selectbox(
        "Do you exercise regularly?",
        ["Yes", "No"]
    )

    if st.button("Check Health Risk"):

        if age >= 50 or smoker == "Yes" or exercise == "No":
            st.warning("⚠️ Health Risk: Moderate to High")
            st.write("### Recommendation")
            st.write("• Exercise regularly")
            st.write("• Eat a balanced diet")
            st.write("• Drink enough water")
            st.write("• Visit your doctor for regular check-ups")
        else:
            st.success("✅ Health Risk: Low")
            st.write("### Recommendation")
            st.write("Keep maintaining your healthy lifestyle! 🎉")
elif menu == "Food Suggestions":
    st.header("🥗 Food Suggestions")

    goal = st.selectbox(
        "Select your health goal",
        [
            "Weight Loss",
            "Weight Gain",
            "Healthy Diet"
        ]
    )

    if st.button("Get Food Suggestions"):

        if goal == "Weight Loss":
            st.success("""
🥗 Recommended Foods:
- Green vegetables
- Fruits
- Oats
- Grilled chicken
- Brown rice
""")

        elif goal == "Weight Gain":
            st.success("""
🍚 Recommended Foods:
- Milk
- Eggs
- Rice
- Nuts
- Peanut butter
""")

        elif goal == "Healthy Diet":
            st.success("""
🥦 Recommended Foods:
- Fresh vegetables
- Fruits
- Whole grains
- Fish
- Yogurt
""")
elif menu == "Health Q&A":
    st.header("🤖 AI Health Q&A")

    user_question = st.text_area("Ask your health-related question:")

    if st.button("Get AI Answer"):

        if user_question.strip() == "":
            st.warning("Please enter a question.")

        else:
            with st.spinner("Thinking..."):
                answer = ask_health_question(user_question)

            st.success("AI Response")
            st.write(answer)