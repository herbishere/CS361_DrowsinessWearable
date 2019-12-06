from flask import render_template, flash, redirect, url_for, request, jsonify, send_file, make_response
import csv
import os
from bs4 import BeautifulSoup
from app import app, db
from app.forms import DriverForm, PhysDataForm, WearableInfoForm, PhysTable, UserSettingsForm

from app.models import Driver, WearableInfo, PhysData, UserSettings



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
    drivers = Driver.query.all()  # get all drivers to display
    form = DriverForm(form_name='Drivers')

    # set choices for the dropdown menus
    form.wearable_name.choices = [(row.id, row.name)
                                  for row in WearableInfo.query.all()]
    form.driver_name.choices = [(row.id, row.driverName)
                                for row in Driver.query.all()]

    if request.method == 'GET':
        return render_template('drivers.html', title='Driver Selection', form=form, drivers=drivers)

    if form.validate_on_submit() and request.form['form_name'] == 'Drivers':
        flash('wearable: %s, driver: %s' %
              (form.wearable_name, form.driver_name))

    print("Going to redirect...")
    return redirect(url_for('drivers'))


# -------------------------------------------------------------------------------------------------------------------
# Get the Settings page
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    usersettings = UserSettings.query.all()[0]
    form = UserSettingsForm(form_name='User Settings')

    # Render Page
    if request.method == "GET":
        return render_template('settings.html', title='User Device Settings', form=form, usersetting=usersettings)
    # Submit Form and Make Changes to Local Database
    if request.method == 'POST':
        # Get the Results as a UserSettings object
        result = UserSettings()
        if request.form.get("shock") == 'y':
            result.shock = 1
        else:
            result.shock = 0

        if request.form.get("vibration") == 'y':
            result.vibration = 1
        else:
            result.vibration = 0

        if request.form.get("noise") == 'y':
            result.noise = 1
        else:
            result.noise = 0
        result.alertFrequency = int(request.form.get('alertFrequency'))
        result.drowsinessThreshold = float(
            request.form.get('drowsinessThreshold'))

        # # DEBUGGING: View Results
        # print(result)  # settings from page
        # print(usersettings)  # settings from database
        # oldSettings = usersettings

        # UPDATE values
        if result.shock != usersettings.shock:
            print("Updating shock in Database...")
            usersettings.shock = result.shock
        if result.vibration != usersettings.vibration:
            print("Updating vibration in Database...")
            usersettings.vibration = result.vibration
        if result.noise != usersettings.noise:
            print("Updating noise in Database...")
            usersettings.noise = result.noise
        if result.alertFrequency != usersettings.alertFrequency:
            print("Updating alertFrequency in Database...")
            usersettings.alertFrequency = result.alertFrequency
        if result.drowsinessThreshold != usersettings.drowsinessThreshold:
            print("Updating drowsinessThreshold in Database...")
            usersettings.drowsinessThreshold = result.drowsinessThreshold
        db.session.commit()  # Commit the changes

        # # DEBUGGING: View Differences
        # print(UserSettings.query.all()[0])  # View the Database Data
        # print(oldSettings)  # View the Old Settings

        usersettings_new = UserSettings.query.all()[0]
        form_updated = UserSettingsForm(form_name='User Settings')
        return render_template('settings.html', title='User Device Settings', form=form_updated, usersetting=usersettings_new)


#     freq = 50
#     dscore = 0.3
#     alert_password = False
#     alert_fingerprint = True
#     userdata_password = False
#     userdata_fingerprint = True

#     if request.method == 'GET':
#         print("GET")
#     elif request.method == 'POST':
#         print("POST")
#         print(request.form)

#         freq = request.form.get('num_Frequency')
#         dscore = request.form.get('num_DScore')

#         if None == request.form.get('onoff_alert_password'):
#             alert_password = False;
#         else:
#             alert_password = True;

#         if None == request.form.get('onoff_alert_fingerprint'):
#             alert_fingerprint = False;
#         else:
#             alert_password = True;

#         if None == request.form.get('onoff_userdata_password'):
#             userdata_password = False;
#         else:
#             alert_password = True;

#         if None == request.form.get('onoff_userdata_fingerprint'):
#             userdata_fingerprint = False;
#         else:
#             alert_password = True;


#     html_page = """
# <html>

# <style>
# .basic_td {
# text-align: center;
# }

# .btn_green {
# background-color: #00ff00;
# }

# .btn_red {
# background-color: #ff0000;
# }

# .btn_center {
# width: 80%;
# height: 50px;
# }

# .btn_full {
# width: 100%;
# height: 30px;
# }

# .input_center {
# width: 80%;
# }

# .input_range {
# background: #d3d3d3;
# }

# .outlined_td {
# outline: solid 1px black;
# }

# .onoff {
# width: 30px;
# height: 30px;
# }

