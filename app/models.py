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
        return '<Wearable: {}; Type: {}>'.format(self.name, self.type)
    