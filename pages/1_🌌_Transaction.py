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
st.set_page_config(page_title='Transactions - Polygan Hard Fork ',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌌Transactions')

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
    elif query == 'overview2_after':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6fd4bc1b-eb0c-466e-bc65-d0e55401c968/data/latest')
    elif query == 'overview2_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5ff1083b-0a20-4d50-9eb2-98a085b734cc/data/latest')
    return None


Overview_After = get_data('Overview_After')
Overview_Before = get_data('Overview_Before')
Daily_Transaction = get_data('Daily_Transaction')
Comparison_After = get_data('Comparison_After')
Comparison_Before = get_data('Comparison_Before')
HeatMap_After = get_data('HeatMap_After')
HeatMap_Before = get_data('HeatMap_Before')
overview2_after = get_data('overview2_after')
overview2_Before = get_data('overview2_Before')


df = Overview_After
df2 = Overview_Before
df3 = Daily_Transaction
df4 = Comparison_After
df5 = Comparison_Before
df6 = HeatMap_After
df7 = HeatMap_Before
df8 = overview2_after
df9 = overview2_Before
######################################################################################################################


st.write(""" ### Crypto Transaction Concept ##  """)

st.write("""
Cryptocurrency transaction is a transfer of information made between blockchain addresses. These transfers have to be signed with a private key that corresponds to its address. Signed transactions are broadcast to the network of nodes, active computers that follow a specific set of rules to validate transactions and blocks. Valid transactions need to be confirmed by being included in blocks through the mining process.[[4]](https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/)   
This section contains data on on-chain transactions that were made 34 days after the fork (the total number of days the fork has been in operation since it was employed) and 34 days prior to the fork.

  """)


st.info(""" ##### In This Transaction Section you can find: ####

 * Transaction Before and After Fork in a Glance
 * Transactions Over time [Daily-Weekly]  
 * Blocks Over time [Daily-Weekly]  
 * Comparing Transaction Types Before and After the Fork
 * Transaction Heatmaps Before and After



""")


#####################################################################################
st.text(" \n")
st.text(" \n")
st.write(""" ## Transaction Before and After Fork in a Glance """)

st.write(""" While the average transaction per block climbed from 76 to 79 after the Fork deployment, the overall number of transactions decreased by roughly 1%.



  """)
c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Fork""")
    st.metric(label='**Total Transactions**',
              value=str(df2["Total Transactions"].map('{:,.0f}'.format).values[0]))

    st.metric(label='**Total Blocks**',
              value=df2["Total Blocks"].map('{:,.0f}'.format).values[0])

    st.metric(label='**Average Daily Transaction**',
              value=df2["Avg Daily Transactions"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction per Block**',
              value=df9["TPB"].map('{:,.0f}'.format).values[0])


with c2:
    st.write(""" #### After Fork """)
    st.metric(label='**Total Transactions**',
              value=str(df["Total Transactions"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Blocks**',
              value=df["Total Blocks"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Daily Transaction**',
              value=df["Avg Daily Transactions"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Average Transaction per Block**',
              value=df8["TPB"].map('{:,.0f}'.format).values[0])

st.text(" \n")
st.write(""" ## Transaction Over Time """)

st.write(""" The market did not experience any hype following the implementation of Fork, and the number of transactions was essentially unchanged for the first week following January 17; however, we did observe a modest decline in the second week of February, which may not have been related to the implementation of Fork. The average number of transactions per block increased as a result of new implementations, which may also be one of the reasons why the number of blocks decreased slightly compared to the prior period.
 """)

interval = st.radio('**Time Interval**',
                    ['Daily', 'Weekly'], key='fees_interval', horizontal=True)


if st.session_state.fees_interval == 'Daily':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "TOTAL_TRANSACTIONS_OVER_TIME"], ascending=[
        True, False]), x="DATE", y="TOTAL_TRANSACTIONS_OVER_TIME", color="STATUS", title='Daily Transaction before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Transaction')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "TOTAL_BLOCK_OVER_TIME"], ascending=[
        True, False]), x="DATE", y="TOTAL_BLOCK_OVER_TIME", color="STATUS", title='Daily Block before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Block')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "TBP"], ascending=[
        True, False]), x="DATE", y="TBP", color="STATUS", title='Daily Transaction Per Block (TPB) Second before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily TPB')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


elif st.session_state.fees_interval == 'Weekly':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "TOTAL_TRANSACTIONS_OVER_TIME"], ascending=[
        True, False]), x="WEEK", y="TOTAL_TRANSACTIONS_OVER_TIME", color="STATUS", title='Weekly Transaction before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Transaction')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "TOTAL_BLOCK_OVER_TIME"], ascending=[
        True, False]), x="WEEK", y="TOTAL_BLOCK_OVER_TIME", color="STATUS", title='Weekly Block before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Number of Block')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "TPS_DAILY"], ascending=[
        True, False]), x="WEEK", y="TPS_DAILY", color="STATUS", title='Weekly Transaction Per (TPS) Second before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily TPS')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#############################################################################################################


st.write(""" ## Comparing Transaction Types Before and After the Fork """)

st.write(""" While the majority of transactions still lack a label, transferred was the most common transaction type. More than 50% of transactions currently lack a label, despite the possibility that the reorganisation protocol would eventually correct this misinformation in tables.
 """)

c1, c2 = st.columns(2)

with c2:
    # Number of Transaction Pie chart
    fig = px.pie(df4, values="Number of Transactions",
                 names="ACTION", title='After the Fork Transaction Type', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c1:
    # Number of Transaction Pie chart
    fig = px.pie(df5, values="Number of Transactions",
                 names="ACTION", title='Before the Fork Transaction Type', hole=0.5)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

############################################################################

st.write(""" ## Transaction HeatMaps """)

st.write(""" The peak of transactions per minute was slightly changed after fork employment in the early hour of the day. Also, Sunday transactions moderately dropped compared to the period before fork implementation. Generally, the transactions were not as evenly distributed as before and were more concentrated throughout certain times of the day.
 """)

c1, c2 = st.columns(2)

with c1:
    st.write(""" #### Before Fork""")
    # "transactions per minute on hour of day (UTC)"
    fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Transactions per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                             histfunc='avg', title='Block per Minute Daily HEAT', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    st.write(""" #### After Fork""")
    # "transactions per minute on hour of day (UTC)"
    fig = px.density_heatmap(df6, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Transactions per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df6, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                             histfunc='avg', title='Block per Minute Daily HEAT', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#############################################################################
st.text(" \n")

st.info(""" #### Conclusion: ####

 * The overall number of transactions decreased by roughly 1%    
 * Although the number of transactions dropped on February 11, the general trend of transactions remained unchanged   
 * The average number of transactions in each block increased by 4%  
 * The majority of transactions still lack a label    
 * the transactions were not as evenly distributed as before and were more concentrated throughout certain



""")
