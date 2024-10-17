from fasthtml import common as fh

app,rt = fh.fast_app(live = True)

key_points = [
    "Data Science expertise",
    "Optimised pricing",
    "Personal company tuition",
    "Time series analysis",
    "Predictive maintenance",
    "Image classification",
    "Deep Learning",
    "Digital Twin modelling"
]

def CV_list(main = False):
    lim = len(key_points)
    if main: lim = 3
    return fh.Ul(*[fh.Li(o) for o in key_points[:lim]], style = "disc")

@rt('/') #for router when you get default get request by http, do get function.
def get(): 
    return fh.Titled('bo goss',
        fh.Div(fh.P('Hello Everyone!'), hx_get="/change"),
        CV_list(main = True),
        fh.P(fh.A('My CV!', href='/RUCK_cv')) #P paragraph a for hyperlink
    )

#Create route for basic CV (with reroute to homepage)
@rt('/RUCK_cv')
def RUCK_cv():
    return fh.Titled('CV',
        fh.P('This is my beautiful CV!'),
        CV_list(),
        fh.P(fh.A('Home', href='/'))
        )

#create local server
fh.serve()