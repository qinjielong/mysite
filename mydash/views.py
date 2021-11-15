from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter


# Create your views here.
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import plotly.graph_objs as go

from django_plotly_dash import DjangoDash


## Sales tracker

def sales_tracker(request):
  
    app = DjangoDash('SimpleExample')      ## Initialize the app using dpd

    #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                   size="population", color="continent", hover_name="country",
                   log_x=True, size_max=60)
 
    app.layout = html.Div([
      dcc.Graph(
          id='life-exp-vs-gdp',
          figure=fig
      )
    ])

    @app.callback(
        Output('graph-with-slider', 'figure'),
        [Input('year-slider', 'value')])
    def update_figure(selected_year):
        filtered_df = df[df.year == selected_year]
        traces = []
        for i in filtered_df.continent.unique():
            df_by_continent = filtered_df[filtered_df['continent'] == i]
            traces.append(go.Scatter(
                x=df_by_continent['gdpPercap'],
                y=df_by_continent['lifeExp'],
                text=df_by_continent['country'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))

        return {
            'data': traces,
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }


    context = {}
    return render(request, 'mydash/index.html')

def index(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    data = Scatter(x=x_data,y=y_data,mode='lines',name='test',opacity=0.8,marker_color='red')
    plot_div = plot([data],output_type='div')
    context = {'plot_div':plot_div}
    return render(request,'mydash/index.html',context=context)

def session_state_view(request):

    session = request.session

    demo_count = session.get('django_plotly_dash', {})

    ind_use = demo_count.get('ind_use', 0)
    ind_use += 1
    demo_count['ind_use'] = ind_use
    session['django_plotly_dash'] = demo_count

    # Use some of the information during template rendering
    context = {'ind_use' : ind_use}
   
    return render(request, 'mydash/demo-eight.html', context=context)
