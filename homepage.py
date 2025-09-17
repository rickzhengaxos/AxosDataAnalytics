import streamlit as st 

st.set_page_config(page_title="Axos - Data Analytics", layout="centered")


st.set_page_config(page_title="Axos - Data Analytics", layout="wide")

# Hide sidebar, menu, and footer
hide_elements = """
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Left-align main content */
    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1200px;
        margin: 0;  /* removes auto-centering */
    }
    </style>
"""

# Title
st.title("Axos Projects and Reporting")

st.write("Sections below:")

# Button to launch your Streamlit project
if st.button("Tableau to Excel Report Project"):
    st.switch_page("pages/TableauToExcel.py")  

# Expander with loan boarding reports links
with st.expander("Loan Boarding Reports"):
    st.markdown(
        "- [Daily Loan Balance Report](https://prod-useast-b.online.tableau.com/#/site/axosfinancialproduction/views/DailyLoanBalance/UnusedLineFees?:iid=1)"  
    )  
    st.markdown("- [Report 2](https://example.com/report2)")  
    st.markdown("- [Report 3](https://example.com/report3)")  
