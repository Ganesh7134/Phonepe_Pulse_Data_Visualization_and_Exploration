import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import json
# Define the menu options and icons
import streamlit as st
import webbrowser
import mysql.connector
from streamlit_lottie import st_lottie

host = "localhost"
port = 3306
user = "root"
password = "Ganesha143@"

# Create a connection object
conn = mysql.connector.connect(host=host, port=port, user=user, password=password)
cursor = conn.cursor()
Db = cursor.execute("use phonepe_data;")

def home():
    
    container = st.container()
    try:
        with container:
            @st.cache_data(ttl=60 * 60)
            def load_lottie_file(filepath : str):
                with open(filepath, "r") as f:
                    gif = json.load(f)
                st_lottie(gif, speed=1, width=450, height=450)
                
            load_lottie_file("anime.json")
    except:
        print("Don't raise exception")

    # Create a container around the image
    image = Image.open("PhonePe.webp")
    resized_image = image.resize((300, 100))
    st.image(resized_image)

    
    st.title(":bar_chart: Phonepe pulse visualization Dashboard")
    
    with st.container():
        st.subheader("A data visualization platform for the payments landscape in India")

    # Create a section to describe PhonePe Pulse
        st.markdown("""
            PhonePe Pulse is a data visualization platform that provides insights into the payments landscape in India. It uses a variety of data sources, including transaction data, user data, and merchant data, to create visualizations that show how people are paying, where they are paying, and what they are paying for.

            PhonePe Pulse is a valuable tool for businesses and policymakers. Businesses can use PhonePe Pulse to understand their customers' payment habits and to identify new opportunities. Policymakers can use PhonePe Pulse to track the adoption of digital payments and to identify areas where government intervention is needed.
            """)

    # Create a section to provide examples of how PhonePe Pulse can be used
        st.markdown("""
            ### Examples of how PhonePe Pulse can be used
            **Businesses:**

            * A business can use PhonePe Pulse to see which payment methods are most popular with their customers. This information can be used to prioritize payment integrations and to develop marketing campaigns. For example, if a business sees that a large percentage of its customers are using UPI, then the business may want to focus on developing UPI-based promotions.

            **Policymakers:**

            * A policymaker can use PhonePe Pulse to track the adoption of digital payments in different regions of India. This information can be used to identify areas where government intervention is needed to promote digital payments. For example, if a policymaker sees that digital payments are low in a particular region, then the policymaker may want to implement programs to educate people about the benefits of digital payments.
            """)

    # Create a section to describe a sample PhonePe Pulse visualization
        st.markdown("""
            ### Sample PhonePe Pulse visualization
            **Visualization Title:** Top UPI Merchants in India

            **Visualization Description:** This visualization shows the top 10 UPI merchants in India by transaction volume. The visualization is a bar chart, with the x-axis showing the merchant name and the y-axis showing the transaction volume in millions of rupees.

            **Data:** The data for this visualization is collected from PhonePe's transaction data. The data is filtered to include only UPI transactions. The data is then sorted by transaction volume, and the top 10 merchants are selected.

            **Insights:** This visualization provides insights into the most popular UPI merchants in India. The visualization shows that Walmart and Amazon are the two most popular UPI merchants in India. This is likely due to the fact that these merchants offer a wide range of products and services, and they accept UPI payments for both online and offline transactions.

            **Other Insights:** This visualization also provides insights into the popularity of different types of merchants. For example, the visualization shows that grocery stores, e-commerce merchants, and food delivery merchants are all very popular UPI merchants. This suggests that people are increasingly using UPI to pay for everyday expenses.
            """)

    # Conclusion
        st.markdown("""
            ## Conclusion

            PhonePe Pulse is a valuable tool for businesses and policymakers. It provides insights into the payments landscape in India and can be used to identify new opportunities and to track the adoption of digital payments.
            """)
        def phonepe_download():
            webbrowser.open("https://www.phonepe.com/app-download/")
        
        image = Image.open("phonepe_down.webp")
        resized_image = image.resize((300,500))
        with st.expander(label="Download Phonepe"):
            st.image(resized_image)
            st.button(label="click here to go phonepe Download page", type="secondary", on_click=phonepe_download)

def about():
    container = st.container()
    try:
        with container:
            @st.cache_data(ttl=60 * 60)
            def load_lottie_file(filepath : str):
                with open(filepath, "r") as f:
                    gif = json.load(f)
                st_lottie(gif, speed=1, width=800, height=450)
                
            load_lottie_file("about.json")
    except:
        print("Don't raise exception")
    st.header("About PhonePe Pulse Visualization Project")
    st.markdown("""
    PhonePe Pulse is a public dataset released by PhonePe, a leading digital payments platform in India. The dataset contains a wide range of metrics and statistics on PhonePe's transactions, users, and merchants.

    The PhonePe Pulse Visualization Project is a data visualization project that aims to extract valuable insights from the PhonePe Pulse dataset. The project uses Python, Streamlit, and Plotly to create interactive dashboards that visualize the data in a clear and concise way.

    The PhonePe Pulse Visualization Project is still under development, but it has already produced some interesting insights. For example, the project has revealed that the majority of PhonePe transactions are made for small amounts, and that the number of PhonePe users is growing rapidly.

    The PhonePe Pulse Visualization Project is a valuable resource for anyone who is interested in learning more about PhonePe and the digital payments landscape in India. The project is also a great example of how data visualization can be used to extract valuable insights from large and complex datasets.
    """)
    st.subheader("Goals of the Project")
    st.markdown("""
    The goals of the PhonePe Pulse Visualization Project are to:

    * Provide a comprehensive and interactive visualization of the PhonePe Pulse dataset.
    * Extract valuable insights from the dataset and share them with the public.
    * Promote data literacy and encourage the use of data visualization in India.
    """)
    st.subheader("Benefits of the Project")
    st.markdown("""
    The PhonePe Pulse Visualization Project benefits a wide range of stakeholders, including:

    * **Data scientists and analysts:** The project provides a valuable resource for data scientists and analysts to explore and analyze the PhonePe Pulse dataset.
    * **Businesses and organizations:** The project can help businesses and organizations to understand the digital payments landscape in India and to identify new opportunities.
    * **Policymakers:** The project can help policymakers to make informed decisions about the digital payments industry.
    * **The general public:** The project can help the general public to understand how PhonePe works and to learn more about the digital payments landscape in India.
  """)
    
    def phonepe_doc():
            webbrowser.open("https://drive.google.com/file/d/1VBRecdnRpbutknJLNZQC4f1bc1eKWdsw/view?pli=1")
    st.button(label="click here to go phonepe project documentation", type="primary", on_click=phonepe_doc)

    def phonepe_git():
            webbrowser.open("https://github.com/PhonePe/pulse#readme")
    st.button(label="click here to go phonepe project dataset", type="primary", on_click=phonepe_git)

    def phonepe_ref():
            webbrowser.open("https://www.phonepe.com/pulse/explore/transaction/2022/4/")
    st.button(label="click here to go phonepe project reference", type="primary", on_click=phonepe_ref)

