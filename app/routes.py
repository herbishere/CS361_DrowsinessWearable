from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.forms import DriverForm, PhysDataForm, WearableInfoForm, PhysTable

from app.models import Driver, WearableInfo, PhysData


@app.route('/')
@app.route('/index')
# -------------------------------------------------------------------------------------------------------------------
# Get the main home page
def index():
    return render_template('index.html', title='Anti-Drowsiness Wearable Home')

# -------------------------------------------------------------------------------------------------------------------
# Get the Driver Selection page
@app.route('/drivers/', methods=['GET', 'POST'])
def drivers():
    drivers = Driver.query.all()            #get all drivers to display
    form = DriverForm(form_name='Drivers')

    #set choices for the dropdown menus
    form.wearable_name.choices = [(row.id, row.name) for row in WearableInfo.query.all()]
    form.driver_name.choices = [(row.id, row.driverName) for row in Driver.query.all()]

    if request.method == 'GET':
        return render_template('drivers.html', title='Driver Selection', form=form, drivers=drivers)

    if form.validate_on_submit() and request.form['form_name'] == 'Drivers':
        flash('wearable: %s, driver: %s' % (form.wearable_name, form.driver_name))

    print("Going to redirect...")
    return redirect(url_for('drivers'))

    # if request.method == "POST":
    #     print("Posting on drivers")
    #     driver_id = request.form.get('wearable_name')     #get id from post
    #     # print(wearable_id)
    #     driver = Driver.query.filter_by(id=driver_id) #get specific wearable
    #     print(driver)
    #
    #     return render_template('drivers.html', title='Driver Selection', form=form, drivers=drivers, driver=driver)
    #
    # else:
    #
    # # if form.validate_on_submit():
    # #     print("good")
    # #     flash('Driver selection required'.format(
    # #         form.wearable_name.data, form.driver_name.data))
    # #     return redirect('/index')
    #
    # #
    # # print(form.errors)
    #     return render_template('drivers.html', title='Driver Selection', form=form, drivers=drivers)

    
