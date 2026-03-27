import streamlit as st
from utils import predict
from url_checker import check_url
from explain import explain_text
from database import save_data, get_history
import pandas as pd

st.set_page_config(page_title="Fraud Detection System", page_icon="🛡️")

st.title("🛡️ AI-Powered Phishing & Fraud Detection System")

# UI styling
st.markdown("""
<style>
.stTextArea textarea {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

option = st.selectbox("Choose Input Type", ["Text", "URL"])

user_input = st.text_area("Enter input")

if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter some input")
    
    else:
        if option == "Text":
            result, confidence = predict(user_input)

            if result == 1:
                st.error("⚠️ Fraud Detected")
            else:
                st.success("✅ Safe Message")

            # Confidence Score
            st.write(f"📊 Confidence: {round(confidence * 100, 2)}%")

            # Explanation
            explanation = explain_text(user_input)

            if explanation:
                st.write("🔍 Reasons:")
                for word in explanation:
                    st.write(f"• {word}")
            else:
                st.write("🔍 No suspicious keywords found")

            save_data(user_input, str(result))

        else:
            result = check_url(user_input)

            if result == "Dangerous":
                st.error("⚠️ Dangerous URL")
            elif result == "Suspicious":
                st.warning("⚠️ Suspicious URL")
            else:
                st.success("✅ Safe URL")

            save_data(user_input, result)

# 📜 History
if st.checkbox("📜 Show History"):
    history = get_history()

    if history:
        st.subheader("Previous Results")

        for item in history[::-1]:
            st.write(f"🔹 Input: {item[0]}")
            st.write(f"➡️ Result: {item[1]}")
            st.write("---")
    else:
        st.write("No history found")

# 📊 Dashboard
if st.checkbox("📊 Show Statistics"):
    history = get_history()

    if history:
        df = pd.DataFrame(history, columns=["Input", "Result"])
        st.subheader("Detection Summary")
        st.bar_chart(df["Result"].value_counts())
    else:
        st.write("No data for statistics")