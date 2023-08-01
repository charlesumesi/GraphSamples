
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px  # requires Pandas installed

# Initialising Dash app
app = dash.Dash()

# Get stock price data
df = px.data.stocks()

def stock_prices():
    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure()
    fig.add_trace(go.Scatter(name = 'Google', x = df['date'], y = df['GOOG']))
    fig.add_trace(go.Scatter(name = 'Apple', x = df['date'], y = df['AAPL']))
    fig.add_trace(go.Scatter(name = 'Amazon', x = df['date'], y = df['AMZN']))
    fig.add_trace(go.Scatter(name = 'Facebook', x = df['date'], y = df['FB']))
    fig.add_trace(go.Scatter(name = 'Netflix', x = df['date'], y = df['NFLX']))
    fig.add_trace(go.Scatter(name = 'Microsoft', x = df['date'], y = df['MSFT']))

    fig.update_layout(
                      xaxis_title = 'Dates',
                      yaxis_title = 'Prices'
                      )
    return fig  

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Stock Prices of Top Tech Companies', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40,\
                                              'font-family':'Verdana, sans-serif'}),
    html.P('To remove a company from the chart, click on it in the legend (and vice-versa)', 
           style = {'textAlign':'center', 'marginTop':40, 'font-family':'Verdana, sans-serif'}),
    
        dcc.Graph(id = 'line_plot', figure = stock_prices())    
    ])


if __name__ == '__main__':
    app.run_server(debug=True)