from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import DriverForm, PhysDataForm, WearableInfoForm

from app.models import Driver, WearableInfo, PhysData


@app.route('/')
@app.route('/index')
# -------------------------------------------------------------------------------------------------------------------
# Get the main home page
def index():
    return render_template('index.html', title='Anti-Drowsiness Wearable Home')

# -------------------------------------------------------------------------------------------------------------------
# Get the Driver Selection page
@app.route('/drivers', methods=['GET', 'POST'])
def drivers():
    drivers = Driver.query.all()
    form = DriverForm()
    if form.validate_on_submit():
        flash('Driver selection required'.format(
            form.wearable.name.data, form.driver_name.data))
        return redirect('/index')
    return render_template('drivers.html', title='Driver Selection', form=form, drivers=drivers)

# -------------------------------------------------------------------------------------------------------------------
# Get the Physiological Data page
@app.route('/phys_data', methods=['GET', 'POST'])
def phys_data():

    physData = PhysData.query.all()
    data = []
    for x in physData:
        y = dict()
        y['date'] = x.date
        y['time'] = x.time
        y['heartrate'] = x.heartrate
        y['overalldrowsiness'] = x.overalldrowsiness
        y['alertstatus'] = x.alertstatus
        y['timeelapsed'] = x.timeelapsed
        data.append(y)

    #data = {}
    #data[0] = {}
    #data[0]['date'] = '2019-12-01'
    #data[0]['time'] = '12:01 PM'
    #data[0]['heartrate'] = 57
    #data[0]['overalldrowsiness'] = 0.3
    #data[0]['alertstatus'] = 'Awake'
    #data[0]['timeelapsed'] = '47:35:24'

    #data[1] = {}
    #data[1]['date'] = '2019-12-01'
    #data[1]['time'] = '12:05 PM'
    #data[1]['heartrate'] = 58
    #data[1]['overalldrowsiness'] = 0.2
    #data[1]['alertstatus'] = 'Awake'
    #data[1]['timeelapsed'] = '47:35:24'

    #data[2] = {}
    #data[2]['date'] = '2019-12-01'
    #data[2]['time'] = '12:11 PM'
    #data[2]['heartrate'] = 91
    #data[2]['overalldrowsiness'] = 0.05
    #data[2]['alertstatus'] = 'Awake'
    #data[2]['timeelapsed'] = '47:38:24'

    sort_by = {}
    sort_by[0] = "Heart Rate"
    sort_by[1] = "Alert History"
    sort_by[2] = "Alertness Score"
    sort_by[3] = "Drowsiness Threshold Score"
    sort_by[4] = "Alert Status"
    sort_by[5] = "All Data"

    if None != request.form.get('phys_data_type'):
        selected = int(request.form.get('phys_data_type'))
    else:
        selected = 1

    output = """<!DOCTYPE html>
    <html>
      <head>
        <title>
        Physiological Data
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
                <legend>Select a type of pyshiological data to view:</legend>
                <div class ="form-group required">
                    <label class="form-control-label" for="phys_data_type">Metric</label>
                    <select class="form-control" id="phys_data_type" name="phys_data_type">
                        <option selected value="{}">{}</option>
                    """.format(selected, sort_by[selected - 1])

    for i in range(len(sort_by)):
        if i != selected - 1:
            output = output + """
                <option value="{}">{}</option>""".format(i + 1, sort_by[i])

    output = output + """
                    </select>
                </div>
                <div class = "form-group">
                    <input class="form-control" id="submit" name="submit" type="submit" value="Select Driver">
                </div>
            </fieldset>
        </form>

        <h3>Physiological Data Information:</h3>

        <table class="table">
            <thead><tr>"""

    output = output + "<td>Date</td>"
    output = output + "<td>Time</td>"

    if selected == 1:
        output = output + "<td>Heart Rate</td>"
    elif selected == 2:
        output = output + "<td>Alert Status</td>"
        output = output + "<td>Time Elapsed</td>"
    elif selected == 3:
        output = output + "<td>Overall Drowsiness</td>"
        output = output + "<td>Time Elapsed</td>"
    elif selected == 4:
        output = output + "<td>Alert Status</td>"
        output = output + "<td>Overall Drowsiness</td>"
        output = output + "<td>Time Elapsed</td>"
    elif selected == 5:
        output = output + "<td>Alert Status</td>"
        output = output + "<td>Overall Drowsiness</td>"
        output = output + "<td>Time Elapsed</td>"
    elif selected == 6:
        output = output + "<td>Heart Rate</td>"
        output = output + "<td>Alert Status</td>"
        output = output + "<td>Overall Drowsiness</td>"
        output = output + "<td>Time Elapsed</td>"

    output = output + """
        </tr></thead>
        <!-- VVVV REPLACE WITH CALLS TO FILL FROM DATABASE DATA -->
        <tbody>"""

    for i in range(len(data)):
        output = output + "<tr>"
        output = output + "<td>{}</td>".format(data[i]['date'])
        output = output + "<td>{}</td>".format(data[i]['time'])

        if selected == 1:
            output = output + "<td>{}</td>".format(data[i]['heartrate'])
        elif selected == 2:
            output = output + "<td>{}</td>".format(data[i]['alertstatus'])
            output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
        elif selected == 3:
            output = output + \
                "<td>{}</td>".format(data[i]['overalldrowsiness'])
            output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
        elif selected == 4:
            output = output + "<td>{}</td>".format(data[i]['alertstatus'])
            output = output + \
                "<td>{}</td>".format(data[i]['overalldrowsiness'])
            output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
        elif selected == 5:
            output = output + "<td>{}</td>".format(data[i]['alertstatus'])
            output = output + \
                "<td>{}</td>".format(data[i]['overalldrowsiness'])
            output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
        elif selected == 6:
            output = output + "<td>{}</td>".format(data[i]['heartrate'])
            output = output + "<td>{}</td>".format(data[i]['alertstatus'])
            output = output + \
                "<td>{}</td>".format(data[i]['overalldrowsiness'])
            output = output + "<td>{}</td>".format(data[i]['timeelapsed'])

        output = output + "</tr>"
    output = output + """
            </tbody>
        </table>
    </div>
        </div>
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
      </body>
    </html>
    """
    return output


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

    selected = 0

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
