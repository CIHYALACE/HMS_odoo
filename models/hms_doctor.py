from odoo import models,fields

class HmsDoctor(models.Model):
    _name="hms.doctor"

    first_name=fields.Char()
    last_name=fields.Char()
    image=fields.Binary()
    department_id=fields.Many2one(comodel_name="hms.department")
    patient_ids=fields.One2many(comodel_name="hms.patient",inverse_name="doctor_id")
    patient_first_name=fields.Char(related="patient_ids.first_name")
    patient_last_name=fields.Char(related="patient_ids.last_name")
    patient_blood_type=fields.Selection(related="patient_ids.blood_type")
