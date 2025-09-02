from odoo import models,fields

class HmsDepartment(models.Model):
    _name="hms.department"

    name=fields.Char()
    capacity=fields.Integer()
    is_opened=fields.Boolean()
    patient_ids=fields.One2many(comodel_name="hms.patient", inverse_name="department_id", string="Patient")
    doctor_ids=fields.One2many(comodel_name="hms.doctor", inverse_name="department_id", string="Doctor")