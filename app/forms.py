from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_table import Table, Col

# -------------------------------------------------------------------------------------------------------------------
# Forms for the "Select Driver" Page
class DriverForm(FlaskForm):
    wearable_name = SelectField('Wearable Name', choices =[(1, "My Wearable"), (2, "Your Wearable")], default = 1)
    driver_name = SelectField('Driver Name', choices = [(1, "Driver 1"), (2, "Driver 2")], default = 1)
    submit = SubmitField('Select Driver')

# -------------------------------------------------------------------------------------------------------------------
# Forms for the "Physiological Data" Page
class PhysDataForm(FlaskForm):
    phys_data_type = SelectField('Metric', choices =[(1, "Heart Rate"), (2, "Alert History"), (3, "Alertness Score"), (4, "Drowsiness Threshold Score"), (5, "Alert Status"), (6, "All Data")], default = 1)
    submit = SubmitField('Select Driver')
    
class PhysTable(Table):
    date = Col('Date')
    time = Col('Time')
    heartrate = Col('Heart Rate', show = True)
    alert_status = Col('Alert Status', show = True)
    time_elapsed = Col('Time Elapsed', show = True)
    drowsy_score = Col('Overall Drowsiness Score', show = True)
    threshold_score = Col('Current Drowsiness threshold Score', show = True)

# -------------------------------------------------------------------------------------------------------------------
# Forms for the "Wearable Information" Page   
class WearableInfoForm(FlaskForm):
    wearable_name = SelectField('Wearable Name', choices =[(1, "My Wearable"), (2, "Your Wearable")], default = 1)
    submit = SubmitField('Select Driver')
