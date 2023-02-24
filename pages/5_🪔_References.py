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
st.set_page_config(page_title='Aknowledgement - Polygan Hard Fork',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Aknowledgement
st.write(""" ##     Aknowledgement 
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Flipside Crypto**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.
""")


# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


c1, c2 = st.columns(2)

with c1:
    st.write("""
    1. [Transaction Daily Polygan](https://flipsidecrypto.xyz/edit/queries/59a8d1ec-2c8c-469c-8d9d-e9e6de66b3c2/visualizations/b6cca8d3-9918-443b-ae24-6d8ce04cab52)   
    2. [Transaction Overview-polygan after](https://flipsidecrypto.xyz/edit/queries/6164fe51-8f89-438d-9c65-8358ec4fc541)  
    3. [Transaction Overview-polygan Before](https://flipsidecrypto.xyz/edit/queries/f4384d86-9743-4b11-be24-8a93bbafb333)  
    4. [Transaction Comparison After](https://flipsidecrypto.xyz/edit/queries/c82fec67-e4b1-40eb-85f5-43101727ee4b/visualizations/e2498788-999f-40bb-9a21-412b414d8d40)  
    5. [Transaction Comparison Before](https://flipsidecrypto.xyz/edit/queries/1ba973f4-6d84-44ae-995b-f310ce0c4182/visualizations/eb392595-2872-4843-bbdd-984c3463f134)  
    6. [Transaction HeatMaps After](https://flipsidecrypto.xyz/edit/queries/3fbb3196-46ec-48eb-a750-5ed37ab48532)  
    7. [Transaction HeatMaps Before](https://flipsidecrypto.xyz/edit/queries/e9e1f2f2-7d01-43fc-b170-ce953042d080)  
    
    
    """)

with c2:

    st.write("""

    8. [Network Daily Fail and Succ](https://flipsidecrypto.xyz/edit/queries/13b3fcb3-f92a-4c19-b995-aa0555d75660/visualizations/a1f3da8d-2a0c-42ff-97e5-af0e6871bd0a)  
    9. [Time between blocks](https://flipsidecrypto.xyz/edit/queries/e352c3a7-bd07-45c0-8ef9-4aa30ffe51b3/visualizations/f1f9cf6c-7bb2-4ed9-afa4-a78874c0827e)  
    10. [Network Heatmap Before](https://flipsidecrypto.xyz/edit/queries/544122bd-cbc0-48d6-b927-86d212772b0b)  
    11. [Network Heatmap Before](https://flipsidecrypto.xyz/edit/queries/544122bd-cbc0-48d6-b927-86d212772b0b)  
    12. [Network Daily](https://flipsidecrypto.xyz/edit/queries/c99ce1f1-8a46-48ef-8f06-89ee2db629d9)  
    13. [Network Heatmap After](https://flipsidecrypto.xyz/edit/queries/2bf9bb29-ab93-4227-9d68-6cf72595a9e7)  
    14. [Overview Before](https://flipsidecrypto.xyz/edit/queries/5ff1083b-0a20-4d50-9eb2-98a085b734cc)     


    """)


# Sources
st.write(""" ## Sources ## """)

st.write("""
1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/    
2.https://worldcoin.org/articles/what-is-a-crypto-whale    
3.https://www.youtube.com/watch?v=1cozsZP8yd4&t=30s  
4.https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/  
5.https://academy.binance.com/en/articles/what-s-the-difference-between-a-cex-and-a-dex   
6.https://www.forbes.com/advisor/in/investing/cryptocurrency/what-is-staking-in-crypto/#:~:text=Staking%20is%20when%20you%20lock,proof%20of%20stake%20consensus%20mechanism.   
7.https://bitpay.com/blog/what-is-a-crypto-swap/#:~:text=Crypto%20swapping%20allows%20you%20to,reason%20users%20participate%20in%20swapping.  
8.https://www.investopedia.com/terms/b/bitcoin-whale.asp#:~:text=A%20crypto%20whale%20is%20a,also%20create%20price%20volatility%20increases.  

""")
