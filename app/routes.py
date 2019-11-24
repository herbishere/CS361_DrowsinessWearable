from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import DriverForm, PhysDataForm, WearableInfoForm

@app.route('/')
@app.route('/index')

# -------------------------------------------------------------------------------------------------------------------
# Get the main home page
def index():
    return render_template('index.html', title = 'Anti-Drowsiness Wearable Home')

# -------------------------------------------------------------------------------------------------------------------
# Get the Driver Selection page    
@app.route('/drivers', methods=['GET', 'POST'])
def drivers():
    form = DriverForm()
    if form.validate_on_submit():
        flash('Driver selection required'.format(
            form.wearable.name.data, form.driver_name.data))
        return redirect('/index')
    return render_template('drivers.html', title = 'Driver Selection', form=form)

# -------------------------------------------------------------------------------------------------------------------
# Get the Physiological Data page   
@app.route('/phys_data', methods=['GET', 'POST'])
def phys_data():
    form = PhysDataForm()
    if form.validate_on_submit():
        flash('Metric is Required'.format(
            form.phys_data_type.name.data))
        return redirect('/index')
    return render_template('phys_data.html', title = 'Physiological Data', form=form)

# -------------------------------------------------------------------------------------------------------------------
# Get the Wearable information page    
@app.route('/wearable_info', methods=['GET', 'POST'])
def wearable_info():
    wearables = {}
    wearables[0] = {}
    wearables[0]["id"] = 0
    wearables[0]["name"] = "My Wearable"
    wearables[0]["battery"] = 90
    wearables[0]["type"] = "Samsung Galaxy Watch"
    wearables[0]["driver"] = 4
    wearables[1] = {}
    wearables[1]["id"] = 1
    wearables[1]["name"] = "Your Wearable"
    wearables[1]["battery"] = 50
    wearables[1]["type"] = "Apple Watch"
    wearables[1]["driver"] = 2

    selected = 0;

    if request.form.get('wearable_name') != None:
        selected = int(request.form.get('wearable_name'))

    output = """<!DOCTYPE html>
    <html>
      <head>
        <title>
        Wearable Information
    </title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap -->
        <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
      </head>
      <body>

        <nav class="navbar navbar-default">
            <div class="container">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="/index">Anti-Drowsiness Wearable</a>
                </div>
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li><a href="/index">Home</a></li>
                        <li><a href="/drivers">Select Drivers</a></li>
                        <li><a href="/phys_data">Physiological Data</a></li>
                        <li><a href="/wearable_info">Wearable Information</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    <div class="container">
        <div class = "container">
            <form action = "" method = "post">
                <fieldset>
                    <legend>Select the wearable whose information you would like to see:</legend>
                        <div class ="form-group required">
                            <label class="form-control-label" for="wearable_name">Wearable</label>
                                <select class="form-control" id="wearable_name" name="wearable_name">
                                    <option selected value="{}">{}</option>""".format(wearables[selected]['id'], wearables[selected]['name'])

    for i in range(len(wearables)):
        if (wearables[i]['id'] != selected):
            output = output + """
                                    <option value="{}">{}</option>
                                    """.format(wearables[i]['id'], wearables[i]['name'])

    output = output + """</select>
                            </div>
                            <div class = "form-group">
                                <input class="form-control" id="submit" name="submit" type="submit" value="Select Driver">
                            </div>
                        </fieldset>
                    </form>

                    <h1>Wearable Information</h1>
                    <h3><strong>Name: </strong>{}</h3>
                    <h3><strong>Battery %: </strong>{}</h3>
                    <h3><strong>Type: </strong>{}</h3>
                    <h3><strong>Selected Driver: </strong>{}</h3>
                </div>
            </div>
            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
            <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
        </body>
    </html>""".format(wearables[selected]['name'], wearables[selected]['battery'], wearables[selected]['type'], wearables[selected]['driver'])

    return output
