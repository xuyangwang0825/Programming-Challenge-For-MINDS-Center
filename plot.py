from compute import compute
import plotly.express as px
import plotly.graph_objects as go

def plot(sentiment_result):
    x = list(range(1,15))
    y = []
    for i in sentiment_result.values():
        y.append(i["avg"])
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', name='avg sentiment'))
    fig.show()

    y = []
    for i in sentiment_result.values():
        y.append(i["count"])
    fig = go.Figure(data=go.Bar(x=x, y=y, textposition='outside'))
    fig.show()


# plot(compute())