import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

All_cities_str = ["multan", "delhi", "london", "new york", "beijing", "sydney", "tokyo", "paris", "dubai", "nuuk"]


st.title("Welcome to Graph 1 :party:")

st.markdown("## Choose the following")


left_column, right_column = st.columns(2, gap="medium", vertical_alignment="bottom")

with left_column:
    city = st.button("City")
    if city:
        city_choosen = st.selectbox("City", All_cities_str)

with right_column:
    country = st.button("Country")
    if country:





def graph1(csv, name):
    years = csv["YEAR"]
    temps = csv["metANN"]

    fig = go.Figure()

    # plotting many small lines for gradient
    n = len(years)

    for i in range(n - 1):
        t = i / (n - 2)
        r = int(133 + t * (226 - 133))
        g = int(183 - t * (183 - 75))
        b = int(235 - t * (235 - 74))
        color = f"rgb({r}, {g}, {b})"

        (fig.add_trace
            (go.Scatter(
            x=years[i:i + 2],
            y=temps[i:i + 2],
            mode="lines",
            line=dict(color=color, width=3),
            showlegend=False,
            hoverinfo="skip"
        )))

    (fig.add_trace
        (go.Scatter(
        x=years,
        y=temps,
        mode="markers",
        marker=dict(size=0.1, color="rgb(0,0,0,0)"),
        showlegend=False,
        hovertemplate="%{x}: %{y:.2f°C<extra></extra>}"

    )))

    fig.update_layout(
        title=f"Temperature change in {name} from 1940 to 2026",
        xaxis_title="Year",
        yaxis_title="Temp anomally (°C)",
        plot_bgcolor="lightgrey",
        paper_bgcolor="white"
    )


    return fig

graph1()