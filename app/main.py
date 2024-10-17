from fasthtml import common as fh

app,rt = fh.fast_app(live = True)

@rt('/') #for router when you get default get request by http, do get function.
def get(): 
    return fh.Titled('Ruckapark',
        fh.Div(fh.P('Hello World!'), hx_get="/change"),
        fh.P(fh.A('My CV!', href='/RUCK_cv')) #P paragraph a for hyperlink
    )

#Create route for basic CV (with reroute to homepage)
@rt('/RUCK_cv')
def RUCK_cv():
    return fh.Titled('CV',
        fh.P('This is my beautiful CV!'),
        fh.P(fh.A('Home', href='/'))
        )

#create local server
fh.serve()