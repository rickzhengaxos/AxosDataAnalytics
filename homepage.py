import streamlit as st 

st.set_page_config(page_title= "Axos - Data Analytics", layout="centered")

st.title("Commercial / Credit Projects (Managed by Rick)")

st.write("Sections below:")

if st.button("Tableau to Excel Report Project"):
    st.switch_page("pages/TableauToExcel.py")  

with st.expander("📂 Loan Boarding Reports"):
    st.markdown("- [Daily Loan Balance Report](https://prod-useast-b.online.tableau.com/#/site/axosfinancialproduction/views/DailyLoanBalance/UnusedLineFees?:iid=1)")  
    st.markdown("- [Report 2](https://example.com/report2)")  
    st.markdown("- [Report 3](https://example.com/report3)")  
