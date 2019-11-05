from marshmallow import fields, Schema, validates, ValidationError


class LocationSchema(Schema):
    city = fields.String()
    street = fields.String()


class PersonSchema(Schema):
    id = fields.String()
    fist_name = fields.String(required=True)
    surname = fields.String()
    age = fields.Integer()
    experiens = fields.Integer()
    location = fields.Nested(LocationSchema)

    @validates('age')
    def validate_ege(self, value):
        if value > 65:
            raise ValidationError('mast be less than 65')

