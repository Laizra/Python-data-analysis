import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

# short-term memory/cache


@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )

    # add "hour" column to df
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df


df = get_data_from_excel()


# line 45 wasn't working because I'd forgotten to delete: st.dataframe(df)


# ---- SIDEBAR ----
st.sidebar.header("Filter Here: ")
city = st.sidebar.multiselect(
    "Select the City: ",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type: ",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Select the Gender: ",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# can use @ to refer to a variable
#  query "adds meaning to the code, allowing the system to understand and execute actions accordingly"
df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

st.dataframe(df_selection)


# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPIs
# sum of "Total" column, no need for float cause it's meant to give a glance at the numbers so int works
total_sales = int(df_selection["Total"].sum())
# average rating will be the mean of rating column and rounded to 1 decimal
average_rating = round(df_selection["Rating"].mean(), 1)
# illustrate the rating score with emojis so we convert to int and multiply number of star emojis by average rating. rounded the rating for simplicity
star_rating = ":star:" * int(round(average_rating, 0))
# calculate average sales by transaction (idk what that means, average transaction value?)
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales: ")
    # f string to concatenate US dollar with actual values we calculated earlier. used comma as one thousand seperator?
    st.subheader(f"US $ {total_sales:,} ")
with middle_column:
    st.subheader("Average Rating: ")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales per Transaction: ")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    # why two [] on Total?
    df_selection.groupby(by=["Product line"]).sum()[
        ["Total"]].sort_values(by="Total")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    # hack: multiply the hexadecimal code with the length of the df
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour<b/>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0, 0, 0, 0)",
    yaxis=(dict(showgrid=False)),
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
