import dash
from dash import dcc, html, Input, Output
import pandas as pd
import sqlite3
import plotly.express as px

# Load data from SQLite
conn = sqlite3.connect('db/warehouse.db')
df = pd.read_sql('SELECT * FROM sales', conn)
conn.close()
df['date'] = pd.to_datetime(df['date'])

# Initialize Dash app
app = dash.Dash(__name__)
app.title = 'Mini Data Warehouse Dashboard'

# Layout
app.layout = html.Div([
    html.H1('Mini Data Warehouse Dashboard', style={'textAlign':'center'}),
    html.Label('Select Product:'),
    dcc.Dropdown(
        id='product-dropdown',
        options=[{'label': p, 'value': p} for p in df['product'].unique()],
        multi=True,
        placeholder='All Products'
    ),
    html.Label('Select Date Range:'),
    dcc.DatePickerRange(
        id='date-picker',
        min_date_allowed=df['date'].min(),
        max_date_allowed=df['date'].max(),
        start_date=df['date'].min(),
        end_date=df['date'].max()
    ),
    dcc.Graph(id='sales-graph')
])

# Callback
@app.callback(
    Output('sales-graph', 'figure'),
    Input('product-dropdown', 'value'),
    Input('date-picker', 'start_date'),
    Input('date-picker', 'end_date')
)
def update_graph(selected_products, start_date, end_date):
    filtered_df = df.copy()
    if selected_products:
        filtered_df = filtered_df[filtered_df['product'].isin(selected_products)]
    filtered_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]
    agg_df = filtered_df.groupby('product', as_index=False)['quantity'].sum()
    fig = px.bar(agg_df, x='product', y='quantity', text='quantity', title='Sales by Product')
    fig.update_traces(textposition='outside')
    return fig

if __name__=='__main__':
    app.run(debug=True)
