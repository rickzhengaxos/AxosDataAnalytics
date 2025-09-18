# import streamlit as st 

# st.set_page_config(page_title="Axos - Data Analytics", layout="wide")

# # Hide sidebar, menu, and footer
# hide_elements = """
#     <style>
#     [data-testid="stSidebar"] {display: none;}
#     [data-testid="collapsedControl"] {display: none;}
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}

#     /* Left-align main content */
#     .block-container {
#         padding-top: 2rem;
#         padding-left: 3rem;
#         padding-right: 3rem;
#         max-width: 1200px;
#         margin: 0;  /* removes auto-centering */
#     }
#     </style>
# """
# st.markdown(hide_elements, unsafe_allow_html=True)

# # Title
# st.title("Axos Projects and Reporting")

# st.write("Sections below:")

# # Button to launch Tableau → Excel project
# if st.button("Tableau to Excel Report Project"):
#     st.switch_page("pages/TableauToExcel.py")  

# # Reports dictionary
# reports = {
#     "Daily Loan Balance Report - Tableau": "https://prod-useast-b.online.tableau.com/#/site/axosfinancialproduction/views/DailyLoanBalance/UnusedLineFees?:iid=1",
#     "WIP nCino Loan Origination Report - SSRS": "http://jhaknow/reports/report/Work%20in%20Progress/Rick's%20Hub/WIP%20nCino%20Loan%20Origination%20Report",
#     "WIP Loan Boarding Approval (nCino) - SSRS": "http://jhaknow/reports/report/Work%20in%20Progress/Rick's%20Hub/WIP%20Loan%20Boarding%20Approval%20(nCino)"
# }

# # Search bar
# search_query = st.text_input("🔎 Search Reports")

# # Filter reports based on search query
# filtered_reports = {name: url for name, url in reports.items() if search_query.lower() in name.lower()}

# # Expander for loan boarding reports
# with st.expander("SSRS/Tableau Reports"):
#     if filtered_reports:
#         for name, url in filtered_reports.items():
#             st.markdown(f"- [{name}]({url})")
#     else:
#         st.write("No reports found.")


import streamlit as st 

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
st.markdown(hide_elements, unsafe_allow_html=True)

# Title
st.title("Axos Projects and Reporting")

st.write("Sections below:")

# Button to launch Tableau → Excel project
if st.button("Tableau to Excel Report Project"):
    st.switch_page("pages/TableauToExcel.py")  

# Reports dictionary
reports = {
    "Daily Loan Balance Report - Tableau": "https://prod-useast-b.online.tableau.com/#/site/axosfinancialproduction/views/DailyLoanBalance/UnusedLineFees?:iid=1",
    "WIP nCino Loan Origination Report - SSRS": "http://jhaknow/reports/report/Work%20in%20Progress/Rick's%20Hub/WIP%20nCino%20Loan%20Origination%20Report",
    "WIP Loan Boarding Approval (nCino) Report - SSRS": "http://jhaknow/reports/report/Work%20in%20Progress/Rick's%20Hub/WIP%20Loan%20Boarding%20Approval%20(nCino)",
    "WIP Post-Funding Covenant (PFC) Report - SSRS": "http://jhaknow/reports/report/Work%20in%20Progress/Rick's%20Hub/WIP%20PostFundingCovenant%20(PFC)%20Report"
}

# --- Search with dropdown suggestions ---
search_options = list(reports.keys())
search_choice = st.selectbox("Search Reports", [""] + search_options)

if search_choice:
    st.markdown(f"**Selected Report:** [{search_choice}]({reports[search_choice]})")