def insights():
    
    # Define a function to read the Aggregated_transactions.csv file
    container = st.container()
    try:
        with container:
            @st.cache_data(ttl=60 * 60)
            def load_lottie_file(filepath : str):
                with open(filepath, "r") as f:
                    gif = json.load(f)
                st_lottie(gif, speed=1, width=800, height=450)
                
            load_lottie_file("insights.json")
    except:
        print("Don't raise exception")
    def Transactions():
    
        def get_data(year, quarter):
            query = f"SELECT * FROM aggregated_transactions WHERE Year = {year} AND Quater = {quarter}"
            df = pd.read_sql(query, conn, index_col="State")
            return df

        # Create a year slider
        year_start = 2018
        year_end = 2023
        selected_year = st.slider("Select Year:", year_start, year_end)

        # Create a quarter slider based on the selected year
        quarter_start = 1
        quarter_end = 4
        selected_quarter = st.slider("Select Quarter:", quarter_start, quarter_end)

        # Get data for the selected year and quarter
        df = get_data(selected_year, selected_quarter)

        # Aggregate data by 'State' for Transaction_Amount and Transaction_count
        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
        data_count = df.groupby(['State'])['Transaction_count'].sum().reset_index()

        # Create a Plotly bar chart for the total transaction amount by state
        fig_amount = px.bar(
            data_amount,
            x="State",
            y="Transaction_Amount",
            color="State",
            title="Total Transaction Amount by State for Year {} Quarter {}".format(selected_year, selected_quarter)
        )
        st.plotly_chart(fig_amount)

        # Create a Plotly bar chart for the total transaction count by state
        fig_count = px.bar(
            data_count,
            x="State",
            y="Transaction_count",
            color="State",
            title="Total Transaction Count by State for Year {} Quarter {}".format(selected_year, selected_quarter)
        )
        st.plotly_chart(fig_count)


    
        with st.expander("Map transactions amount by state and district"):
            st.header("Map transactions amount by state and district")
            df = pd.read_sql("select * from  map_transaction1;",conn,index_col="State")

            # Create a multiselect for states
            state_options = df.index.unique().tolist()
            selected_state2 = st.multiselect("Select states:", state_options,key="selected_state2")

            # Create a slider for year
            year_start = 2018
            year_end = 2023
            selected_year1 = st.slider("Select year:", year_start, year_end,key="selected_year1")
        
            # Create a slider for quarter
            quarter_start = 1
            quarter_end = 4
            selected_quarter1 = st.slider("Select quarter:", quarter_start, quarter_end,key="selected_quarter1")

            # Get the data for the selected state, year, and quarter
            def get_data_for_state_year_quarter(state, year, quarter):
                state_df = df.loc[state]
                state_df = state_df.loc[(state_df['Year'] == year) & (state_df['Quater'] == quarter)]
                return state_df

            state_df = get_data_for_state_year_quarter(selected_state2, selected_year1, selected_quarter1)

            # Aggregate data by 'State' for Transaction_Amount and Transaction_count
            state_amount = state_df.groupby(['State'])['Transaction_amount'].sum().reset_index()

            # # Aggregate data by 'District' for Transaction_Amount and Transaction_count
            district_amount = state_df.groupby(['District_name'])['Transaction_amount'].sum().reset_index()

            # Create a bar graph of state-wise transaction amount
            fig_state = px.bar(
                state_amount,
                x="State",
                y="Transaction_amount",
                color="State",
                title="Total Transaction Amount by State in {} Year Quarter {}".format(selected_year1, selected_quarter1)
            )

            # Create a bar graph of district-wise transaction amount for the selected state, year, and quarter
            fig_district = px.bar(
                district_amount,
                x="District_name",
                y="Transaction_amount",
                color="District_name",
                title="Total Transaction Amount by District in {} State {} Year Quarter {}".format(selected_state2, selected_year1, selected_quarter1)
            )

            # Display the graphs on Streamlit
            st.plotly_chart(fig_state)
            st.plotly_chart(fig_district)

        with st.expander("Top transactions amount by state and district and pincode"):
            st.header("Top transactions amount by state and district")
            df = pd.read_sql("select * from top_transaction_districts;",conn,index_col="State")

            # Create a multiselect for states
            state_options = df.index.unique().tolist()
            selected_state3 = st.multiselect("Select states:", state_options,key="selected_state3")

            # Create a slider for year
            year_start = 2018
            year_end = 2023
            selected_year = st.slider("Select year:", year_start, year_end)

            # Create a slider for quarter
            quarter_start = 1
            quarter_end = 4
            selected_quarter = st.slider("Select quarter:", quarter_start, quarter_end)

            # Get the data for the selected state, year, and quarter
            def get_data_for_state_year_quarter(state, year, quarter):
                state_df = df.loc[state]
                state_df = state_df.loc[(state_df['Year'] == year) & (state_df['Quater'] == quarter)]
                return state_df

            state_df = get_data_for_state_year_quarter(selected_state3, selected_year, selected_quarter)

            # Aggregate data by 'State' for Transaction_Amount and Transaction_count
            state_amount = state_df.groupby(['State'])['Transaction_amount'].sum().reset_index()

            # # Aggregate data by 'District' for Transaction_Amount and Transaction_count
            district_amount = state_df.groupby(['District_name'])['Transaction_amount'].sum().reset_index()

            df1 = pd.read_sql("select * from top_transaction_pincode",conn,index_col="State")

            def get_data_for_state_year_quarter(state, year, quarter):
                state_df = df1.loc[state]
                state_df = state_df.loc[(state_df['Year'] == year) & (state_df['Quater'] == quarter)]
                return state_df
            
            state_df = get_data_for_state_year_quarter(selected_state3, selected_year, selected_quarter)

            # Aggregate data by 'Pincode' for Transaction_Amount
            pin_amount = state_df.groupby(['pincode'])['Transaction_amount'].sum().reset_index()

            # Create a bar graph of pincode-wise transaction amount
            fig_pincode = px.pie(
                pin_amount,
                names="pincode",
                values="Transaction_amount",
                title="Total Transaction Amount by Pincode in {} State {} Year Quarter {}".format(selected_state3, selected_year, selected_quarter)
            )

            # Create a bar graph of state-wise transaction amount
            fig_state = px.bar(
                state_amount,
                x="State",
                y="Transaction_amount",
                color="State",
                title="Total Transaction Amount by State in {} Year Quarter {}".format(selected_year, selected_quarter)
            )

            # Create a bar graph of district-wise transaction amount for the selected state, year, and quarter
            fig_district = px.bar(
                district_amount,
                x="District_name",
                y="Transaction_amount",
                color="District_name",
                title="Total Transaction Amount by District in {} State {} Year Quarter {}".format(selected_state3, selected_year, selected_quarter)
            )

            # Display the graphs on Streamlit
            st.plotly_chart(fig_state)
            st.plotly_chart(fig_district)
            st.plotly_chart(fig_pincode)

        def pin_code():
            webbrowser.open("http://1min.in/indiapost/pincode/826001")
        st.button(label="click here to go pincode search", type="primary", on_click=pin_code)

        container = st.container()
        with container:
            df = pd.read_sql("SELECT * FROM aggregated_transactions",conn)
            grouped_df = df.groupby('Transaction_type')['Transaction_Amount'].sum()
            dict_ = grouped_df.to_dict()

            labels = list(dict_.keys())
            sizes = list(dict_.values())

            def us_dollars(number):
                    """Converts an integer number to US dollars.

                    Args:
                        number: An integer number.

                    Returns:
                        A string representing the number in US dollars, with two decimal places.
                    """
                    res = number//83.22
                    return "${:,.2f}".format(res)
            in_dollars = []
            for i in sizes:
                in_dollars.append(us_dollars(i))
            # st.write(in_dollars)
            data = pd.DataFrame(
                {
                    "Transaction_type":labels,
                    "Total_transaction_amount" :sizes,
                    "Modified_trans_amount":np.log10(sizes),
                    "transaction_amount_in_dollars":in_dollars
                }
            )

            Pie_chart = px.pie(
            data,
            values="Modified_trans_amount",
            names="Transaction_type",
            title="Pie chart of Total Transaction Amount by Transaction Type",
            height=300,
            width=400,
            )

            # Add the Pie chart to a Streamlit expander.
            with st.expander("Pie chart of Total Transaction Amount by Transaction Type"):
                st.plotly_chart(Pie_chart)

            container = st.container()
        with container:
            df = pd.read_sql("select * from aggregated_transactions;",conn)
            grouped_df = df.groupby(['State'])['Transaction_Amount'].sum()
            dict_ = grouped_df.to_dict()
            labels = list(dict_.keys())
            sizes = list(dict_.values())
            # st.write(dict_)
            data = pd.DataFrame({
                                    "State":labels,
                                    "Total_transaction_amount":sizes
                                })
            Pie_chart = px.pie(
            data,
            values="Total_transaction_amount",
            names="State",
            title="Pie chart of Total number of transaction amount by state",
            height=300,
            width=400,
            )
            with st.expander("Pie chart of Total transaction amount by state"):
                st.plotly_chart(Pie_chart)
           
            with container:
                df = pd.read_sql("select * from aggregated_transactions;",conn)
                grouped_df = df.groupby(['State'])['Transaction_count'].sum()
                dict_ = grouped_df.to_dict()
                labels = list(dict_.keys())
                sizes = list(dict_.values())
                # st.write(dict_)
                data = pd.DataFrame({
                                        "State":labels,
                                        "Total_transaction_count":sizes
                                    })
                Pie_chart = px.pie(
                data,
                values="Total_transaction_count",
                names="State",
                title="Pie chart of Total number of transaction count by state",
                height=300,
                width=400,
                )
                with st.expander("Pie chart of Total transaction count by state"):
                    st.plotly_chart(Pie_chart)

            def get_data():
                df = pd.read_sql("select * from aggregated_transactions;", conn, index_col="State")
                return df

            df = get_data()

            # Create a multiselect widget for brands
            type_options = df['Transaction_type'].unique()
            selected_type = st.multiselect("Select Transaction_type :", type_options)

            # Filter the DataFrame based on selected brands
            filtered_df = df[df['Transaction_type'].isin(selected_type)]

            # Group the data by state and brand and sum the count column
            grouped_df = filtered_df.groupby(['State', 'Transaction_type'])['Transaction_Amount'].sum().reset_index()

            fig = px.bar(
                grouped_df,
                x="State",
                y="Transaction_Amount",
                color="State",
                labels={"Transaction_Amount": "Total_transaction_Amount"},
                title="Total Transaction_Amount by State and Transaction_type"
            )

            # Display the Plotly chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

    
    def users():
        def get_data(year, quarter):
            query = f"SELECT * FROM aggregate_users WHERE Year = {year} AND Quater = {quarter}"
            df = pd.read_sql(query, conn, index_col="State")
            return df

        # Create a year slider
        year_start = 2018
        year_end = 2023
        selected_year = st.slider("Select Year:", year_start, year_end)

        # Create a quarter slider based on the selected year
        quarter_start = 1
        quarter_end = 4
        selected_quarter = st.slider("Select Quarter:", quarter_start, quarter_end)

        # Get data for the selected year and quarter
        df = get_data(selected_year, selected_quarter)

        # Aggregate data by 'State' for count and appOpens
        reg_users = df.groupby(['State'])['count'].sum().reset_index()
        app = df.groupby(['State'])['appOpens'].sum().reset_index()

        # Create a Plotly bar chart for the total registered users by state
        fig_reg_users = px.bar(
            reg_users,
            x="State",
            y="count",
            color="State",
            title="Total Registered Users by State for Year {} Quarter {}".format(selected_year, selected_quarter)
        )
        st.plotly_chart(fig_reg_users)

        # Create a Plotly bar chart for the total appOpens by state
        fig_app = px.bar(
            app,
            x="State",
            y="appOpens",
            color="State",
            title="Total App Opens by State for Year {} Quarter {}".format(selected_year, selected_quarter)
        )
        st.plotly_chart(fig_app)

        container = st.container()
        with container:
            df = pd.read_sql("select * from aggregate_users;",conn)
            grouped_df = df.groupby(['State'])['count'].sum()
            dict_ = grouped_df.to_dict()
            labels = list(dict_.keys())
            sizes = list(dict_.values())
            # st.write(dict_)
            data = pd.DataFrame({
                                    "State":labels,
                                    "registered_users":sizes
                                })
            Pie_chart = px.pie(
            data,
            values="registered_users",
            names="State",
            title="Pie chart of Total number of phonepe users by state",
            height=300,
            width=400,
            )
            with st.expander("Pie Chart of Total registered users by state"):
                st.plotly_chart(Pie_chart)

        with st.expander("Map registeredUsers by state and district"):
            st.header("Map registeredUsers by state and district")
            # Load the data
            df = pd.read_sql("select * from  map_user;",conn,index_col="State")

            # Create a multiselect for states
            state_options = df.index.unique().tolist()
            selected_state = st.multiselect("Select states:", state_options, key="selected_state")

            # Create a slider for year
            year_start = 2018
            year_end = 2023
            selected_year = st.slider("Select year:", year_start, year_end)

            # Create a slider for quarter
            quarter_start = 1
            quarter_end = 4
            selected_quarter = st.slider("Select quarter:", quarter_start, quarter_end)

            # Get the data for the selected state, year, and quarter
            def get_data_for_state_year_quarter(state, year, quarter):
                state_df = df.loc[state]
                state_df = state_df.loc[(state_df['Year'] == year) & (state_df['Quater'] == quarter)]
                return state_df

            state_df = get_data_for_state_year_quarter(selected_state, selected_year, selected_quarter)

            # Aggregate data by 'State' for registeredUser
            state_amount = state_df.groupby(['State'])['registeredUser'].sum().reset_index()

            # Aggregate data by 'District' for registeredUser
            district_amount = state_df.groupby(['District_name'])['registeredUser'].sum().reset_index()

            # Create a bar graph of state-wise registeredUsers
            fig_state = px.bar(
                state_amount,
                x="State",
                y="registeredUser",
                color="State",
                title="Total Registered Users by State in {} Year Quarter {}".format(selected_year, selected_quarter)
            )

            # Create a bar graph of district-wise registeredUsers for the selected state, year, and quarter
            fig_district = px.bar(
                district_amount,
                x="District_name",
                y="registeredUser",
                color="District_name",
                title="Total Registered Users by District in {} State {} Year Quarter {}".format(selected_state, selected_year, selected_quarter)
            )

            # Display the graphs on Streamlit
            st.plotly_chart(fig_state)
            st.plotly_chart(fig_district)

        with st.expander("Top registeredUsers by state and district and pincode"):
            st.header("Top registeredUsers by state and district")
            # Load the data
            df = pd.read_sql("select * from top_users_district;",conn,index_col="State")

            # Create a multiselect for states
            state_options = df.index.unique().tolist()
            selected_state1 = st.multiselect("Select states:", state_options, key="selected_state1")

            # Create a slider for year
            year_start = 2018
            year_end = 2023
            selected_year1 = st.slider("Select year:", year_start, year_end,key="selected_year1")

            # Create a slider for quarter
            quarter_start = 1
            quarter_end = 4
            selected_quarter1 = st.slider("Select quarter:", quarter_start, quarter_end,key="selected_quarter1")

            # Get the data for the selected state, year, and quarter
            def get_data_for_state_year_quarter(state, year, quarter):
                state_df = df.loc[state]
                state_df = state_df.loc[(state_df['Year'] == year) & (state_df['Quater'] == quarter)]
                return state_df

            state_df = get_data_for_state_year_quarter(selected_state1, selected_year1, selected_quarter1)

            # Aggregate data by 'State' for registeredUsers
            state_amount = state_df.groupby(['State'])['registeredUsers'].sum().reset_index()

            # Aggregate data by 'District' for registeredUsers
            district_amount = state_df.groupby(['District_name'])['registeredUsers'].sum().reset_index()

            df1 = pd.read_sql("select * from top_users_pincode;",conn,index_col="State")
            def get_data_for_state_year_quarter(state, year, quarter):
                state_df = df1.loc[state]
                state_df = state_df.loc[(state_df['Year'] == year) & (state_df['Quater'] == quarter)]
                return state_df

            state_df = get_data_for_state_year_quarter(selected_state1, selected_year1, selected_quarter1)

            # Aggregate data by 'State' for registeredUsers
            pin_amount = state_df.groupby(['pincode'])['registeredUsers'].sum().reset_index()

            # Create a bar graph of state-wise registeredUsers
            fig_state = px.bar(
                state_amount,
                x="State",
                y="registeredUsers",
                color="State",
                title="Total Registered Users by State in {} Year Quarter {}".format(selected_year1, selected_quarter1)
            )

            # Create a bar graph of district-wise registeredUsers for the selected state, year, and quarter
            fig_district = px.bar(
                district_amount,
                x="District_name",
                y="registeredUsers",
                color="District_name",
                title="Total Registered Users by District in {} State {} Year Quarter {}".format(selected_state1, selected_year1, selected_quarter1)
            )
            fig_pin = px.pie(
                pin_amount,
                names="pincode",
                values="registeredUsers",
                title="Total Registered Users by pincode in {} Year Quarter {}".format(selected_year1, selected_quarter1)
            )
            # Display the graphs on Streamlit
            st.plotly_chart(fig_state)
            st.plotly_chart(fig_district)
            st.plotly_chart(fig_pin)
            
        def pin_code():
            webbrowser.open("http://1min.in/indiapost/pincode/826001")
        st.button(label="click here to go pincode search", type="primary", on_click=pin_code)

        with container:
            df = pd.read_sql("select * from top_users;",conn)
            grouped_df = df.groupby(['District_name'])['registeredUsers'].sum()
            dict_ = grouped_df.to_dict()
            labels = list(dict_.keys())
            sizes = list(dict_.values())
            # st.write(dict_)
            data = pd.DataFrame({
                                    "District_name":labels,
                                    "registered_users":sizes
                                })
            Pie_chart = px.pie(
            data,
            values="registered_users",
            names="District_name",
            title="Pie chart of Total number of phonepe Top users by District_name",
            height=300,
            width=400,
            )
            with st.expander("Pie chart of Total registered Top users by District_name"):
                st.plotly_chart(Pie_chart)
        container = st.container()
        with container:
            df = pd.read_sql("select * from aggregate_users;",conn)
            grouped_df = df.groupby(['Brand'])['count'].sum()
            dict_ = grouped_df.to_dict()
            labels = list(dict_.keys())
            sizes = list(dict_.values())
            # st.write(dict_)
            data = pd.DataFrame({
                                    "Brand":labels,
                                    "registered_users":sizes
                                })
            Pie_chart = px.pie(
            data,
            values="registered_users",
            names="Brand",
            title="Pie chart of Total number of phonepe users by state",
            height=300,
            width=400,
            )
            with st.expander("Pie chart of Total registered users by Mobile brand"):
                st.plotly_chart(Pie_chart)
        with container:
            df = pd.read_sql("select * from aggregate_users;",conn)
            grouped_df = df.groupby(['State'])['count'].sum()
            dict_ = grouped_df.to_dict()
            labels = list(dict_.keys())
            sizes = list(dict_.values())
            # st.write(dict_)
            data = pd.DataFrame({
                                    "State":labels,
                                    "user_count":sizes
                                })
            Pie_chart = px.pie(
            data,
            values="user_count",
            names="State",
            title="Pie chart of Total user count by state",
            height=300,
            width=400,
            )
            with st.expander("Pie chart of Total user count by state"):
                st.plotly_chart(Pie_chart)
    
            
            container = st.container()
            def get_data():
                df = pd.read_sql("select * from aggregate_users", conn, index_col="State")
                return df

            df = get_data()

            # Create a multiselect widget for brands
            brand_options = df['Brand'].unique()
            selected_brands = st.multiselect("Select Brand(s):", brand_options)

            # Filter the DataFrame based on selected brands
            filtered_df = df[df['Brand'].isin(selected_brands)]

            # Group the data by state and brand and sum the count column
            grouped_df = filtered_df.groupby(['State', 'Brand'])['count'].sum().reset_index()

            # Create a Plotly bar chart for the user count
            fig = px.bar(
                grouped_df,
                x="State",
                y="count",
                color="State",
                labels={"count": "Total Users Count"},
                title="Total Users by State and Brand"
            )

            # Display the Plotly chart in Streamlit
            st.plotly_chart(fig, use_container_width=True)

    def drop_downs():
        def Q1():
            with container:
                df = pd.read_sql("select * from top_users;",conn)
                grouped_df = df.groupby(['District_name'])['registeredUsers'].sum().sort_values(ascending=False).reset_index()
                top_10_df = grouped_df.iloc[:10]
                # st.write(top_10_df)
                bar_chart1 = px.bar(
                    top_10_df,
                    x="District_name",
                    y="registeredUsers",
                    color = "District_name",
                    title="Top 10 Registered Users by District Name",
                )
                st.plotly_chart(bar_chart1)
        def Q2():
            with container:
                df = pd.read_sql("select * from top_users;",conn)
                grouped_df = df.groupby(['State'])['registeredUsers'].sum().sort_values(ascending=False).reset_index()
                top_10_df = grouped_df.iloc[:10]
                # st.write(top_10_df)
                bar_chart2 = px.bar(
                    top_10_df,
                    x="State",
                    y="registeredUsers",
                    color = "State",
                    title="Top 10 Registered Users by State",
                )
                st.plotly_chart(bar_chart2)
        def Q3():
            with container:
                df = pd.read_sql("select * from top_users;",conn)
                grouped_df = df.groupby(['Year'])['registeredUsers'].sum().sort_values(ascending=False).reset_index()
                # st.write(top_10_df)
                bar_chart3 = px.bar(
                    grouped_df,
                    x="Year",
                    y="registeredUsers",
                    color = "Year",
                    title="Total registered users by year",
                )
                st.plotly_chart(bar_chart3)
        def Q4():
            with container:
                df = pd.read_sql("select * from aggregated_transactions;",conn)
                data_amount = df.groupby(['State'])['Transaction_Amount'].mean().reset_index()
                bar_chart4 = px.bar(
                            data_amount, 
                            x="State", 
                            y="Transaction_Amount", 
                            color="State", 
                            title="Average Transaction Amount by State"
                )
                st.plotly_chart(bar_chart4)
        def Q5():
            with container:
                df = pd.read_sql("select * from aggregated_transactions;",conn)
                data_count = df.groupby(['State'])['Transaction_count'].mean().reset_index()
                bar_chart5 = px.bar(
                            data_count, 
                            x="State", 
                            y="Transaction_count", 
                            color="State", 
                            title="Average Transaction count by State"
                )
                st.plotly_chart(bar_chart5)
        def Q6():
            with container:
                df = pd.read_sql("select * from  map_transaction1;",conn)
                grouped_df = df.groupby(['District_name'])['Transaction_amount'].sum().sort_values(ascending=False).reset_index()
                top_5_df = grouped_df.iloc[:5]

                bar_chart6 = px.bar(
                            top_5_df,
                            x="District_name",
                            y="Transaction_amount",
                            color="District_name",
                            title="Top 5 Districts by Map Transaction Amount",
                        )
                st.plotly_chart(bar_chart6)
        def Q7():
            with container:
                df = pd.read_sql("select * from  map_transaction1;",conn)
                grouped_df = df.groupby(['State'])['Transaction_amount'].sum().sort_values(ascending=False).reset_index()
                top_5_df = grouped_df.iloc[:5]

                bar_chart7 = px.bar(
                            top_5_df,
                            x="State",
                            y="Transaction_amount",
                            color="State",
                            title="Top 5 States by Map Transaction Amount",
                        )

                
                st.plotly_chart(bar_chart7)
        def Q8():
            with container:
                df = pd.read_sql("select * from aggregated_transactions;",conn)
                count_by_trans_type = df.groupby(['Transaction_type'])['Updated_Transaction_Amount'].mean().sort_values(False).reset_index()
                bar_chart8 = px.bar(
                        count_by_trans_type,
                        x="Transaction_type",
                        y="Updated_Transaction_Amount",
                        color = "Transaction_type",
                        title="Average Transaction Amount by Transaction Type",
                    )
                st.plotly_chart(bar_chart8)
        def Q9():
            with container:
                df = pd.read_sql("select * from aggregated_transactions;",conn)
                count_by_trans_type = df.groupby(['Year'])['Transaction_Amount'].sum().sort_values(False).reset_index()
                bar_chart9 = px.bar(
                        count_by_trans_type,
                        x="Year",
                        y="Transaction_Amount",
                        color = "Year",
                        title="Total transaction Amount by year",
                    )
            st.plotly_chart(bar_chart9)
        def Q10():
            with container:
                df = pd.read_sql("select * from aggregated_transactions;",conn)
                count_by_trans_type = df.groupby(['Quater'])['Transaction_Amount'].sum().sort_values(False).reset_index()
                bar_chart10 = px.bar(
                        count_by_trans_type,
                        x="Quater",
                        y="Transaction_Amount",
                        color = "Quater",
                        title="Total transaction Amount by Quater",
                    )
                
                st.plotly_chart(bar_chart10)
        options = {
            "Top 10 Registered Users by District Name": Q1,
            "Top 10 Registered Users by State": Q2,
            "Total registered users by year": Q3,
            "Average Transaction Amount by State": Q4,
            "Average Transaction count by State": Q5,
            "Top 5 Districts by Map Transaction Amount": Q6,
            "Top 5 States by Map Transaction Amount": Q7,
            "Average Transaction Amount by Transaction Type": Q8,
            "Total transaction Amount by year": Q9,
            "Total transaction Amount by Quater": Q10,
        }

        select_box = st.selectbox(
            label="Select a question to visualize",
            options=options.keys(),
        )
        container = st.container()
        with container:
            options[select_box]()


    # Add a transactions selectbox to the beginning of the code.
    transactions = st.selectbox("Choose a function:", ["None", "Transactions","users","dropdowns"])

    # Call the selected function.
    if transactions == "Transactions":
        Transactions()
    elif transactions == "users":
        users()
    elif transactions == "dropdowns":
        drop_downs()
    container = st.container()
    
