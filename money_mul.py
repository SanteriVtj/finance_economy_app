import numpy as np
import plotly.graph_objects as go

def money_multiplier(c, e, rr):
    return (1 + c) / (rr + e + c)

def graph_rr():
    x, y = np.linspace(.5, 2, 150), np.linspace(.5, 2, 150)
    fig = go.Figure()

    for i in np.arange(0, 1, 0.01):
        fig.add_trace(
            go.Surface(
                visible=False,
                x=x,
                y=y,
                # Setting mm matrixes as a function of money_multiplier() factor
                z=np.array([[money_multiplier(c, e, i) for c in x] for e in y])
            )
        )

    # Sets default required reserve ratio as 10%
    fig.data[10].visible = True

    steps = []
    for i in range(len(fig.data)):
        step = {
            'method': 'update',
            'args': [{'visible': [False] * len(fig.data)},
            {'title': f'Required reserve ratio: {i}%'}]
        }
        step['args'][0]['visible'][i] = True
        steps.append(step)

    slider = [{
                'active': 10,
                'pad': {'t': 50},
                'currentvalue': {'prefix': 'Required reserve multiplier-%: '},
                'steps': steps
            }]

    fig.update_layout(autosize=False, 
                      width=1000, height = 1000,
                      scene={
                                 'xaxis_title': 'Currency ration',
                                 'yaxis_title': 'Excess reserve ratio',
                                 'zaxis_title': 'Money multiplier'
                      },
                      sliders=slider
                      )
    return fig

def graph_c():
    x, y = np.linspace(.5, 2, 150), np.linspace(0, 1, 150)
    fig = go.Figure()

    for i in np.arange(.5, 2, 0.01):
        fig.add_trace(
            go.Surface(
                visible=False,
                x=x,
                y=y,
                # Setting mm matrixes as a function of money_multiplier() factor
                z=np.array([[money_multiplier(c, e, i) for c in x] for e in y])
            )
        )

    # Sets default required reserve ratio as 10%
    fig.data[10].visible = True

    steps = []
    for i in range(len(fig.data)):
        step = {
            'method': 'update',
            'args': [{'visible': [False] * len(fig.data)},
            {'title': f'Currency ratio: {i}%'}]
        }
        step['args'][0]['visible'][i] = True
        steps.append(step)

    slider = [{
                'active': 10,
                'pad': {'t': 50},
                'currentvalue': {'prefix': 'Currency ratio-%: '},
                'steps': steps
            }]

    fig.update_layout(autosize=False, 
                      width=1000, height = 1000,
                      scene={
                                 'xaxis_title': 'Excess reserve ratio',
                                 'yaxis_title': 'Required reserve rate',
                                 'zaxis_title': 'Money multiplier'
                      },
                      sliders=slider
                      )
    return fig
