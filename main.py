import streamlit as st

page = st.sidebar.radio("Навигация", ["Launch Bundler", "Pump.fun Trader"])

if page == "Launch Bundler":
    st.title("Pump.fun Launch Bundler")

    st.header("Fees:")
    st.write("- Launch + up to 5 buys: 0.1 SOL")
    st.write("- Launch + up to 17 buys: 0.2 SOL")

    st.header("Token Information")
    token_image = st.file_uploader("Token Image*", type=["png", "jpg", "jpeg"])
    token_name = st.text_input("Token Name*")
    token_description = st.text_area("Token Description*")
    token_symbol = st.text_input("Token Symbol*")
    twitter = st.text_input("Twitter (Optional)")
    telegram = st.text_input("Telegram (Optional)")
    website = st.text_input("Website (Optional)")

    st.header("Wallet Private Keys and Buy Amounts* (first wallet = dev) (format= bs58)")
    wallets = st.session_state.get("wallets", [{"key": "", "amount": ""}])

    for i, wallet in enumerate(wallets):
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            wallets[i]["key"] = st.text_input(f"Wallet Private Key {i+1}", value=wallet["key"], key=f"wallet_key_{i}")
        with col2:
            wallets[i]["amount"] = st.text_input(f"Buy Amount (SOL) {i+1}", value=wallet["amount"], key=f"wallet_amount_{i}")
        with col3:
            if st.button(f"Remove {i+1}", key=f"remove_wallet_{i}"):
                wallets.pop(i)
                st.session_state["wallets"] = wallets
                st.experimental_rerun()

    if st.button("Add Wallet", key="add_wallet"):
        wallets.append({"key": "", "amount": ""})
        st.session_state["wallets"] = wallets
        st.experimental_rerun()

    st.header("Mint Private Key")
    mint_private_key = st.text_input("Mint Private Key", key="mint_private_key")

    if st.button("Generate New Mint Key", key="generate_mint_key"):
        st.write("New Mint Key Generated (заглушка)")

    st.header("Coupon Code (optional)")
    coupon_code = st.text_input("Enter coupon code", key="coupon_code")

    st.write("Submit Current fees: 0.05 SOL (+0.01 jito tip)")
    st.write("Want to try it out? Contact us on Telegram for a trial coupon code!")

    if st.button("Submit", key="submit_button"):
        st.write("Data Submitted (заглушка)")

    st.write("Current Wallets:", wallets)
    st.write("Mint Private Key:", mint_private_key)
    st.write("Coupon Code:", coupon_code)

elif page == "Pump.fun Trader":
    st.title("Pump.fun Trader")

    st.header("Fees:")
    st.write("- Buying and Selling 0.01 sol per tx")

    st.header("Notes:")
    st.write("- Sell all can sell a maximum of 20 wallets at a time, adds a 0.01 jito tip fee to the tx")
    st.write("- Fees will be deducted within the transaction so you only pay if it completes")
    st.write("- Wallets filled in the bundler will be shown here")

    st.header("Buying")
    token_mint = st.text_input("Token: Enter mint publickey...", key="buy_token_mint")
    buyer_pvtkey = st.text_input("Buyer pvtkey: Enter private key for buyer...", key="buyer_pvtkey")
    sol_amount = st.number_input("Sol amount: Enter sol amount...", min_value=0.0, step=0.01, key="sol_amount")

    if st.button("Buy", key="buy_button"):
        st.write(f"Buying {sol_amount} SOL of token with mint: {token_mint}")

    st.header("Selling")
    sell_token_mint = st.text_input("Token: Enter mint publickey...", key="sell_token_mint")
    sell_percentage = st.slider("Set Sell Percentage:", 1, 100, key="sell_percentage")

    if st.button("Sell", key="sell_button"):
        st.write(f"Selling {sell_percentage}% of token with mint: {sell_token_mint}")

    if st.button("Sell All (will always sell 100%)", key="sell_all_button"):
        st.write(f"Selling 100% of token with mint: {sell_token_mint}")