# .settings_table {
# text-align: center;
# margin-left: auto;
# margin-right: auto;
# height: 400px;
# width: 250px;
# }
# </style>

# <head>
# <title>
# Driver Selection
# </title>
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <!-- Bootstrap -->
# <link href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
# </head>

# <body>

# <nav class="navbar navbar-default">
# <div class="container">
# <div class="navbar-header">
# <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
# <span class="sr-only">Toggle navigation</span>
# <span class="icon-bar"></span>
# <span class="icon-bar"></span>
# <span class="icon-bar"></span>
# </button>
# <a class="navbar-brand" href="/index">Anti-Drowsiness Wearable</a>
# </div>
# <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
# <ul class="nav navbar-nav">
# <li><a href="/index">Home</a></li>
# <li><a href="/drivers/">Select Drivers</a></li>
# <li><a href="/phys_data">Physiological Data</a></li>
# <li><a href="/wearable_info">Wearable Information</a></li>
# <li><a href="/settings">Alert Settings</a></li>
# </ul>
# </div>
# </div>
# </nav>

# <table class="master_table">
# <tr>
# <td>

# <form method="POST">
# <table class="settings_table" style="border:black solid 1px">
# <tr>
# <td class="basic_td" colspan="3">Alerts
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <button class="btn_green btn_center" id="btn_Shock">Shock</button>
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <button class="btn_green btn_center" id="btn_Noise">Noise</button>
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <button class="btn_red btn_center" id="btn_Vibration">Vibration</button>
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">Frequency (Hz)
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <input class="input_center input_range" type="range" name="rng_Frequency" value='""" + str(freq) + """' id="rng_Frequency" onchange="document.getElementById('num_Frequency').value = this.value">
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <input class="input_center" type="number" name="num_Frequency" value='""" + str(freq) + """' id="num_Frequency" onchange="document.getElementById('rng_Frequency').value = this.value">
# <td>
# </tr>
# <tr>
# <td style="width: 33%"></td>
# <td><button class="btn_green btn_full" id="btn_Cancel_Alerts">Cancel</button></td>
# <td><input type="submit" class="btn_red btn_full" id="btn_Apply_Alerts" value="Apply"></td>
# </tr>
# </table>
# <td>

# <table class="settings_table" style="border:black solid 1px">
# <tr>
# <td class="basic_td" colspan="3">Sensitivity
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">Drowsiness Score
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <input class="input_center input_range" type="range" name="rng_DScore" value='""" + str(dscore) + """' min="0" max="1.0" step="0.01" id="rng_DScore"
# onchange="document.getElementById('num_DScore').value = this.value">
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">
# <input class="input_center" type="number" step="any" name="num_DScore" value='""" + str(dscore) + """' id="num_DScore" onchange="document.getElementById('rng_DScore').value = this.value">
# <td>
# </tr>
# <tr>
# <td style="width: 33%"></td>
# <td><button class="btn_green btn_full" id="btn_Cancel_Sensitivity">Cancel</button></td>
# <td><input type="submit" class="btn_red btn_full" id="btn_Apply_Sensitivity" value="Apply"></td>
# </tr>
# </table>
# <td>

# <table class="settings_table" style="border:black solid 1px">
# <tr>
# <td class="basic_td" colspan="3">Security
# <td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">Alert Setting
# <td>
# </tr>
# <tr>
# <td class="basic_td outlined_td" colspan="2">Password
# </td>
# <td class="basic_td">
# <input class="onoff" type="checkbox" name="onoff_alert_password" """ + ("checked" if alert_password else "") + """>
# </td>
# </tr>
# <tr>
# <td class="basic_td outlined_td" colspan="2">Fingerprint
# </td>
# <td class="basic_td">
# <input class="onoff" type="checkbox" name="onoff_alert_fingerprint" """ + ("checked" if alert_fingerprint else "") + """>
# </td>
# </tr>
# <tr>
# <td class="basic_td" colspan="3">User Data
# <td>
# </tr>
# <tr>
# <td class="basic_td outlined_td" colspan="2">Password
# </td>
# <td class="basic_td">
# <input class="onoff" type="checkbox" name="onoff_userdata_password" """ + ("checked" if userdata_password else "") + """>
# </td>
# </tr>
# <tr>
# <td class="basic_td outlined_td" colspan="2">Fingerprint
# </td>
# <td class="basic_td">
# <input class="onoff" type="checkbox" name="onoff_userdata_fingerprint" """ + ("checked" if userdata_fingerprint else "") + """>
# </td>
# </tr>
# <tr>
# <td style="width: 33%"></td>
# <td><button class="btn_green btn_full" id="btn_Cancel_Security" onclick="window.location.reload()">Cancel</button></td>
# <td><input type="submit" class="btn_red btn_full" id="btn_Apply_Security" value="Apply"></td>
# </tr>

