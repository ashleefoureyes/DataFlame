import pandas as pd
import plotly.graph_objs as go
from itertools import chain


def plot_shooting_graph(shooting_df_new):
    arena_figure = go.Figure(
        data=[
            go.Scatter(
                x=shooting_df_new['X'],
                y=shooting_df_new['Y'],
                mode='markers',
                marker=dict(size=10, color='black', symbol='square'),
            )
        ],
        layout=
        go.Layout(
            hovermode='closest',
            shapes=rink_shapes(),
            yaxis=dict(
                range=[-100, 581],
                scaleanchor="x",
                scaleratio=1,
                ticks='',
                showticklabels=False),
            xaxis=dict(range=[-340.5, 340.5], ticks='', showticklabels=False),
            height=800,
            width=800,
        )
    )

    return arena_figure


# Create arena figure to plot on
# I DID NOT DRAW THIS FIGURE, TODO FIND SOURCE
def rink_shapes():
    outer_rectangle = dict(
        type='rect',
        xref='x',
        yref='y',
        x0='-250',
        y0='0',
        x1='250',
        y1='516.2',
        line=dict(width=1, ))

    outer_line = dict(
        type='line',
        xref='x',
        yref='y',
        x0='200',
        y0='580',
        x1='-200',
        y1='580',
        line=dict(width=1, ))

    outer_arc1 = dict(
        type='path',
        xref='x',
        yref='y',
        path='M 200 580 C 217 574, 247 532, 250 516.2',
        line=dict(width=1, ))

    outer_arc2 = dict(
        type='path',
        xref='x',
        yref='y',
        path='M -200 580 C -217 574, -247 532, -250 516.2',
        line=dict(width=1, ))

    center_red_line = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-250',
        y0='0',
        x1='250',
        y1='0',
        line=dict(width=1, color='rgba(255, 0, 0, 1)'))

    end_line = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-250',
        y0='516.2',
        x1='250',
        y1='516.2',
        line=dict(width=1, color='rgba(255, 0, 0, 1)'))

    blue_line = dict(
        type='rect',
        xref='x',
        yref='y',
        x0='250',
        y0='150.8',
        x1='-250',
        y1='145',
        line=dict(color='rgba(0, 0, 255, 1)', width=1),
        fillcolor='rgba(0, 0, 255, 1)')

    center_blue_spot_shape = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='2.94',
        y0='2.8',
        x1='-2.94',
        y1='-2.8',
        line=dict(color='rgba(0, 0, 255, 1)', width=1),
        fillcolor='rgba(0, 0, 255, 1)')

    red_spot1 = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='135.5',
        y0='121.8',
        x1='123.5',
        y1='110.2',
        line=dict(color='rgba(255, 0, 0, 1)', width=1),
        fillcolor='rgba(255, 0, 0, 1)')

    red_spot2 = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='-135.5',
        y0='121.8',
        x1='-123.5',
        y1='110.2',
        line=dict(color='rgba(255, 0, 0, 1)', width=1),
        fillcolor='rgba(255, 0, 0, 1)')

    red_spot3 = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='135.5',
        y0='406',
        x1='123.5',
        y1='394',
        line=dict(color='rgba(255, 0, 0, 1)', width=1),
        fillcolor='rgba(255, 0, 0, 1)')

    red_spot4 = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='-135.5',
        y0='406',
        x1='-123.5',
        y1='394',
        line=dict(color='rgba(255, 0, 0, 1)', width=1),
        fillcolor='rgba(255, 0, 0, 1)')

    red_spot_circle1 = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='217.6',
        y0='487.2',
        x1='41.2',
        y1='313.2',
        line=dict(width=1, color='rgba(255, 0, 0, 1)'))

    red_spot_circle2 = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='-217.6',
        y0='487.2',
        x1='-41.2',
        y1='313.2',
        line=dict(width=1, color='rgba(255, 0, 0, 1)'))

    center_circle = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='88.2',
        y0='88.2',
        x1='-88.2',
        y1='-88.2',
        line=dict(width=1, color='rgba(0, 0, 255, 1)'))

    parallel_line1 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='230',
        y0='416.4',
        x1='217.8',
        y1='416.4',
        line=dict(color='rgba(255, 0, 0, 1)', width=1))

    parallel_line2 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='230',
        y0='384',
        x1='217.8',
        y1='384',
        line=dict(color='rgba(255, 0, 0, 1)', width=1))

    parallel_line3 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-230',
        y0='416.4',
        x1='-217.8',
        y1='416.4',
        line=dict(color='rgba(255, 0, 0, 1)', width=1))

    parallel_line4 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-230',
        y0='384',
        x1='-217.8',
        y1='384',
        line=dict(color='rgba(255, 0, 0, 1)', width=1))

    faceoff_line1 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='141.17',
        y0='423.4',
        x1='141.17',
        y1='377',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line2 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='117.62',
        y0='423.4',
        x1='117.62',
        y1='377',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line3 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='153',
        y0='406',
        x1='105.8',
        y1='406',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line4 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='153',
        y0='394.4',
        x1='105.8',
        y1='394.4',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line5 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-141.17',
        y0='423.4',
        x1='-141.17',
        y1='377',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line6 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-117.62',
        y0='423.4',
        x1='-117.62',
        y1='377',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line7 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-153',
        y0='406',
        x1='-105.8',
        y1='406',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    faceoff_line8 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-153',
        y0='394.4',
        x1='-105.8',
        y1='394.4',
        line=dict(color='rgba(10, 10, 100, 1)', width=1))

    goal_line1 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='64.7',
        y0='516.2',
        x1='82.3',
        y1='580',
        line=dict(width=1))

    goal_line2 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='23.5',
        y0='516.2',
        x1='23.5',
        y1='493',
        line=dict(width=1))

    goal_line3 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-64.7',
        y0='516.2',
        x1='-82.3',
        y1='580',
        line=dict(width=1))

    goal_line4 = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-23.5',
        y0='516.2',
        x1='-23.5',
        y1='493',
        line=dict(width=1))

    goal_arc1 = dict(
        type='path',
        xref='x',
        yref='y',
        path='M 23.5 493 C 20 480, -20 480, -23.5 493',
        line=dict(width=1, ))

    goal_arc2 = dict(
        type='path',
        xref='x',
        yref='y',
        path='M 17.6 516.2 C 15 530, -15 530, -17.6 516.2',
        line=dict(width=1, ))

    referee_crease = dict(
        type='path',
        xref='x',
        yref='y',
        path='M ',
        line=dict(width=1, color='rgba(255, 0, 0, 1)'))

    rink_shapes = []
    # Main Rink Shape
    rink_shapes.append(outer_rectangle)
    rink_shapes.append(outer_line)
    rink_shapes.append(outer_arc1)
    rink_shapes.append(outer_arc2)

    # Main Lines Shapes
    rink_shapes.append(center_red_line)
    rink_shapes.append(end_line)
    rink_shapes.append(blue_line)

    # Faceoff Dots
    rink_shapes.append(center_blue_spot_shape)
    rink_shapes.append(red_spot1)
    rink_shapes.append(red_spot2)
    rink_shapes.append(red_spot3)
    rink_shapes.append(red_spot4)

    # Faceoff Circles
    rink_shapes.append(red_spot_circle1)
    rink_shapes.append(red_spot_circle2)
    rink_shapes.append(center_circle)
    # Faceoff Lines
    rink_shapes.append(parallel_line1)
    rink_shapes.append(parallel_line2)
    rink_shapes.append(faceoff_line1)
    rink_shapes.append(faceoff_line2)
    rink_shapes.append(faceoff_line3)
    rink_shapes.append(faceoff_line4)
    # Other Side
    rink_shapes.append(parallel_line3)
    rink_shapes.append(parallel_line4)
    rink_shapes.append(faceoff_line5)
    rink_shapes.append(faceoff_line6)
    rink_shapes.append(faceoff_line7)
    rink_shapes.append(faceoff_line8)

    # Goalie Shapes
    rink_shapes.append(goal_line1)
    rink_shapes.append(goal_line2)
    rink_shapes.append(goal_line3)
    rink_shapes.append(goal_line4)

    rink_shapes.append(goal_arc1)
    rink_shapes.append(goal_arc2)
    rink_shapes.append(referee_crease)
    return rink_shapes
