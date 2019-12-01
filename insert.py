
from app import db
from app.models import Driver, WearableInfo, PhysData

# Driver Database Initialization
# Apple Drivers
appleDrivers = [
    Driver(device='Apple Watch', driverName='Apple Driver1_000',
           version='1.000', releaseDate='10/10/2019', mostCurrent='No'),
    Driver(device='Apple Watch', driverName='Apple Driver1_001',
           version='1.001', releaseDate='10/15/2019', mostCurrent='No'),
    Driver(device='Apple Watch', driverName='Apple Driver1_002',
           version='1.002', releaseDate='10/24/2019', mostCurrent='Yes')
]

for driver in appleDrivers:
    db.session.add(driver)
db.session.commit()

# FitBit Drivers
fitbitDrivers = [
    Driver(device='Fitbit', driverName='Fitbit Driver1_000',
           version='1.000', releaseDate='09/04/2019', mostCurrent='No'),
    Driver(device='Fitbit', driverName='Fitbit Driver1_100',
           version='1.100', releaseDate='10/19/2019', mostCurrent='No'),
    Driver(device='Fitbit', driverName='Fitbit Driver1_101',
           version='1.101', releaseDate='11/24/2019', mostCurrent='Yes')
]

for driver in fitbitDrivers:
    db.session.add(driver)
db.session.commit()

# Necklace Drivers
necklaceDrivers = [
    Driver(device='Necklace', driverName='Necklace Driver1_000',
           version='1.000', releaseDate='11/11/2019', mostCurrent='Yes')
]

for driver in necklaceDrivers:
    db.session.add(driver)
db.session.commit()

# Back brace drivers
backbraceDrivers = [
    Driver(device='Back Brace', driverName='BackBrace Driver1_000',
           version='1.000', releaseDate='10/11/2019', mostCurrent='Yes')
]

for driver in backbraceDrivers:
    db.session.add(driver)
db.session.commit()

# Wearable Information Initialization

wearableInfo = [
    WearableInfo(name='My Wearable', battery=90, type='Apple Watch',
                 selectedDriver='Apple Driver 1_002'),
    WearableInfo(name='Your Wearable', battery=100, type='Fitbit',
                      selectedDriver='Fitbit Driver1_000'),
    WearableInfo(name='His Wearable', battery=50, type='Necklace',
                 selectedDriver='Necklace Driver1_000'),
    WearableInfo(name='Her Wearable', battery=25, type='Back Brace',
                 selectedDriver='BackBrace Driver1_000')
]

for wearable in wearableInfo:
    db.session.add(wearable)
db.session.commit()

physData = [
    PhysData(date='11-24-2019', time='12:05:05', heartrate=70,
             overalldrowsiness=0.3, alertstatus='Awake', timeelapsed='47:35:24'),
    PhysData(date='11-24-2019', time='12:05:06', heartrate=69,
             overalldrowsiness=0.29, alertstatus='Awake', timeelapsed='47:35:25'),
    PhysData(date='11-24-2019', time='12:05:07', heartrate=68,
             overalldrowsiness=0.28, alertstatus='Awake', timeelapsed='47:35:26'),
    PhysData(date='11-24-2019', time='12:05:08', heartrate=67,
             overalldrowsiness=0.27, alertstatus='Awake', timeelapsed='47:35:27')
]

for data in physData:
    db.session.add(data)
db.session.commit()

drivers = Driver.query.all()
drivers

wearables = WearableInfo.query.all()
wearables

data = PhysData.query.all()
data
