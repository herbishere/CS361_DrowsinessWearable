from app import db


class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(128))
    driverName = db.Column(db.String(128))
    version = db.Column(db.String(128))
    releaseDate = db.Column(db.String(128))
    mostCurrent = db.Column(db.String(128))

    def __repr__(self):
        return '<Driver: {}; Version: {}>'.format(self.driverName, self.version)


class WearableInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    battery = db.Column(db.Integer)
    type = db.Column(db.String(128))
    selectedDriver = db.Column(db.String(128))

    def __repr__(self):
        return '<Wearable: {}; Battery: {}; Type: {}>; Selected Driver: {}'.format(self.name, self.battery, self.type, self.selectedDriver)


class PhysData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(128))
    time = db.Column(db.String(128))
    heartrate = db.Column(db.Integer)
    overalldrowsiness = db.Column(db.Integer)
    alertstatus = db.Column(db.String(128))
    timeelapsed = db.Column(db.String(128))

    def __repr__(self):
        return '<Date: {}; Drowsiness: {}; Alert Status: {}>'.format(self.date, self.overalldrowsiness, self.alertstatus)


class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    #1-shock; 2-noise; 3-vibration
    #alertMode = db.Column(db.Integer)
    shock = db.Column(db.Integer)
    noise = db.Column(db.Integer)
    vibration = db.Column(db.Integer)
    alertFrequency = db.Column(db.Integer)

    drowsinessThreshold = db.Column(db.Float)

    def __repr__(self):
        return '<shock: {}; noise {}; vibration: {}; alertFrequency: {}; drowsinessThreshold: {}>'.format(self.shock, self.noise, self.vibration, self.alertFrequency, self.drowsinessThreshold)


db.create_all()
