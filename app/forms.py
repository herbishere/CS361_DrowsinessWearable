from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, HiddenField
from wtforms.validators import DataRequired
from flask_table import Table, Col
from app.models import WearableInfo

# -------------------------------------------------------------------------------------------------------------------
# Forms for the "Select Driver" Page
class DriverForm(FlaskForm):
    # wearable_name = SelectField('Wearable Name', choices =[(1, "My Wearable"), (2, "Your Wearable")], default = 1)
    # driver_name = SelectField('Driver Name', choices = [(1, "Driver 1"), (2, "Driver 2")], default = 1)
    form_name = HiddenField('Form Name')


    wearable_name = SelectField('Wearable Name', validators=[DataRequired()], id='select_wearable')
    driver_name = SelectField('Driver Name', validators=[DataRequired()], id='select_driver')


    submit = SubmitField('Select Driver')

# -------------------------------------------------------------------------------------------------------------------
# Forms for the "Physiological Data" Page
class PhysDataForm(FlaskForm):
    phys_data_type = SelectField('Metric', choices =[(1, "Heart Rate"), (2, "Alert History"), (3, "Alertness Score"), (4, "Drowsiness Threshold Score"), (5, "Alert Status"), (6, "All Data")], default = 1)
    submit = SubmitField('Select Driver')
    
class PhysTable(Table):
    classes = ['table','table-condensed']
    date = Col('Date')
    time = Col('Time')
    heartrate = Col('Heart Rate', show=False)       #don't show these columns unless called for
    alertstatus = Col('Alert Status', show=False)
    timeelapsed = Col('Time Elapsed', show=False)
    overalldrowsiness = Col('Overall Drowsiness Score', show=False)
    threshold_score = Col('Current Drowsiness threshold Score', show=False)

# -------------------------------------------------------------------------------------------------------------------
# Forms for the "Wearable Information" Page   
class WearableInfoForm(FlaskForm):
    wearables = WearableInfo.query.all()
    choices2 = []           #fill with query data to display
    # print(wearables)
    for wearable in wearables:
        x = (wearable.id, wearable.name)        #change here to display different wearable attributes in dropdown

        choices2.append(x)


    wearable_name = SelectField('Wearable Name', choices = choices2, default = 1)
    submit = SubmitField('Select Driver')
