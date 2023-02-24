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
st.set_page_config(page_title='Network Performance -Polygan Hard Fork ',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🎯 Network Performance ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Overview_After':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6fd4bc1b-eb0c-466e-bc65-d0e55401c968/data/latest')
    elif query == 'Overview_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5ff1083b-0a20-4d50-9eb2-98a085b734cc/data/latest')
    elif query == 'Daily_Netperformance':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c99ce1f1-8a46-48ef-8f06-89ee2db629d9/data/latest')
    elif query == 'Succeeded_Daily':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/13b3fcb3-f92a-4c19-b995-aa0555d75660/data/latest')
    elif query == 'Time_Between_Blocks':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1d0d9572-bea5-4512-a7a0-c963d5adca76/data/latest')
    elif query == 'HeatMap_After':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/2bf9bb29-ab93-4227-9d68-6cf72595a9e7/data/latest')
    elif query == 'HeatMap_Before':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/544122bd-cbc0-48d6-b927-86d212772b0b/data/latest')
    return None


Overview_After = get_data('Overview_After')
Overview_Before = get_data('Overview_Before')
Daily_Netperformance = get_data('Daily_Netperformance')
Succeeded_Daily = get_data('Succeeded_Daily')
Time_Between_Blocks = get_data('Time_Between_Blocks')
HeatMap_After = get_data('HeatMap_After')
HeatMap_Before = get_data('HeatMap_Before')
D_TX_type = get_data('D_TX_type')
D_Fee_Type = get_data('D_Fee_Type')


df = Overview_After
df2 = Overview_Before
df3 = Daily_Netperformance
df4 = Succeeded_Daily
df5 = Time_Between_Blocks
df6 = HeatMap_After
df7 = HeatMap_Before
############################################################################################################

st.write(""" ### Key Metrics to Measure Blockchain Network performance ##  """)

st.write("""
Everything out there has a particular set of characteristics against which its performance can be measured. Be it something as simple as a car or as intricately intertwined as the blockchain. These factors also help draw a comparison between two or multiple blockchains in order to find out the one that’s best for developing projects.[[6]](https://bitcoinist.com/key-metrics-to-measure-blockchain-network-performance/)   

* Transactions per Second (TPS)  
* Block Time 
* Transaction Latency  
* Success Rate

In this part, we make an effort to compare Polygan before and after the deployment of the fork using these metrics.  """)


st.info(""" ##### In This Network Performance Section you can find: ####

* Network Performance Before and After Fork Overview
* Transactions per Second (TPS) Over time [Daily-Weekly]
* Block Time Over time [Daily-Weekly]
* Time Between Blocks Over time [Daily-Weekly]
* Succeeded and Failed Transactions Over time [Daily-Weekly]
* Failed transactions per minute HeatMap



""")


############################################################################################################
st.text(" \n")
st.text(" \n")
st.write(""" ## Network Performance Before and After Fork Overview """)

c1, c2 = st.columns(2)
with c1:
    st.write(""" #### Before Fork""")
    st.metric(label='**Success Rate**',
              value=str(df2["Success Rate"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Transaction Per Second [TPS]**',
              value=str(df2["TPS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Block per Min [BPM]**',
              value=df2["Average Block per Min"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Failed Rate**',
              value=df2["Failed Rate"].map('{:,.0f}'.format).values[0])


with c2:
    st.write(""" #### After Fork """)
    st.metric(label='**Success Rate**',
              value=str(df["Success Rate"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Transaction Per Second [TPS]**',
              value=str(df["TPS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Block per Min [BPM]**',
              value=df["Average Block per Min"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Failed Rate**',
              value=df["Failed Rate"].map('{:,.0f}'.format).values[0])


st.text(" \n")
st.write(""" ## Network Performance Metrics Over Time """)


interval = st.radio('**Time Interval**',
                    ['Daily', 'Weekly'], key='fees_interval', horizontal=True)


if st.session_state.fees_interval == 'Daily':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "TPS_DAILY"], ascending=[
        True, False]), x="DATE", y="TPS_DAILY", color="STATUS", title='Daily Transaction Per Second (TPS) before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Transaction Fees')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["DATE", "AVG_BLOCK_TIME_DAILY"], ascending=[
        True, False]), x="DATE", y="AVG_BLOCK_TIME_DAILY", color="STATUS", title='Daily Average Block Time before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Gas Used')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Succed failed Transactionsil
    fig = px.bar(df5.sort_values(["DATE", "MAX_SEC"], ascending=[
        True, False]), x="DATE", y="MAX_SEC", color="STATUS", title='Daily Max time between blocks before and after Fork ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Time between Blocks')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Succed failed Transactionsil
    fig = px.bar(df5.sort_values(["DATE", "AVERAGE_SEC"], ascending=[
        True, False]), x="DATE", y="AVERAGE_SEC", color="STATUS", title='Daily Average time between blocks before and after Fork ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Succed failed Transactionsil
    fig = px.bar(df4.sort_values(["DATE", "TOTAL_TRANSACTIONS_OVER_TIME"], ascending=[
        True, False]), x="DATE", y="TOTAL_TRANSACTIONS_OVER_TIME", color="TRANSACTION_STATUS", title='Daily Succeeded and  Failed Transactions ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Daily Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


elif st.session_state.fees_interval == 'Weekly':

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "TPS_DAILY"], ascending=[
        True, False]), x="WEEK", y="TPS_DAILY", color="STATUS", title='Weekly Transaction Per Second before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transaction Fees')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Transaction Type In Each Wallet
    fig = px.bar(df3.sort_values(["WEEK", "AVG_BLOCK_TIME_DAILY"], ascending=[
        True, False]), x="WEEK", y="AVG_BLOCK_TIME_DAILY", color="STATUS", title='Weekly Average Block Time before and after Fork')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Gas Used')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Succed failed Transactionsil
    fig = px.bar(df5.sort_values(["WEEK", "MAX_SEC"], ascending=[
        True, False]), x="WEEK", y="MAX_SEC", color="STATUS", title='Weekly Max time between blocks before and after Fork ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Time between Blocks')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Succed failed Transactionsil
    fig = px.bar(df5.sort_values(["WEEK", "AVERAGE_SEC"], ascending=[
        True, False]), x="WEEK", y="AVERAGE_SEC", color="STATUS", title='Weekly Average time between blocks before and after Fork ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Daily Succed failed Transactionsil
    fig = px.bar(df4.sort_values(["WEEK", "TOTAL_TRANSACTIONS_OVER_TIME"], ascending=[
        True, False]), x="WEEK", y="TOTAL_TRANSACTIONS_OVER_TIME", color="TRANSACTION_STATUS", title='Weekly Succeeded and  Failed Transactions ')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transactions')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#############################################################################################################
st.write(""" ##  Failed Transaction HeatMaps """)


c1, c2 = st.columns(2)

with c1:
    st.write(""" #### Before Fork""")

    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df7, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Failed transactions per minute on hour of day (UTC)", nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
        'dtick': 2}, coloraxis_colorbar=dict(title='Transfers'))
    fig.update_yaxes(categoryorder='array', categoryarray=week_days)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    st.write(""" #### After Fork""")

    # Block per Minute Daily HEAT
    fig = px.density_heatmap(df6, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                             histfunc='avg', title="Failed transactions per minute on hour of day (UTC)", nbinsx=24)
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
