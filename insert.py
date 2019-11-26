
from app import db
from app.models import Driver, WearableInfo, PhysData

# Driver Database Initialization

# Apple Drivers
d = Driver(device='Apple Watch', driverName='Apple Driver1_000', version='1.000', releaseDate='10/10/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

d = Driver(device='Apple Watch', driverName='Apple Driver1_001', version='1.001', releaseDate='10/15/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

d = Driver(device='Apple Watch', driverName='Apple Driver1_002', version='1.002', releaseDate='10/24/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

# Fitbit Drivers
d = Driver(device='Fitbit', driverName='Fitbit Driver1_000', version='1.000', releaseDate='09/04/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

d = Driver(device='Fitbit', driverName='Fitbit Driver1_100', version='1.100', releaseDate='10/19/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

d = Driver(device='Fitbit', driverName='Fitbit Driver1_101', version='1.101', releaseDate='11/24/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

# Wearable Information Initialization
d = WearableInfo(name='My Wearable', battery=90, type='Apple Watch', selectedDriver='Apple Driver 1_002')
db.session.add(d)
db.session.commit()

d = WearableInfo(name='My Wearable', battery=100, type='Fitbit', selectedDriver='Fitbit Driver1_000')
db.session.add(d)
db.session.commit()

# Physiological Data History Database
d = PhysData(date='11-24-2019', time='12:05:05', heartrate=70, overalldrowsiness=0.3, alertstatus='Awake', timeelapsed='47:35:24')
db.session.add(d)
db.session.commit()

d = PhysData(date='11-24-2019', time='12:05:06', heartrate=69, overalldrowsiness=0.29, alertstatus='Awake', timeelapsed='47:35:25')
db.session.add(d)
db.session.commit()

d = PhysData(date='11-24-2019', time='12:05:07', heartrate=68, overalldrowsiness=0.28, alertstatus='Awake', timeelapsed='47:35:26')
db.session.add(d)
db.session.commit()

d = PhysData(date='11-24-2019', time='12:05:08', heartrate=67, overalldrowsiness=0.27, alertstatus='Awake', timeelapsed='47:35:27')
db.session.add(d)
db.session.commit()

drivers = Driver.query.all()
drivers

wearables = WearableInfo.query.all()
wearables

data = PhysData.query.all()
data