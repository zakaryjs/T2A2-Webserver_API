from init import db, ma

class Format(db.Model):
    __tablename__ = 'format'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

class FormatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'format')

format_schema = FormatSchema
formats_schema = FormatSchema(many=True)