def map_visualization():
    container = st.container()
    try:
        with container:
            @st.cache_data(ttl=60 * 60)
            def load_lottie_file(filepath : str):
                with open(filepath, "r") as f:
                    gif = json.load(f)
                st_lottie(gif, speed=1, width=750, height=450)
                
            load_lottie_file("india.json")
    except:
        print("Don't raise exception")
    container = st.container()
    with container:
        def get_data():
            df = pd.read_sql("SELECT * FROM aggregated_transactions",conn,index_col="State")
            return df

        df = get_data()
        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()

        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                    "andhra-pradesh":"Andhra Pradesh",
                    "arunachal-pradesh":"Arunachal Pradesh",
                    "assam":"Assam",
                    "bihar":"Bihar",
                    "chandigarh":"Chandigarh",
                    "chhattisgarh":"Chhattisgarh",
                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                    "delhi":"Delhi",
                    "goa":"Goa",
                    "gujarat":"Gujarat",
                    "haryana":"Haryana",
                    "himachal-pradesh":"Himachal Pradesh",
                    "jammu-&-kashmir":"Jammu & Kashmir",
                    "jharkhand":"Jharkhand",
                    "karnataka":"Karnataka",
                    "kerala":"Kerala",
                    "ladakh":"Ladakh",
                    "lakshadweep":"Lakshadweep",
                    "madhya-pradesh":"Madhya Pradesh",
                    "maharashtra":"Maharashtra",
                    "manipur":"Manipur",
                    "meghalaya":"Meghalaya",
                    "mizoram":"Mizoram",
                    "nagaland":"Nagaland",
                    "odisha":"Odisha",
                    "puducherry":"Puducherry",
                    "punjab":"Punjab",
                    "rajasthan":"Rajasthan",
                    "sikkim":"Sikkim",
                    "tamil-nadu":"Tamil Nadu",
                    "telangana":"Telangana",
                    "tripura":"Tripura",
                    "uttar-pradesh":"Uttar Pradesh",
                    "uttarakhand":"Uttarakhand",
                    "west-bengal":"West Bengal"}

        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

        fig = px.choropleth(
            data_amount,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Transaction_Amount',
            color_continuous_scale=px.colors.diverging.BrBG
        )

        fig.update_geos(fitbounds="locations", visible=False)
        # Add a title to the graph
        fig.update_layout(title='Choropleth Map of Transaction Amount by State')

        # Plot the map in Streamlit
        with st.expander("Choropleth Map of Transaction Amount by State"):
            st.plotly_chart(fig)
    container = st.container()
    with container:
        def get_data():
            df = pd.read_sql("SELECT * FROM aggregated_transactions",conn,index_col="State")
            return df

        df = get_data()
        data_count = df.groupby(['State'])['Transaction_count'].sum().reset_index()

        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                    "andhra-pradesh":"Andhra Pradesh",
                    "arunachal-pradesh":"Arunachal Pradesh",
                    "assam":"Assam",
                    "bihar":"Bihar",
                    "chandigarh":"Chandigarh",
                    "chhattisgarh":"Chhattisgarh",
                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                    "delhi":"Delhi",
                    "goa":"Goa",
                    "gujarat":"Gujarat",
                    "haryana":"Haryana",
                    "himachal-pradesh":"Himachal Pradesh",
                    "jammu-&-kashmir":"Jammu & Kashmir",
                    "jharkhand":"Jharkhand",
                    "karnataka":"Karnataka",
                    "kerala":"Kerala",
                    "ladakh":"Ladakh",
                    "lakshadweep":"Lakshadweep",
                    "madhya-pradesh":"Madhya Pradesh",
                    "maharashtra":"Maharashtra",
                    "manipur":"Manipur",
                    "meghalaya":"Meghalaya",
                    "mizoram":"Mizoram",
                    "nagaland":"Nagaland",
                    "odisha":"Odisha",
                    "puducherry":"Puducherry",
                    "punjab":"Punjab",
                    "rajasthan":"Rajasthan",
                    "sikkim":"Sikkim",
                    "tamil-nadu":"Tamil Nadu",
                    "telangana":"Telangana",
                    "tripura":"Tripura",
                    "uttar-pradesh":"Uttar Pradesh",
                    "uttarakhand":"Uttarakhand",
                    "west-bengal":"West Bengal"}

        data_count["State"] = data_count["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

        fig = px.choropleth(
            data_count,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='Transaction_count',
            color_continuous_scale='RdBu'
        )

        fig.update_geos(fitbounds="locations", visible=False)
        # Add a title to the graph
        fig.update_layout(title='Choropleth Map of Transaction count by State')

        # Plot the map in Streamlit
        with st.expander("Choropleth Map of Transaction count by State"):
            st.plotly_chart(fig)
    container = st.container()
    with container:
        def get_data():
            df = pd.read_sql("select * from aggregate_users",conn,index_col="State")
            return df
        df = get_data()
        data_amount = df.groupby(['State'])['count'].sum().reset_index()

        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                    "andhra-pradesh":"Andhra Pradesh",
                    "arunachal-pradesh":"Arunachal Pradesh",
                    "assam":"Assam",
                    "bihar":"Bihar",
                    "chandigarh":"Chandigarh",
                    "chhattisgarh":"Chhattisgarh",
                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                    "delhi":"Delhi",
                    "goa":"Goa",
                    "gujarat":"Gujarat",
                    "haryana":"Haryana",
                    "himachal-pradesh":"Himachal Pradesh",
                    "jammu-&-kashmir":"Jammu & Kashmir",
                    "jharkhand":"Jharkhand",
                    "karnataka":"Karnataka",
                    "kerala":"Kerala",
                    "ladakh":"Ladakh",
                    "lakshadweep":"Lakshadweep",
                    "madhya-pradesh":"Madhya Pradesh",
                    "maharashtra":"Maharashtra",
                    "manipur":"Manipur",
                    "meghalaya":"Meghalaya",
                    "mizoram":"Mizoram",
                    "nagaland":"Nagaland",
                    "odisha":"Odisha",
                    "puducherry":"Puducherry",
                    "punjab":"Punjab",
                    "rajasthan":"Rajasthan",
                    "sikkim":"Sikkim",
                    "tamil-nadu":"Tamil Nadu",
                    "telangana":"Telangana",
                    "tripura":"Tripura",
                    "uttar-pradesh":"Uttar Pradesh",
                    "uttarakhand":"Uttarakhand",
                    "west-bengal":"West Bengal"}

        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

        fig = px.choropleth(
            data_amount,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='count',
            color_continuous_scale= 'oxy' 
        )

        fig.update_geos(fitbounds="locations", visible=False)
        # Add a title to the graph
        fig.update_layout(title='Choropleth Map of phonepe appopens user count by State')

        # Plot the map in Streamlit
        with st.expander("Choropleth Map of users"):
            st.plotly_chart(fig)

    container = st.container()
    with container:
        def get_data():
            df = pd.read_sql("select * from aggregate_users",conn,index_col="State")
            return df
        df = get_data()
        data_amount = df.groupby(['State'])['appOpens'].sum().reset_index()

        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                    "andhra-pradesh":"Andhra Pradesh",
                    "arunachal-pradesh":"Arunachal Pradesh",
                    "assam":"Assam",
                    "bihar":"Bihar",
                    "chandigarh":"Chandigarh",
                    "chhattisgarh":"Chhattisgarh",
                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                    "delhi":"Delhi",
                    "goa":"Goa",
                    "gujarat":"Gujarat",
                    "haryana":"Haryana",
                    "himachal-pradesh":"Himachal Pradesh",
                    "jammu-&-kashmir":"Jammu & Kashmir",
                    "jharkhand":"Jharkhand",
                    "karnataka":"Karnataka",
                    "kerala":"Kerala",
                    "ladakh":"Ladakh",
                    "lakshadweep":"Lakshadweep",
                    "madhya-pradesh":"Madhya Pradesh",
                    "maharashtra":"Maharashtra",
                    "manipur":"Manipur",
                    "meghalaya":"Meghalaya",
                    "mizoram":"Mizoram",
                    "nagaland":"Nagaland",
                    "odisha":"Odisha",
                    "puducherry":"Puducherry",
                    "punjab":"Punjab",
                    "rajasthan":"Rajasthan",
                    "sikkim":"Sikkim",
                    "tamil-nadu":"Tamil Nadu",
                    "telangana":"Telangana",
                    "tripura":"Tripura",
                    "uttar-pradesh":"Uttar Pradesh",
                    "uttarakhand":"Uttarakhand",
                    "west-bengal":"West Bengal"}

        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

        fig = px.choropleth(
            data_amount,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='State',
            color='appOpens',
            color_continuous_scale= 'turbid' 
        )

        fig.update_geos(fitbounds="locations", visible=False)
        # Add a title to the graph
        fig.update_layout(title='Choropleth Map of phonepe appopens user count by State')

        # Plot the map in Streamlit
        with st.expander("Choropleth Map of users by appOpens"):
            st.plotly_chart(fig)
    st.header("chloropeth map of Transaction amount by year and quater")
    container = st.container()
    with container:
                years = ["2018", "2019", "2020", "2021", "2022", "2023"]
                st.warning("**Note**: the data have taken from 2018 to 2022 upto four Quaters (2023 two quaters)")
                selected_year1 = st.selectbox("Select a year:", years,key="selected_year1")
                if selected_year1 == '2018':
                    check1 = st.checkbox("Quater1",key="check1")
                    if check1:
                        def get_data():
                            df = pd.read_sql("select * from q1_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check2 = st.checkbox("Quater2",key="check2")
                    if check2:
                        def get_data():
                            df = pd.read_sql("select * from q2_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check3 = st.checkbox("Quater3",key="check3")
                    if check3:
                        def get_data():
                            df = pd.read_sql("select * from q3_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check4 = st.checkbox("Quater4",key="check4")
                    if check4:
                        def get_data():
                            df = pd.read_sql("select * from q4_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year1 == '2019':
                    check1 = st.checkbox("Quater1",key="check1")
                    if check1:
                        def get_data():
                            df = pd.read_sql("select * from q1_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check2 = st.checkbox("Quater2",key="check2")
                    if check2:
                        def get_data():
                            df = pd.read_sql("select * from q2_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check3 = st.checkbox("Quater3",key="check3")
                    if check3:
                        def get_data():
                            df = pd.read_sql("select * from q3_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check4 = st.checkbox("Quater4",key="check4")
                    if check4:
                        def get_data():
                            df = pd.read_sql("select * from q4_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year1 == '2020':
                    check1 = st.checkbox("Quater1",key="check1")
                    if check1:
                        def get_data():
                            df = pd.read_sql("select * from q1_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check2 = st.checkbox("Quater2",key="check2")
                    if check2:
                        def get_data():
                            df = pd.read_sql("select * from q2_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check3 = st.checkbox("Quater3",key="check3")
                    if check3:
                        def get_data():
                            df = pd.read_sql("select * from q3_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check4 = st.checkbox("Quater4",key="check4")
                    if check4:
                        def get_data():
                            df = pd.read_sql("select * from q4_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year1 == '2021':
                    check1 = st.checkbox("Quater1",key="check1")
                    if check1:
                        def get_data():
                            df = pd.read_sql("select * from q1_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check2 = st.checkbox("Quater2",key="check2")
                    if check2:
                        def get_data():
                            df = pd.read_sql("select * from q2_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check3 = st.checkbox("Quater3",key="check3")
                    if check3:
                        def get_data():
                            df = pd.read_sql("select * from q3_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check4 = st.checkbox("Quater4",key="check4")
                    if check4:
                        def get_data():
                            df = pd.read_sql("select * from q4_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year1 == '2022':
                    check1 = st.checkbox("Quater1",key="check1")
                    if check1:
                        def get_data():
                            df = pd.read_sql("select * from q1_2022",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check2 = st.checkbox("Quater2",key="check2")
                    if check2:
                        def get_data():
                            df = pd.read_sql("select * from q2_2022",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check3 = st.checkbox("Quater3",key="check3")
                    if check3:
                        def get_data():
                            df = pd.read_sql("select * from q3_2022",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check4 = st.checkbox("Quater4",key="check4")
                    if check4:
                        def get_data():
                            df = pd.read_sql("select * from q4_2022",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year1 == '2023':
                    check1 = st.checkbox("Quater1",key="check1")
                    if check1:
                        def get_data():
                            df = pd.read_sql("select * from q1_2023",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check2 = st.checkbox("Quater2",key="check2")
                    if check2:
                        def get_data():
                            df = pd.read_sql("select * from q2_2023",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['Transaction_Amount'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Transaction_Amount',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of Transaction Amount by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
    st.header("chloropeth map of registered_users by year and quater")
    container = st.container()
    with container:
                years = ["2018", "2019", "2020", "2021", "2022"]
                st.warning("**Note**: the data have taken from 2018 to 2021 upto four Quaters (2022 one quaters)")
                selected_year2 = st.selectbox("Select a year:", years,key="selected_year2")
                if selected_year2 == '2018':
                    check11 = st.checkbox("Quater1",key="check11")
                    if check11:
                        def get_data():
                            df = pd.read_sql("select * from q1_user_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check22 = st.checkbox("Quater2",key="check22")
                    if check22:
                        def get_data():
                            df = pd.read_sql("select * from q2_user_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check33 = st.checkbox("Quater3",key="check33")
                    if check33:
                        def get_data():
                            df = pd.read_sql("select * from q3_user_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check44 = st.checkbox("Quater4",key="check44")
                    if check44:
                        def get_data():
                            df = pd.read_sql("select * from q4_user_2018",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year2 == '2019':
                    check11 = st.checkbox("Quater1",key="check11")
                    if check11:
                        def get_data():
                            df = pd.read_sql("select * from q1_user_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check22 = st.checkbox("Quater2",key="check22")
                    if check22:
                        def get_data():
                            df = pd.read_sql("select * from q2_user_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check33 = st.checkbox("Quater3",key="check33")
                    if check33:
                        def get_data():
                            df = pd.read_sql("select * from q3_user_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check44 = st.checkbox("Quater4",key="check44")
                    if check44:
                        def get_data():
                            df = pd.read_sql("select * from q4_user_2019",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year2 == '2020':
                    check11 = st.checkbox("Quater1",key="check11")
                    if check11:
                        def get_data():
                            df = pd.read_sql("select * from q1_user_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check22 = st.checkbox("Quater2",key="check22")
                    if check22:
                        def get_data():
                            df = pd.read_sql("select * from q2_user_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check33 = st.checkbox("Quater3",key="check33")
                    if check33:
                        def get_data():
                            df = pd.read_sql("select * from q3_user_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check44 = st.checkbox("Quater4",key="check44")
                    if check44:
                        def get_data():
                            df = pd.read_sql("select * from q4_user_2020",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year2 == '2021':
                    check11 = st.checkbox("Quater1",key="check11")
                    if check11:
                        def get_data():
                            df = pd.read_sql("select * from q1_user_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check22 = st.checkbox("Quater2",key="check22")
                    if check22:
                        def get_data():
                            df = pd.read_sql("select * from q2_user_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='pubugn'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check33 = st.checkbox("Quater3",key="check33")
                    if check33:
                        def get_data():
                            df = pd.read_sql("select * from q3_user_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='geyser'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    check44 = st.checkbox("Quater4",key="check44")
                    if check44:
                        def get_data():
                            df = pd.read_sql("select * from q4_user_2021",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='ylorbr' 
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                if selected_year2 == '2022':
                    check11 = st.checkbox("Quater1",key="check11")
                    if check11:
                        def get_data():
                            df = pd.read_sql("select * from q1_user_2022",conn)
                            return df
                        df = get_data()
                        data_amount = df.groupby(['State'])['registered_users'].sum().reset_index()
                        state_names = {"andaman-&-nicobar-islands":"Andaman & Nicobar",
                                    "andhra-pradesh":"Andhra Pradesh",
                                    "arunachal-pradesh":"Arunachal Pradesh",
                                    "assam":"Assam",
                                    "bihar":"Bihar",
                                    "chandigarh":"Chandigarh",
                                    "chhattisgarh":"Chhattisgarh",
                                    "dadra-&-nagar-haveli-&-daman-&-diu":"Dadra and Nagar Haveli and Daman and Diu",
                                    "delhi":"Delhi",
                                    "goa":"Goa",
                                    "gujarat":"Gujarat",
                                    "haryana":"Haryana",
                                    "himachal-pradesh":"Himachal Pradesh",
                                    "jammu-&-kashmir":"Jammu & Kashmir",
                                    "jharkhand":"Jharkhand",
                                    "karnataka":"Karnataka",
                                    "kerala":"Kerala",
                                    "ladakh":"Ladakh",
                                    "lakshadweep":"Lakshadweep",
                                    "madhya-pradesh":"Madhya Pradesh",
                                    "maharashtra":"Maharashtra",
                                    "manipur":"Manipur",
                                    "meghalaya":"Meghalaya",
                                    "mizoram":"Mizoram",
                                    "nagaland":"Nagaland",
                                    "odisha":"Odisha",
                                    "puducherry":"Puducherry",
                                    "punjab":"Punjab",
                                    "rajasthan":"Rajasthan",
                                    "sikkim":"Sikkim",
                                    "tamil-nadu":"Tamil Nadu",
                                    "telangana":"Telangana",
                                    "tripura":"Tripura",
                                    "uttar-pradesh":"Uttar Pradesh",
                                    "uttarakhand":"Uttarakhand",
                                    "west-bengal":"West Bengal"}

                        data_amount["State"] = data_amount["State"].apply(lambda x:state_names[x]) #lambda x x is list of states


                        # df = pd.read_csv("https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/active_cases_2020-07-17_0800.csv")

                        fig = px.choropleth(
                            data_amount,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='registered_users',
                            color_continuous_scale='oranges'
                        )

                        fig.update_geos(fitbounds="locations", visible=False)
                        # Add a title to the graph
                        fig.update_layout(title='Choropleth Map of registered_users by Quater')

                        # Plot the map in Streamlit
        
                        st.plotly_chart(fig)
                    
    
    with container:
        st.header("Statistical data of phonepe transactions")
        years = ["2018", "2019", "2020", "2021", "2022", "2023"]
        st.warning("**Note**: the data have taken from 2018 to 2022 upto four Quaters (2023 two quaters)")
        selected_year = st.selectbox("Select a year:", years)

        def convert(n):
            numbers = "{:,}".format(n)
            return numbers

        if selected_year == '2018':
            if st.checkbox("Quater1"):
                def get_data():
                    df = pd.read_sql("select * from q1_2018",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")


            if st.checkbox("Quater2"):
                def get_data():
                    df = pd.read_sql("select * from q2_2018",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater3"):
                def get_data():
                    df = pd.read_sql("select * from q3_2018",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater4"):
                def get_data():
                    df = pd.read_sql("select * from q4_2018",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

        elif selected_year == '2019':
            if st.checkbox("Quater1"):
                def get_data():
                    df = pd.read_sql("select * from q1_2019",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater2"):
                def get_data():
                    df = pd.read_sql("select * from q2_2019",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater3"):
                def get_data():
                    df = pd.read_sql("select * from q3_2019",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater4"):
                def get_data():
                    df = pd.read_sql("select * from q4_2019",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

        elif selected_year == '2020':
            if st.checkbox("Quater1"):
                def get_data():
                    df = pd.read_sql("select * from q1_2020",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater2"):
                def get_data():
                    df = pd.read_sql("select * from q2_2020",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater3"):
                def get_data():
                    df = pd.read_sql("select * from q3_2020",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater4"):
                def get_data():
                    df = pd.read_sql("select * from q4_2020",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

        elif selected_year == '2021':
            if st.checkbox("Quater1"):
                def get_data():
                    df = pd.read_sql("select * from q1_2021",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater2"):
                def get_data():
                    df = pd.read_sql("select * from q2_2021",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater3"):
                def get_data():
                    df = pd.read_sql("select * from q3_2021",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater4"):
                def get_data():
                    df = pd.read_sql("select * from q4_2021",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

        elif selected_year == '2022':
            if st.checkbox("Quater1"):
                def get_data():
                    df = pd.read_sql("select * from q1_2022",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater2"):
                def get_data():
                    df = pd.read_sql("select * from q2_2022",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater3"):
                def get_data():
                    df = pd.read_sql("select * from q3_2022",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater4"):
                def get_data():
                    df = pd.read_sql("select * from q4_2022",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

        elif selected_year == '2023':
            if st.checkbox("Quater1"):
                def get_data():
                    df = pd.read_sql("select * from q1_2023",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")

            if st.checkbox("Quater2"):
                def get_data():
                    df = pd.read_sql("select * from q2_2023",conn)
                    return df
                df = get_data()
                tot_trans_count = df["Transaction_count"].sum()

                tot_count = convert(tot_trans_count)

                tot_trans_amount = df["Transaction_Amount"].sum()
                amount = convert(tot_trans_amount)
                
                avg_trans_amount = df["Transaction_Amount"].mean()
                avg = int(avg_trans_amount)
                avg_amount = convert(avg)
            
                count_by_trans_type = df.groupby(['Transaction_type'])['Transaction_count'].sum().reset_index()
                transaction_types = count_by_trans_type['Transaction_type'].tolist()
                transaction_count= count_by_trans_type['Transaction_count'].tolist()
                
                st.subheader(f"**All PhonePe transactions (UPI + Cards + Wallets)**:**:violet[{tot_count}]**")
                st.subheader(f"**Total payment value**: **:violet[\u20B9{amount} Cr]**")
                st.subheader(f"**Avg. transaction value**: **:violet[\u20B9{avg_amount}]**")
                st.header(f"**:red[categories:]**")
                for i in range(len(transaction_types)):
                    container = st.container()
                    with container:
                        st.subheader(f"**{transaction_types[i]}** = **:violet[{transaction_count[i]}]**")




menu_options = ["Home", "Insights", "Map visualization", "About"]

# Create the menu bar
with st.sidebar:
    selected = option_menu("Main Menu", menu_options)

# Display the selected page
page_functions = {
    "Home": home,
    "Insights": insights,
    "Map visualization": map_visualization,
    "About": about
}
page_functions[selected]()

