import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

data = pd.read_csv("world-happiness-report.csv")

list1 = ["Czech Republic", "Slovenia", "Kosovo", "Slovakia",  "Lithuania", "Estonia", "Poland", "Poland",
         "Romania",  "Serbia", "Latvia", "Hungary", "Croatia", "Bosnia and Herzegovina",
          "Montenegro", "Bulgaria", "Albania", "North Macedonia",'Iceland']

list2 = ["Finland", "Denmark", "Switzerland", "Netherlands", "Norway", "Sweden", "Luxembourg", "Austria",
         "Germany", "Ireland", "United Kingdom", "Belgium", "France", "Malta", "Spain", "Italy",
         "Cyprus", "Portugal", "Greece", "North Cyprus"]

list3 = ["New Zealand", "Australia", "Canada", "United States"]

list4 = ["Israel", "Bahrain", "United Arab Emirates", "Saudi Arabia", "Kuwait", "Libya", "Turkey",
        "Morocco", "Algeria", "Iraq", "Iran", "Tunisia", "Lebanon", "Palestinian Territories",
        "Jordan", "Egypt", "Yemen"]

list5 = ["Taiwan Province of China", "Japan" ,"South Korea", "Mongolia", "Hong Kong S.A.R. of China", "China", "Bhutan"]

list6 = ["Singapore", "Thailand", "Philippines", "Vietnam", "Malaysia", "Indonesia", "Laos", "Cambodia", "Myanmar"]

list7 = ["Uzbekistan", "Kazakhstan", "Moldova" ,"Kyrgyzstan", "Belarus", "Russia", "Tajikistan", "Armenia",
         "Azerbaijan", "Turkmenistan", "Georgia", "Ukraine", 'Oman','Qatar', 'Syria']

list8 =  ["Nepal", "Maldives", "Bangladesh", "Pakistan", "Sri Lanka", "India", "Afghanistan"]

list9 = ["Mauritius", "Congo (Brazzaville)", "Ivory Coast", "Cameroon", "Angola", "Benin", "Botswana",'Burkina Faso', 'Burundi',
         'Central African Republic', 'Chad', 'Comoros', 'Congo (Kinshasa)', 'Djibouti', 'Ethiopia', 'Gabon',
         'Gambia', 'Ghana', 'Guinea', 'Guyana', 'Rwanda', 'Senegal', 'Tanzania', 'Togo', 'Trinidad and Tobago',
         'Uganda',  'Sierra Leone', 'Somalia','Somaliland region', 'South Africa', 'South Sudan','Sudan',
         "Zambia",'Zimbabwe','Mozambique', 'Namibia', 'Niger','Nigeria', 'Swaziland', 'Madagascar', 'Malawi', 'Mali',  'Kenya',
         'Lesotho', 'Liberia', 'Mauritania']

list10 = ["Costa Rica", "Guatemala", "Uruguay", "Brazil", "Mexico", "Jamaica", "Panama", "Chile", "El Salvador",
         "Colombia", "Nicaragua", "Argentina", "Honduras", "Peru", "Ecuador", "Bolivia", "Paraguay", "Dominican Republic",
          "Venezuela", "Haiti", "Belize", "Cuba", "Suriname"]

def converter(country):
    if country in list1:
        return "Central and Eastern Europe"
    elif country in list2:
        return "Western Europe"
    elif country in list3:
        return "North America and ANZ"
    elif country in list4:
        return "Middle East and North Africa"
    elif country in list5:
        return "East Asia"
    elif country in list6:
        return "Southeast Asia"
    elif country in list7:
        return "Commonwealth of Independent States"
    elif country in list8:
        return "South Asia"
    elif country in list9:
        return "Sub-Saharan Africa"
    elif country in list10:
        return "Latin America and Caribbean"

data["continent"] = data["Country name"].apply(converter)

df = data
all_continents = df.continent.unique()

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.H1(children='World Happiness Scores', 
            style={'textAlign': 'center'}
            ),

    html.Div(children="Tick the boxes and/or countries to make a subselection:", 
             style={'textAlign': 'center'}
             ),
    
    dcc.Checklist(
        id="checklist",
        options=[{"label": x, "value": x} 
                 for x in all_continents],
        value=all_continents[10:],
        labelStyle={'display': 'inline-block'}
    ),
    

    dcc.Graph(id="line-chart"),
])

@app.callback(
    Output("line-chart", "figure"),
    [Input("checklist", "value")])
def update_line_chart(continents):
    mask = df.continent.isin(continents)
    fig = px.line(df[mask],
        x="year", y="Life Ladder", color='Country name')
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