# -------------------------------------------------------------------------------------------------------------------
# Get the Settings page
@app.route('/settings', methods=['GET','POST'])
def settings():
    freq = 50
    dscore = 0.3
    alert_password = False
    alert_fingerprint = True
    userdata_password = False
    userdata_fingerprint = True

    if request.method == 'GET':
        print("GET")
    elif request.method == 'POST':
        print("POST")
        print(request.form)

        freq = request.form.get('num_Frequency')
        dscore = request.form.get('num_DScore')

        if None == request.form.get('onoff_alert_password'):
            alert_password = False;
        else:
            alert_password = True;

        if None == request.form.get('onoff_alert_fingerprint'):
            alert_fingerprint = False;
        else:
            alert_password = True;

        if None == request.form.get('onoff_userdata_password'):
            userdata_password = False;
        else:
            alert_password = True;

        if None == request.form.get('onoff_userdata_fingerprint'):
            userdata_fingerprint = False;
        else:
            alert_password = True;


    html_page = """
<html>

<style>
.basic_td {
text-align: center;
}

.btn_green {
background-color: #00ff00;
}

.btn_red {
background-color: #ff0000;
}

.btn_center {
width: 80%;
height: 50px;
}

.btn_full {
width: 100%;
height: 30px;
}

.input_center {
width: 80%;
}

.input_range {
background: #d3d3d3;
}

.outlined_td {
outline: solid 1px black;
}

.onoff {
width: 30px;
height: 30px;
}

.settings_table {
text-align: center;
margin-left: auto;
margin-right: auto;
height: 400px;
width: 250px;
}
</style>

<head>
<title>
Driver Selection
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
<li><a href="/drivers/">Select Drivers</a></li>
<li><a href="/phys_data">Physiological Data</a></li>
<li><a href="/wearable_info">Wearable Information</a></li>
</ul>
</div>
</div>
</nav>

<table class="master_table">
<tr>
<td>

<form method="POST">
<table class="settings_table" style="border:black solid 1px">
<tr>
<td class="basic_td" colspan="3">Alerts
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<button class="btn_green btn_center" id="btn_Shock">Shock</button>
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<button class="btn_green btn_center" id="btn_Noise">Noise</button>
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<button class="btn_red btn_center" id="btn_Vibration">Vibration</button>
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">Frequency (Hz)
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<input class="input_center input_range" type="range" name="rng_Frequency" value='""" + str(freq) + """' id="rng_Frequency" onchange="document.getElementById('num_Frequency').value = this.value">
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<input class="input_center" type="number" name="num_Frequency" value='""" + str(freq) + """' id="num_Frequency" onchange="document.getElementById('rng_Frequency').value = this.value">
<td>
</tr>
<tr>
<td style="width: 33%"></td>
<td><button class="btn_green btn_full" id="btn_Cancel_Alerts">Cancel</button></td>
<td><input type="submit" class="btn_red btn_full" id="btn_Apply_Alerts" value="Apply"></td>
</tr>
</table>
<td>

<table class="settings_table" style="border:black solid 1px">
<tr>
<td class="basic_td" colspan="3">Sensitivity
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">Drowsiness Score
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<input class="input_center input_range" type="range" name="rng_DScore" value='""" + str(dscore) + """' min="0" max="1.0" step="0.01" id="rng_DScore"
onchange="document.getElementById('num_DScore').value = this.value">
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">
<input class="input_center" type="number" step="any" name="num_DScore" value='""" + str(dscore) + """' id="num_DScore" onchange="document.getElementById('rng_DScore').value = this.value">
<td>
</tr>
<tr>
<td style="width: 33%"></td>
<td><button class="btn_green btn_full" id="btn_Cancel_Sensitivity">Cancel</button></td>
<td><input type="submit" class="btn_red btn_full" id="btn_Apply_Sensitivity" value="Apply"></td>
</tr>
</table>
<td>

<table class="settings_table" style="border:black solid 1px">
<tr>
<td class="basic_td" colspan="3">Security
<td>
</tr>
<tr>
<td class="basic_td" colspan="3">Alert Setting
<td>
</tr>
<tr>
<td class="basic_td outlined_td" colspan="2">Password
</td>
<td class="basic_td">
<input class="onoff" type="checkbox" name="onoff_alert_password" """ + ("checked" if alert_password else "") + """>
</td>
</tr>
<tr>
<td class="basic_td outlined_td" colspan="2">Fingerprint
</td>
<td class="basic_td">
<input class="onoff" type="checkbox" name="onoff_alert_fingerprint" """ + ("checked" if alert_fingerprint else "") + """>
</td>
</tr>
<tr>
<td class="basic_td" colspan="3">User Data
<td>
</tr>
<tr>
<td class="basic_td outlined_td" colspan="2">Password
</td>
<td class="basic_td">
<input class="onoff" type="checkbox" name="onoff_userdata_password" """ + ("checked" if userdata_password else "") + """>
</td>
</tr>
<tr>
<td class="basic_td outlined_td" colspan="2">Fingerprint
</td>
<td class="basic_td">
<input class="onoff" type="checkbox" name="onoff_userdata_fingerprint" """ + ("checked" if userdata_fingerprint else "") + """>
</td>
</tr>
<tr>
<td style="width: 33%"></td>
<td><button class="btn_green btn_full" id="btn_Cancel_Security" onclick="window.location.reload()">Cancel</button></td>
<td><input type="submit" class="btn_red btn_full" id="btn_Apply_Security" value="Apply"></td>
</tr>

</table>
</form>
</table>

</html>"""

    return html_page
    
    
