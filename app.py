import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Tạo ứng dụng Dash
app = dash.Dash(__name__)

# Dữ liệu mẫu
df = px.data.gapminder()

# Layout của dashboard
app.layout = html.Div([
    html.H1("Dashboard Phân tích dữ liệu lớn ơi là lớn"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in df["country"].unique()],
        value="Vietnam"
    ),
    dcc.Graph(id="line-chart")
])

# Callbacks để cập nhật dữ liệu động
@app.callback(
    Output("line-chart", "figure"),
    [Input("country-dropdown", "value")]
)
def update_chart(selected_country):
    filtered_df = df[df["country"] == selected_country]
    fig = px.line(filtered_df, x="year", y="gdpPercap", title=f"GDP per Capita of {selected_country}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
