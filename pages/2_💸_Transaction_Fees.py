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
st.set_page_config(page_title='Transactions Fees - Polygan Hard Fork ',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌌Transactions Fees')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Overview_After':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6164fe51-8f89-438d-9c65-8358ec4fc541/data/latest')
    elif query == 'Overview_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f4384d86-9743-4b11-be24-8a93bbafb333/data/latest')
    elif query == 'Daily_Transaction':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/59a8d1ec-2c8c-469c-8d9d-e9e6de66b3c2/data/latest')
    elif query == 'Comparison_After':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c82fec67-e4b1-40eb-85f5-43101727ee4b/data/latest')
    elif query == 'Comparison_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1ba973f4-6d84-44ae-995b-f310ce0c4182/data/latest')
    elif query == 'HeatMap_After':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3fbb3196-46ec-48eb-a750-5ed37ab48532/data/latest')
    elif query == 'HeatMap_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e9e1f2f2-7d01-43fc-b170-ce953042d080/data/latest')
    return None


Overview_After = get_data('Overview_After')
Overview_Before = get_data('Overview_Before')
Daily_Transaction = get_data('Daily_Transaction')
Comparison_After = get_data('Comparison_After')
Comparison_Before = get_data('Comparison_Before')
HeatMap_After = get_data('HeatMap_After')
HeatMap_Before = get_data('HeatMap_Before')
D_TX_type = get_data('D_TX_type')
D_Fee_Type = get_data('D_Fee_Type')


df = Overview_After
df2 = Overview_Before
df3 = Daily_Transaction
df4 = Comparison_After
df5 = Comparison_Before
df6 = HeatMap_After
df7 = HeatMap_Before
######################################################################################################################


st.write(""" ### Gas Fee Concept ##  """)

st.write("""
Mathematically, transaction fees are the difference between the amount of cryptocurrency sent and the amount received. Conceptually, transaction fees are a reflection of the speed with which a user wants their transaction validated on the blockchain. Gas is the fee required to successfully conduct a transaction or execute a contract on the blockchain platforms. Fees are priced in tiny fractions of the cryptocurrency. Gas is used to pay validators for the resources needed to conduct transactions.The exact price of the gas is determined by supply, demand, and network capacity at the time of the transaction.[[5]](https://www.investopedia.com/terms/g/gas-ethereum.asp#:~:text=Gas%20is%20the%20fee%20required,resources%20needed%20to%20conduct%20transactions.)    
Has Polygan's software change resulted in reduced gas fees as hoped? This section aims to answer that question.
  """)


st.info(""" ##### In This Transaction Fee Section you can find: ####

 * Transaction Fee Before and After Fork Overview
 * Transaction Fee Over time [Daily-Weekly] 
 * Gas Used Over time [Daily-Weekly] 
 * Share of each Transaction Type on Transaction Fee
 * Transaction Fee HeatMaps 



""")


#####################################################################################
st.text(" \n")
st.text(" \n")
st.write(""" ## Transaction Fee Before and After Fork Overview """)

c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Fork""")
    st.metric(label='**Total Fees**',
              value=str(df2["Total Fees"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Gas Used**',
              value=str(df2["Total Gas Used"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Gas Used**',
              value=str(df2["AVG Gas Used"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Fees [USD]**',
              value=str(df2["Total Fees-USD"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average FEE per block**',
              value=df2["Avg FEE per block"].map('{:,.0f}'.format).values[0])
    st.metric(label='**MAX Fee**',
              value=df2["MAX Fee"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction Fee**',
              value=df2["AVG Fee"].map('{:,.4f}'.format).values[0])


with c2:
    st.write(""" #### After Fork """)
    st.metric(label='**Total Fees**',
              value=str(df["Total Fees"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Gas Used**',
              value=str(df["Total Gas Used"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Gas Used**',
              value=str(df["AVG Gas Used"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Fees [USD]**',
              value=str(df["Total Fees-USD"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average FEE per block**',
              value=df["Avg FEE per block"].map('{:,.0f}'.format).values[0])
    st.metric(label='**MAX Fee**',
              value=df["MAX Fee"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction Fee**',
              value=df["AVG Fee"].map('{:,.4f}'.format).values[0])


st.text(" \n")
st.write(""" ## Transaction Fee Over Time """)


interval = st.radio('**Time Interval**',
                    ['Daily', 'Weekly'], key='fees_interval', horizontal=True)


if st.session_state.fees_interval == 'Daily':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "TOTAL_FEES_OVER_TIME"], ascending=[
        True, False]), x="DATE", y="TOTAL_FEES_OVER_TIME", color="STATUS", title='Daily Transaction Fees before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Transaction Fees')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "TOTAL_GAS_USED_OVER_TIME"], ascending=[
        True, False]), x="DATE", y="TOTAL_GAS_USED_OVER_TIME", color="STATUS", title='Daily Gase Used before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Gas Used')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "AVG_FEES_OVER_TIME"], ascending=[
        True, False]), x="DATE", y="AVG_FEES_OVER_TIME", color="STATUS", title='Daily Average Transacton Fee before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily AVG TX Fee')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


elif st.session_state.fees_interval == 'Weekly':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "TOTAL_FEES_OVER_TIME"], ascending=[
        True, False]), x="WEEK", y="TOTAL_FEES_OVER_TIME", color="STATUS", title='Weekly Transaction Fees before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transaction Fee')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "TOTAL_GAS_USED_OVER_TIME"], ascending=[
        True, False]), x="WEEK", y="TOTAL_GAS_USED_OVER_TIME", color="STATUS", title='Weekly  Gase Used before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Gas Used')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "AVG_FEES_OVER_TIME"], ascending=[
        True, False]), x="WEEK", y="AVG_FEES_OVER_TIME", color="STATUS", title='Weekly Average Transacton Fee before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly AVG TX Fee')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#############################################################################################################
st.text(" \n")
st.write(""" ## Share of each Transaction Type on Transaction Fee """)
c1, c2 = st.columns(2)

with c2:
    # Number of Transaction Pie chart
    fig = px.pie(df4, values="total Fees",
                 names="ACTION", title='After Fork Total Transaction diffrent Action Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c1:
    # Number of Transaction Pie chart
    fig = px.pie(df5, values="total Fees",
                 names="ACTION", title='Before Fork Total Transaction diffrent Action Comparison', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

############################################################################


st.write(""" ## Transaction Fee HeatMaps """)


c1, c2 = st.columns(2)

with c1:
    st.write(""" #### Before Fork""")
    # "transactions per minute on hour of day (UTC)"
    fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Gas Used per minute on hour of day (UTC)",
                             histfunc='avg', title="Gas Used per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Transaction Fees per minute on hour of day (UTC)",
                             histfunc='avg', title="Transaction Fees per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    st.write(""" #### After Fork""")
    # "transactions per minute on hour of day (UTC)"
    fig = px.density_heatmap(df6, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Gas Used per minute on hour of day (UTC)",
                             histfunc='avg', title="Gas Used per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df6, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Transaction Fees per minute on hour of day (UTC)",
                             histfunc='avg', title="Transaction Fees per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#############################################################################
st.text(" \n")

st.info(""" #### Conclusion: ####

 * 95 percent of whale transactions were transferring- No NFT traded- relatively low stake and swaps
 * Although whales accounted for less than 1 percent of Total transactions, they had average transaction figures 12 times higher than regular users  
 * Number of Whales Transactions rose significantly in the second half of 2022
 * on 14 Feb 2022, the number of transactions rose more than three times its average



""")
