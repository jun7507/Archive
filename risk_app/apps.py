from django.apps import AppConfig
from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly import graph_objs as go
from dash import dcc, html
from django_plotly_dash import DjangoDash


class RiskAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "risk_app"

#  plotly dash 만들기
external_stylesheets = ['https://codpen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1('Square Root Slider Graph'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):


    x = []
    for i in range(value):
        x.append(i)

    y = []
    for i in range(value):
        y.append(i*i)

    graph = go.Scatter(
        x=x,
        y=y,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),
        autosize=True

    )
    return {'data': [graph], 'layout': layout}

app = DjangoDash('SquareRootBarPlot', external_stylesheets=external_stylesheets)

graph_style = {"backgroundColor": "#1a2d46", 'color': '#ffffff', 'height': '600px'}

app.layout = html.Div([
    html.H1('Square Root Slider Graph'),
    dcc.Graph(id='slider-graph', animate=True, style=graph_style),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(21)},  # 0부터 20까지의 마크 설정
        max=20,
        value=5,  # 초기값을 5로 설정
        step=1,
        updatemode='drag',
    ),
])

# 그래프 레이아웃에 'autosize' 옵션 추가
@app.callback(
    Output('slider-graph', 'figure'),
    [Input('slider-updatemode', 'value')]
)
def update_graph(value):
    x = list(range(value))
    y = [i ** 2 for i in x]  # 제곱값 계산

    graph = go.Bar(  # Bar 그래프 객체 생성
        x=x,
        y=y,
        marker=dict(color="LightSkyBlue"),  # 막대 색상 설정
        opacity=0.6  # 막대 투명도 설정
    )

    layout = go.Layout(
        title="Square Values Bar Plot",  # 그래프 제목 설정
        xaxis=dict(title="Number"),  # x축 제목 설정
        yaxis=dict(title="Square"),  # y축 제목 설정
        paper_bgcolor='#27293d',  # 배경 색상 설정
        plot_bgcolor='rgba(0,0,0,0)',  # 그래프 배경 색상 설정
        font=dict(color='white'),  # 글꼴 색상 설정
    )

    return {'data': [graph], 'layout': layout}