# </table>
# </form>
# </table>

# </html>"""

#     return html_page


# -------------------------------------------------------------------------------------------------------------------
# Get the Physiological Data page
@app.route('/phys_data', methods=['GET', 'POST'])
def phys_data():
    physData = PhysData.query.all()  # get all drivers to display
    form = PhysDataForm()
    table = PhysTable(physData)

    if request.method == 'GET':
        return render_template('phys_data.html', title='Driver Selection', form=form, physData=physData)

    elif request.method == 'POST':
        # phys data type selection
        selected = request.form.get('phys_data_type')
        print(selected)
        table.heartrate.show = table.alertstatus.show = table.timeelapsed.show = table.overalldrowsiness.show = False

        # each case adjusts which columns need to be shown
        if int(selected) == 1:
            physData = PhysData.query.with_entities(
                PhysData.date, PhysData.time, PhysData.heartrate)
            table = PhysTable(physData)
            table.heartrate.show = True

        elif int(selected) == 2:
            physData = PhysData.query.with_entities(
                PhysData.date, PhysData.time, PhysData.alertstatus, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.alertstatus.show = table.timeelapsed.show = True

        elif int(selected) == 3:
            physData = PhysData.query.with_entities(
                PhysData.date, PhysData.time, PhysData.overalldrowsiness, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.overalldrowsiness.show = table.timeelapsed.show = True

        elif int(selected) == 4:
            physData = PhysData.query.with_entities(
                PhysData.date, PhysData.time, PhysData.alertstatus, PhysData.overalldrowsiness, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.alertstatus.show = table.overalldrowsiness.show = table.timeelapsed.show = True

        elif int(selected) == 5:
            physData = PhysData.query.with_entities(
                PhysData.date, PhysData.time, PhysData.alertstatus, PhysData.overalldrowsiness, PhysData.timeelapsed)
            table = PhysTable(physData)
            table.alertstatus.show = table.overalldrowsiness.show = table.timeelapsed.show = True

        elif int(selected) == 6:  # All data
            physData = PhysData.query.all()
            table = PhysTable(physData)
            table.heartrate.show = table.alertstatus.show = table.timeelapsed.show = table.overalldrowsiness.show = True

        else:

            physData = PhysData.query.all()
            table = PhysTable(physData)
            table.heartrate.show = table.alertstatus.show = table.timeelapsed.show = table.overalldrowsiness.show = True

        # This is for downloading the table
        html = render_template('phys_data.html', title='Driver Selection', form=form, table = table)
        soup = BeautifulSoup(html, 'html.parser')
        dl_tbl = soup.find("table")
        output_rows = []
        for table_row in dl_tbl.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_rows.append(output_row)
        write_file = open(os.getcwd() + '/report.csv', 'w')
        # print("WRITE FUNC")
        # print(os.getcwd())
        with write_file as csvfile:
            #print("NEXT IS THE TABLE")
            #print(output_rows)
            writer = csv.writer(csvfile)
            writer.writerows(output_rows)
        write_file.close()
            
        return render_template('phys_data.html', title='Driver Selection', form=form, table=table)

    if form.validate_on_submit() and request.form['form_name'] == 'Drivers':
        flash('wearable: %s, driver: %s' %
              (form.wearable_name, form.driver_name))

    print("Going to redirect...")
    return redirect(url_for('phys_data'))

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
        wearable_id = request.form.get('wearable_name')  # get id from post
        # print(wearable_id)
        wearables = WearableInfo.query.filter_by(
            id=wearable_id).first()  # get specific wearable
        # print(wearable.name)
        return render_template('wearable_info.html', title='Wearable Info Selection', form=form, wearables=wearables)

    if form.validate_on_submit():
        flash('Wearable selection required'.format(
            form.wearable.name.data))
        return redirect('/index')
    return render_template('wearable_info.html', title='Wearable Info Selection', form=form, wearables=wearables)


# view to respond to xhr requests for drivers depending on wearable selection
@app.route('/_get_drivers/')
def _get_drivers():
    # parse query string for wearable id
    wearable = request.args.get('wearable', '1', type=str)
    # get the type of device from wearable id
    wearable = WearableInfo.query.filter_by(id=wearable).first()

    # (row.id, Name displayed in dropdown
    drivers = [(row.id, row.driverName) for row in Driver.query.filter_by(
        device=wearable.type).all()]  # get available drivers for device type

    return jsonify(drivers)  # send to jquery code to fill in

# -------------------------------------------------------------------------------------------------------------------
# Download physiological data table
@app.route("/files", methods=['GET', 'POST'])
def download_file():
    
    if request.method == "GET":
        # print("DL FUNC")
        # print(os.getcwd())
        return send_file('outputs/report.csv',
                 mimetype='text/csv',
                 attachment_filename='report.csv',
                 as_attachment=True)

