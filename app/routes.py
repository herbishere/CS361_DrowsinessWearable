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
    form = WearableInfoForm()
    if form.validate_on_submit():
        flash('Wearable is Required'.format(
            form.wearable_info.name.data))
        return redirect('/index')
    return render_template('wearable_info.html', title = 'Wearable Information', form=form)