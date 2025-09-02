from odoo import models,fields

BLOOD_TYPES = [
    ('ab','AB'),
    ('a','A'),
    ('b','B'),
    ('o','O')
]
class HmsPatient(models.Model):
    _name = "hms.patient"

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(BLOOD_TYPES)
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()
    department_id=fields.Many2one(comodel_name="hms.department")
    department_capacity=fields.Integer(related="department_id.capacity")
    doctor_id=fields.Many2one(comodel_name="hms.doctor")