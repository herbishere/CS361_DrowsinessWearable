
from app import db
from app.models import Driver, WearableInfo

d = Driver(device='Apple Watch', driverName='Apple Driver1', version='1.0', releaseDate='11/24/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

d = Driver(device='Fitbit', driverName='Fitbit Driver1', version='1.0', releaseDate='11/24/2019', mostCurrent='Yes')
db.session.add(d)
db.session.commit()

d = WearableInfo(name='My Wearable', battery=90, type='Apple Watch', selectedDriver='Apple Driver 1')
db.session.add(d)
db.session.commit()

drivers = Driver.query.all()
drivers

wearables = WearableInfo.query.all()
wearables
