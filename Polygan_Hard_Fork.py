# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Polygan Hard Fork ',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Polygan Hard Fork 🍴')


# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.video('https://www.youtube.com/watch?v=GWUwFDFOipo')

with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/polygon-logo.png'), width=350)


st.write("""
### What Is Polygan ? ###
Polygon is a cryptocurrency, with the symbol MATIC, and also a technology platform that enables blockchain networks to connect and scale. Polygon—"Ethereum's internet of blockchains"— launched under the name Matic Network in 2017. 
The Polygon platform operates using the Ethereum blockchain and connects Ethereum-based projects. Using the Polygon platform can increase the flexibility, scalability, and sovereignty of a blockchain project while still affording the security, interoperability, and structural benefits of the Ethereum blockchain.
MATIC is an ERC-20 token, meaning that it's compatible with other Ethereum-based digital currencies. MATIC is used to govern and secure the Polygon network and to pay network transaction fees.   
Polygon uses a modified proof-of-stake consensus mechanism that enables a consensus to be achieved with every block. (Achieving consensus using traditional proof-of-stake requires processing many blocks to achieve consensus.) The proof-of-stake method requires network participants to stake—agree to not trade or sell—their MATIC, in exchange for the right to validate Polygon network transactions. Successful validators in the Polygon network are rewarded with MATIC. The Polygon network, as a secondary scaling solution, aims to address the limitations of the Ethereum platform—namely, high transaction fees and slow transaction processing speeds.[[1]](https://www.investopedia.com/polygon-matic-definition-5217569)

### Polygon Completes Hard Fork to Reduce Gas Fee Spikes  ###
Polygon, an Ethereum-scaling project, successfully completed a hard fork designed to reduce instances of spiking gas fees and disruptive chain reorganizations known as "reorgs."
The software upgrade occurred at 10:45 UTC (5:45 a.m. ET) on Tuesday, according to a tweet from Polygon Labs, the lead company behind the project.
The two proposals included in the hard fork were put forth in December. Some 87% of Polygon validator teams that participated voted for approval. Only 15 validator teams took part in the voting process, which is extremely low given the number of active validators at a time is limited to 100.
The first proposal adjusted a mechanism that sets gas fees – a kind of tax one pays in order to transact on a blockchain. The new mechanism aims to keep gas prices low when there is a lot of activity on the network.  
The second proposal aims to reduce the amount of time it takes to complete a data block – part of an effort to prevent frequent reorgs, which occur when a validator node receives information that temporarily creates a new version of the blockchain.
The price of Polygon’s native token, MATIC, is up nearly 15% over the last seven days – in keeping with a broad rally in digital-asset markets.[[2]](https://www.coindesk.com/tech/2023/01/17/polygon-completes-hard-fork-to-reduce-gas-fee-spikes-disruptive-reorgs/)

""")


c1, c2 = st.columns(2)

c1.image(Image.open('Images/Polly.jpg'))
c2.image(Image.open('Images/Twit2.jpg'))


st.write("""
## Methodology ##  
ETH-scaling project Polygon completed a hard fork last month in hopes of reducing gas fees, as well as disruptive chain reorganizations known as "reorgs,” according to Coindesk. Let’s dive into the network’s health and performance leading up to and since the hard fork.
Has the software upgrade led to lower gas fees as hoped? Have these changes affected any meaningful user metrics, such as volume, activity, monthly active users, or others?  
to answer these questions first we 




""")

st.write("""   
#### Sources ####  """)
st.write("""    1.https://www.investopedia.com/polygon-matic-definition-5217569       
        2.https://www.coindesk.com/tech/2023/01/17/polygon-completes-hard-fork-to-reduce-gas-fee-spikes-disruptive-reorgs/    
        3.https://polygon.technology/blog/hardfork-incoming-upgrading-polygon-pos-chain-to-boost-performance  
        4.https://www.youtube.com/watch?v=GWUwFDFOipo   
 
      
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Project Github:  [Polygan Hard Fork](https://github.com/Kaizen-Step/The_Whales_of_Near)**', icon="💻")

with c1:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
