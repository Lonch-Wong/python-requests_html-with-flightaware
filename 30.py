import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()  #读取机场数据

df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head() #读取航班数据



trace0 = go.Scattergeo(  #线的颜色
   locationmode = 'USA-states',
        lon = df_airports['long'],
        lat = df_airports['lat'],
        hoverinfo = 'text',
        text = df_airports['airport'],
        mode = 'lines',
        marker = dict( 
            size=2, 
            color='rgb(255, 0, 0)',
            line = dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        )
)

data = [trace0]

cluster0 = []  #每个机场的点
for i in range( len( df_flight_paths ) ):
    cluster0 .append(
        dict(
            type = 'scattergeo',
            locationmode = 'USA-states',
            lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
            lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
            mode = 'lines',
            line = dict(
                width = 1,
                color = 'red',
            ),
            opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
        )
    )

updatemenus = list([ #按钮
    dict(type="buttons",
         buttons=list([   
            dict(label = 'None',
                 method = 'update'),
            dict(label = 'Cluster 0',
                 method = 'update',
                 args = [{'annotations':cluster0}]),
        ]),
    )
])

layout = dict( title = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)', #布局
        showlegend = False, 
        geo = dict(
            scope='north america',
            projection=dict( type='azimuthal equal area' ),
            showland = True,
            landcolor = 'rgb(243, 243, 243)',
            countrycolor = 'rgb(204, 204, 204)',
        ),
 updatemenus=updatemenus
 )

fig = dict(data=data, layout=layout) #数据带入

py.plot(fig, filename='relayout_option') #实现