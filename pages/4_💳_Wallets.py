# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Wallet - Polygan Hard Fork ',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳 Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'New_Active_Wallets':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e8898e36-bcca-4920-bc5f-98d7c917eea8/data/latest')
    elif query == 'top10_Wallet_After':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/efb902c0-3144-4748-9020-b734cf84cfbf/data/latest')
    elif query == 'top10_Wallet_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/fea15dd7-d071-4854-82bb-4e2248046c89/data/latest')
    return None


New_Active_Wallets = get_data('New_Active_Wallets')
top10_Wallet_After = get_data('top10_Wallet_After')
top10_Wallet_Before = get_data('top10_Wallet_Before')


df3 = New_Active_Wallets
df4 = top10_Wallet_After
df5 = top10_Wallet_Before

#########################################################################################

st.write(""" ### Crypto Wallet Concept ##  """)

st.write("""
Cryptocurrency wallets store users' public and private keys while providing an easy-to-use interface to manage crypto balances. They also support cryptocurrency transfers through the blockchain. Some wallets even allow users to perform certain actions with their crypto assets such as buying and selling or interacting with decentralised applications (dapps).[[7]](https://crypto.com/university/crypto-wallets#:~:text=Cryptocurrency%20wallets%20store%20users'%20public,cryptocurrency%20transfers%20through%20the%20blockchain.)      

Each wallet in this section represents the individual user who owns it, and active wallets are those that have had one or more transactions in a certain time frame.
  """)


st.info(""" ##### In This Wallet(User) Section you can find: ####


* New Wallets Over time 
* Active Wallets Over time
* Top 10 Wallets Based on Transaction Fees Paid


""")


#########################################################################################

st.write(""" ## New & Active Wallets  ##  """)

interval = st.radio('**Time Interval**',
                    ['Daily', 'Weekly'], key='fees_interval', horizontal=True)


if st.session_state.fees_interval == 'Daily':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["daily", "New Users"], ascending=[
        True, False]), x="daily", y="New Users", color="STATUS", title='Daily New Wallets before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily New Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["daily", "ACTIVE_USER"], ascending=[
        True, False]), x="daily", y="ACTIVE_USER", color="STATUS", title='Daily Active Wallets before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Active Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


elif st.session_state.fees_interval == 'Weekly':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEKLY", "New Users"], ascending=[
        True, False]), x="WEEKLY", y="New Users", color="STATUS", title='Weekly New Wallets before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly New Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEKLY", "ACTIVE_USER"], ascending=[
        True, False]), x="WEEKLY", y="ACTIVE_USER", color="STATUS", title='Weekly Active Wallets before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Active Users')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#############################################################################################################
st.write(""" ##  Top 10 Wallets Based on Transaction Fees Paid """)
c1, c2 = st.columns(2)

with c2:
    # Number of Transaction Pie chart
    fig = px.pie(df4, values="total Fees",
                 names="WALLET", title='After Fork Top 10 Wallet Based  on Transaction Fee Paid', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c1:
    # Number of Transaction Pie chart
    fig = px.pie(df5, values="total Fees",
                 names="WALLET", title='Before Fork Top 10 Wallet Based  on Transaction Fee Paid', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

############################################################################

st.text(" \n")

st.info(""" #### Conclusion: ####

 * 95 percent of whale transactions were transferring- No NFT traded- relatively low stake and swaps
 * Although whales accounted for less than 1 percent of Total transactions, they had average transaction figures 12 times higher than regular users  
 * Number of Whales Transactions rose significantly in the second half of 2022
 * on 14 Feb 2022, the number of transactions rose more than three times its average



""")
