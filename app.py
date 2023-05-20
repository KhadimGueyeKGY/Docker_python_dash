import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Test - page - Khadim : Python dash -> docker"),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Données exemple"}],
                "layout": {"title": "Graphique Dash"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)