# -------------------------------------------------------------------------------------------------------------------
# Get the Physiological Data page
@app.route('/phys_data', methods=['GET', 'POST'])
def phys_data():
    physData = PhysData.query.all()            #get all drivers to display
    form = PhysDataForm()
    table = PhysTable(physData)

    #set choices for the dropdown menus
    #form.wearable_name.choices = [(row.id, row.name) for row in WearableInfo.query.all()]
    #form.driver_name.choices = [(row.id, row.driverName) for row in Driver.query.all()]

    if request.method == 'GET':
        return render_template('phys_data.html', title='Driver Selection', form=form, physData = physData )

    elif request.method == 'POST':
        selected = request.form.get('phys_data_type')       #phys data type selection
        print(selected)
        table.heartrate.show = table.alertstatus.show = table.timeelapsed.show = table.overalldrowsiness.show = False

        #each case adjusts which columns need to be shown
        if int(selected) == 1:
            physData= PhysData.query.with_entities(PhysData.date, PhysData.time, PhysData.heartrate)
            table = PhysTable(physData)
            table.heartrate.show = True

        elif int(selected) == 2:
            physData= PhysData.query.with_entities(PhysData.date, PhysData.time, PhysData.alertstatus, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.alertstatus.show = table.timeelapsed.show = True

        elif int(selected) == 3:
            physData= PhysData.query.with_entities(PhysData.date, PhysData.time, PhysData.overalldrowsiness, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.overalldrowsiness.show = table.timeelapsed.show = True

        elif int(selected) == 4:
            physData= PhysData.query.with_entities(PhysData.date, PhysData.time, PhysData.alertstatus, PhysData.overalldrowsiness, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.alertstatus.show = table.overalldrowsiness.show = table.timeelapsed.show = True

        elif int(selected) == 5:
            physData= PhysData.query.with_entities(PhysData.date, PhysData.time, PhysData.alertstatus, PhysData.overalldrowsiness, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.alertstatus.show = table.overalldrowsiness.show = table.timeelapsed.show = True

        elif int(selected) == 6: #All data
            physData= PhysData.query.all()
            table = PhysTable(physData)
            table.heartrate.show = table.alertstatus.show = table.timeelapsed.show = table.overalldrowsiness.show = True

        else:

            physData=  PhysData.query.all()
            table = PhysTable(physData)
            table.heartrate.show = table.alertstatus.show = table.timeelapsed.show = table.overalldrowsiness.show = True

        return render_template('phys_data.html', title='Driver Selection', form=form, table = table)

    if form.validate_on_submit() and request.form['form_name'] == 'Drivers':
        flash('wearable: %s, driver: %s' % (form.wearable_name, form.driver_name))

    print("Going to redirect...")
    return redirect(url_for('phys_data'))


    # physData = PhysData.query.all()
    # data = []
    # for x in physData:
    #     y = dict()
    #     y['date'] = x.date
    #     y['time'] = x.time
    #     y['heartrate'] = x.heartrate
    #     y['overalldrowsiness'] = x.overalldrowsiness
    #     y['alertstatus'] = x.alertstatus
    #     y['timeelapsed'] = x.timeelapsed
    #     data.append(y)
    #
    # # #data = {}
    # # #data[0] = {}
    # # #data[0]['date'] = '2019-12-01'
    # # #data[0]['time'] = '12:01 PM'
    # # #data[0]['heartrate'] = 57
    # # #data[0]['overalldrowsiness'] = 0.3
    # # #data[0]['alertstatus'] = 'Awake'
    # # #data[0]['timeelapsed'] = '47:35:24'
    # #
    # # #data[1] = {}
    # # #data[1]['date'] = '2019-12-01'
    # # #data[1]['time'] = '12:05 PM'
    # # #data[1]['heartrate'] = 58
    # # #data[1]['overalldrowsiness'] = 0.2
    # # #data[1]['alertstatus'] = 'Awake'
    # # #data[1]['timeelapsed'] = '47:35:24'
    # #
    # # #data[2] = {}
    # # #data[2]['date'] = '2019-12-01'
    # # #data[2]['time'] = '12:11 PM'
    # # #data[2]['heartrate'] = 91
    # # #data[2]['overalldrowsiness'] = 0.05
    # # #data[2]['alertstatus'] = 'Awake'
    # # #data[2]['timeelapsed'] = '47:38:24'
    #
    # sort_by = {}
    # sort_by[0] = "Heart Rate"
    # sort_by[1] = "Alert History"
    # sort_by[2] = "Alertness Score"
    # sort_by[3] = "Drowsiness Threshold Score"
    # sort_by[4] = "Alert Status"
    # sort_by[5] = "All Data"
    #
    # if None != request.form.get('phys_data_type'):
    #     selected = int(request.form.get('phys_data_type'))
    # else:
    #     selected = 1
    #
    # output = """<!DOCTYPE html>
    # <html>
    #   <head>
    #     <title>
    #     Physiological Data
    # </title>
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <!-- Bootstrap -->
    #     <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    #   </head>
    #   <body>
    #     <nav class="navbar navbar-default">
    #         <div class="container">
    #             <div class="navbar-header">
    #                 <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
    #                     <span class="sr-only">Toggle navigation</span>
    #                     <span class="icon-bar"></span>
    #                     <span class="icon-bar"></span>
    #                     <span class="icon-bar"></span>
    #                 </button>
    #                 <a class="navbar-brand" href="/index">Anti-Drowsiness Wearable</a>
    #             </div>
    #             <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
    #                 <ul class="nav navbar-nav">
    #                     <li><a href="/index">Home</a></li>
    #                     <li><a href="/drivers">Select Drivers</a></li>
    #                     <li><a href="/phys_data">Physiological Data</a></li>
    #                     <li><a href="/wearable_info">Wearable Information</a></li>
    #                 </ul>
    #             </div>
    #         </div>
    #     </nav>
    #     <div class="container">
    #
    # <div class = "container">
    #     <form action = "" method = "post">
    #         <fieldset>
    #             <legend>Select a type of pyshiological data to view:</legend>
    #             <div class ="form-group required">
    #                 <label class="form-control-label" for="phys_data_type">Metric</label>
    #                 <select class="form-control" id="phys_data_type" name="phys_data_type">
    #                     <option selected value="{}">{}</option>
    #                 """.format(selected, sort_by[selected - 1])
    #
    # for i in range(len(sort_by)):
    #     if i != selected - 1:
    #         output = output + """
    #             <option value="{}">{}</option>""".format(i + 1, sort_by[i])
    #
    # output = output + """
    #                 </select>
    #             </div>
    #             <div class = "form-group">
    #                 <input class="form-control" id="submit" name="submit" type="submit" value="Select Driver">
    #             </div>
    #         </fieldset>
    #     </form>
    #
    #     <h3>Physiological Data Information:</h3>
    #
    #     <table class="table">
    #         <thead><tr>"""
    #
    # output = output + "<td>Date</td>"
    # output = output + "<td>Time</td>"
    #
    # if selected == 1:
    #     output = output + "<td>Heart Rate</td>"
    # elif selected == 2:
    #     output = output + "<td>Alert Status</td>"
    #     output = output + "<td>Time Elapsed</td>"
    # elif selected == 3:
    #     output = output + "<td>Overall Drowsiness</td>"
    #     output = output + "<td>Time Elapsed</td>"
    # elif selected == 4:
    #     output = output + "<td>Alert Status</td>"
    #     output = output + "<td>Overall Drowsiness</td>"
    #     output = output + "<td>Time Elapsed</td>"
    # elif selected == 5:
    #     output = output + "<td>Alert Status</td>"
    #     output = output + "<td>Overall Drowsiness</td>"
    #     output = output + "<td>Time Elapsed</td>"
    # elif selected == 6:
    #     output = output + "<td>Heart Rate</td>"
    #     output = output + "<td>Alert Status</td>"
    #     output = output + "<td>Overall Drowsiness</td>"
    #     output = output + "<td>Time Elapsed</td>"
    #
    # output = output + """
    #     </tr></thead>
    #     <!-- VVVV REPLACE WITH CALLS TO FILL FROM DATABASE DATA -->
    #     <tbody>"""
    #
    # for i in range(len(data)):
    #     output = output + "<tr>"
    #     output = output + "<td>{}</td>".format(data[i]['date'])
    #     output = output + "<td>{}</td>".format(data[i]['time'])
    #
    #     if selected == 1:
    #         output = output + "<td>{}</td>".format(data[i]['heartrate'])
    #     elif selected == 2:
    #         output = output + "<td>{}</td>".format(data[i]['alertstatus'])
    #         output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
    #     elif selected == 3:
    #         output = output + \
    #             "<td>{}</td>".format(data[i]['overalldrowsiness'])
    #         output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
    #     elif selected == 4:
    #         output = output + "<td>{}</td>".format(data[i]['alertstatus'])
    #         output = output + \
    #             "<td>{}</td>".format(data[i]['overalldrowsiness'])
    #         output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
    #     elif selected == 5:
    #         output = output + "<td>{}</td>".format(data[i]['alertstatus'])
    #         output = output + \
    #             "<td>{}</td>".format(data[i]['overalldrowsiness'])
    #         output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
    #     elif selected == 6:
    #         output = output + "<td>{}</td>".format(data[i]['heartrate'])
    #         output = output + "<td>{}</td>".format(data[i]['alertstatus'])
    #         output = output + \
    #             "<td>{}</td>".format(data[i]['overalldrowsiness'])
    #         output = output + "<td>{}</td>".format(data[i]['timeelapsed'])
    #
    #     output = output + "</tr>"
    # output = output + """
    #         </tbody>
    #     </table>
    # </div>
    #     </div>
    #     <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    #     <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    #   </body>
    # </html>
    # """
    # return output


# -------------------------------------------------------------------------------------------------------------------
# Get the Wearable information page
@app.route('/wearable_info', methods=['GET', 'POST'])
def wearable_info():
    wearables = WearableInfo.query.all()
    # print("Printing wearables...")
    # print(wearables)


    form = WearableInfoForm()

    if request.method == "POST":
        # return "Submitted form"
        wearable_id = request.form.get('wearable_name')     #get id from post
        # print(wearable_id)
        wearables = WearableInfo.query.filter_by(id=wearable_id).first() #get specific wearable
        # print(wearable.name)
        return render_template('wearable_info.html', title='Wearable Info Selection', form=form, wearables=wearables)

    if form.validate_on_submit():
        flash('Wearable selection required'.format(
            form.wearable.name.data))
        return redirect('/index')
    return render_template('wearable_info.html', title='Wearable Info Selection', form=form, wearables=wearables)


    # wearables = {}
    # wearables[0] = {}
    # wearables[0]["id"] = 0
    # wearables[0]["name"] = "My Wearable"
    # wearables[0]["battery"] = 90
    # wearables[0]["type"] = "Samsung Galaxy Watch"
    # wearables[0]["driver"] = 4
    # wearables[1] = {}
    # wearables[1]["id"] = 1
    # wearables[1]["name"] = "Your Wearable"
    # wearables[1]["battery"] = 50
    # wearables[1]["type"] = "Apple Watch"
    # wearables[1]["driver"] = 2
    #
    # selected = 0
    #
    # if request.form.get('wearable_name') != None:
    #     selected = int(request.form.get('wearable_name'))
    #
    # output = """<!DOCTYPE html>
    # <html>
    #   <head>
    #     <title>
    #     Wearable Information
    # </title>
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <!-- Bootstrap -->
    #     <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    #   </head>
    #   <body>
    #
    #     <nav class="navbar navbar-default">
    #         <div class="container">
    #             <div class="navbar-header">
    #                 <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
    #                     <span class="sr-only">Toggle navigation</span>
    #                     <span class="icon-bar"></span>
    #                     <span class="icon-bar"></span>
    #                     <span class="icon-bar"></span>
    #                 </button>
    #                 <a class="navbar-brand" href="/index">Anti-Drowsiness Wearable</a>
    #             </div>
    #             <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
    #                 <ul class="nav navbar-nav">
    #                     <li><a href="/index">Home</a></li>
    #                     <li><a href="/drivers">Select Drivers</a></li>
    #                     <li><a href="/phys_data">Physiological Data</a></li>
    #                     <li><a href="/wearable_info">Wearable Information</a></li>
    #                 </ul>
    #             </div>
    #         </div>
    #     </nav>
    # <div class="container">
    #     <div class = "container">
    #         <form action = "" method = "post">
    #             <fieldset>
    #                 <legend>Select the wearable whose information you would like to see:</legend>
    #                     <div class ="form-group required">
    #                         <label class="form-control-label" for="wearable_name">Wearable</label>
    #                             <select class="form-control" id="wearable_name" name="wearable_name">
    #                                 <option selected value="{}">{}</option>""".format(wearables[selected]['id'], wearables[selected]['name'])
    #
    # for i in range(len(wearables)):
    #     if (wearables[i]['id'] != selected):
    #         output = output + """
    #                                 <option value="{}">{}</option>
    #                                 """.format(wearables[i]['id'], wearables[i]['name'])
    #
    # output = output + """</select>
    #                         </div>
    #                         <div class = "form-group">
    #                             <input class="form-control" id="submit" name="submit" type="submit" value="Select Driver">
    #                         </div>
    #                     </fieldset>
    #                 </form>
    #
    #                 <h1>Wearable Information</h1>
    #                 <h3><strong>Name: </strong>{}</h3>
    #                 <h3><strong>Battery %: </strong>{}</h3>
    #                 <h3><strong>Type: </strong>{}</h3>
    #                 <h3><strong>Selected Driver: </strong>{}</h3>
    #             </div>
    #         </div>
    #         <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    #         <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    #     </body>
    # </html>""".format(wearables[selected]['name'], wearables[selected]['battery'], wearables[selected]['type'], wearables[selected]['driver'])
    #
    # return output

@app.route('/_get_drivers/')    #view to respond to xhr requests for drivers depending on wearable selection
def _get_drivers():
    wearable = request.args.get('wearable', '1', type=str)      #parse query string for wearable id
    wearable = WearableInfo.query.filter_by(id = wearable).first() #get the type of device from wearable id

    #(row.id, Name displayed in dropdown
    drivers = [(row.id, row.driverName) for row in Driver.query.filter_by(device=wearable.type).all()] #get available drivers for device type

    return jsonify(drivers)     #send to jquery code to fill in

