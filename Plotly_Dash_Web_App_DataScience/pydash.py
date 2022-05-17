from logging import _STYLES
from os import symlink
import dash
from dash import dcc
from dash import html
from dash.html.Div import Div
from dash.html.H1 import H1
from dash.html.P import P

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

 
from dash import dcc
from dash import html
import datetime
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash()

app = dash.Dash(__name__)



app.layout = html.Div(children=[
   
 html.Div(
     className='mar',
     children=[
 html.Marquee("If You Have Symptoms, Please Don't be Afraid, And try to Visit Your Nearest Doctor.")
     ],
 style={'font-size':'24px','padding':'10px','font-family':'sans-serif','background':'#7fffd485'},
 ),

    html.Div(
        className="head-1",
        children=html.Img(
            src="https://i.ibb.co/n3Jqc2j/image.png",
            style={
                  
                   'height': '500px',
                  
                   'display':'inline-block',
                
            }
        ),
    style={ 'display':'inline-block'}
            

    ),


 html.Div(
        className="head-2",style={'display': 'inline-block','vertical-align':'top','font-size':'94px','border-left':'2px solid #85818163','font-family':'sans-serif','text-align':'center','padding':'15px 9px 5px 229px','float':'right'},
        children=[
            html.P("Let's Fight With"),
            html.P("Covid-19"),
           

        ]
        ),





    html.P('HOW IT SPREADS', style={'margin-top':'72px','background':'aliceblue','font-size':'66px','margin':'48px','font-weight':'bold', 'text-align':'center','font-family':'sans-serif'}),

 html.Div(
     className="how",
     
        children=html.Img(
            
            src="https://pbs.twimg.com/media/EUv1fSOU8AA9S8R.jpg",
            style={
                   
                    'padding':'10px',
                   'height': '670px',
                   'width': '82%',
                'marginLeft': '200px',
                'marginRight': 'auto'
            }
        )

        
    ),

html.Div(
        children=html.Img(
            className="image",
            src="https://akm-img-a-in.tosshub.com/indiatoday/images/mediamanager/Covid.gif",
            style={
                    'padding':'20px 96px 19px 30px',
                    
                   'height': 'auto',
                   'width': 'auto',
                  'margin':'48px',
                  'border-right':'2px solid #d56262'   
                  
                  
            }
        ),style={'display':'inline-block'},


    ),

       
      html.H1('SYMPTOMS', style={'display':'inline','vertical-align':'top','font-size':'72px','font-weight':'bold','text-align':'center','display': 'inline-block','font-family':'sans-serif','margin-top':'33px'}),
        html.Div(
        className="symptoms",style={'display': 'inline-block','font-size':'32px','text-transform':'capitalize','vertical-align':'top','margin-top':'192px'},
        children=[

            html.Li("difficulty breathing or shortness of breath",style={'padding':'10px'}),
            html.Li("loss of speech or mobility, or confusion",style={'padding':'10px'}),
            html.Li("chest pain",style={'padding':'10px'}),
            html.Li("loss of speech or mobility",style={'padding':'10px'}),
            html.Li("Fever",style={'padding':'10px'}),
            html.Li("Cough",style={'padding':'10px'}),
            html.Li("Tiredness",style={'padding':'10px'}),
            html.Li("Loss of test or smell",style={'padding':'10px'}),
           

        ] 
        ),

        html.Div(
html.Hr()
        ),


        #  html.Div(
        # children=html.Img(
        #     className="upload-image",
        #     src="https://akm-img-a-in.tosshub.com/indiatoday/images/mediamanager/Covid.gif",
        #     style={
        #             'padding':'20px 96px 19px 30px',
                    
        #            'height': 'auto',
        #            'width': 'auto',
        #           'margin':'48px',
        #           'border-right':'2px solid #d56262'   
                  
                  
        #     }
        # ),style={'display':'inline-block'},


        

    #),
    
#Upload Code

     
    html.Div(
className='upload',
        
  children=[ 
        dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',

            'width': '63%',
            'margin-left': '115px',
            'margin-top': '200px',
            
        
        },
    

  multiple=True
     ),
  ],            



           style={'margin-left':'88px','float':'left','width':'600px','background':'aliceblue','height':'400px','display':'inline-block','margin-top':'88px'},
        ),


    html.Div(id='output-image-upload'),
html.Div(
            className='output_table',
                       style={'display':'block','padding': '10px', },

             children=[ 
                    html.Tr( [html.Th('Temp '), html.Th("Temp"),html.Th("Temp"),html.Th("Temp")]  
                    ),
                                         

               
             ] 
            +
            [
                                                        html.Tr( [html.Td('Report'), html.Td("Report"),html.Td('Report'), html.Td("Report"),]  ),
         
         
          ]

                  
             
             
             ),
        

        

        
])

def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents),
        html.Hr(),
       
    ])



@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
           
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children



        

if __name__ == '__main__':
    app.run_server(debug=True)
    
