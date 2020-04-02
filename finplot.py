import plotly.graph_objects as go


import pandas as pd
def plotGFC(filen ):
    df=  pd.read_csv(filen+'.csv')

    # df.drop(columns = ['Open','High','Low','Adj Close','Volume'], inplace = True)


    fig = go.Figure(data = [go.Candlestick(x=df['Date'],
                            open = df['Open'],
                            high = df['High'],
                            low = df['Low'],
                            close = df['Close'])])
    fig.update_layout(xaxis_rangeslider_visible = False,
                    autosize = False,
                    width = 1800,
                    height = 1000,
                    margin = dict(
                    l = 50,
                    r = 50,
                    b = 100,
                    t = 100,
                    pad = 4)
                    )
    fig.show()

plotGFC('Now')