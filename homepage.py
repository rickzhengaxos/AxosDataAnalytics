import streamlit as st 

st.set_page_config(page_title="Axos - Data Analytics", layout="centered")

# Hide sidebar, menu, and footer
hide_elements = """
    <style>
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_elements, unsafe_allow_html=True)

# Title
st.title("Commercial / Credit Projects (Managed by Rick)")

st.write("Sections below:")

# Button to launch your Streamlit project
if st.button("📊 Tableau to Excel Report Project"):
    st.switch_page("pages/TableauToExcel.py")  

# Expander with loan boarding reports links
with st.expander("📂 Loan Boarding Reports"):
    st.markdown(
        "- [Daily Loan Balance Report](https://prod-useast-b.online.tableau.com/#/site/axosfinancialproduction/views/DailyLoanBalance/UnusedLineFees?:iid=1)"  
    )  
    st.markdown("- [Report 2](https://example.com/report2)")  
    st.markdown("- [Report 3](https://example.com/report3)")  
