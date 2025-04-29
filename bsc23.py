import streamlit as st
from datetime import date

# Initialize or load recharge ledger
if "recharge_ledger" not in st.session_state:
    st.session_state.recharge_ledger = {}

# Function to add or update recharge record
def add_recharge(user_name, amount, recharge_date):
    if user_name not in st.session_state.recharge_ledger:
        st.session_state.recharge_ledger[user_name] = []

    recharge = {
        "amount": amount,
        "date": recharge_date
    }
    st.session_state.recharge_ledger[user_name].append(recharge)
    st.success(f"Recharge added for {user_name} on {recharge_date} of amount ₹{amount}.")

# Streamlit UI
st.title("📱 Mobile Recharge Ledger")

st.subheader("➕ Add a Recharge Record")
user_name = st.text_input("User Name")
amount = st.number_input("Recharge Amount (₹)", min_value=0)
recharge_date = st.date_input("Recharge Date", value=date.today())

if st.button("Add Recharge"):
    if user_name and amount:
        add_recharge(user_name, amount, str(recharge_date))
    else:
        st.warning("Please fill in all fields.")

# Display Recharge Ledger
st.subheader("📒 Recharge Ledger")

if st.session_state.recharge_ledger:
    for user, recharges in st.session_state.recharge_ledger.items():
        st.markdown(f"### User: {user}")
        for rec in recharges:
            st.write(f"- Amount: ₹{rec['amount']}, Date: {rec['date']}")
else:
    st.info("No recharge records yet.")
