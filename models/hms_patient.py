from odoo import models,fields,api

BLOOD_TYPES = [
    ('ab','AB'),
    ('a','A'),
    ('b','B'),
    ('o','O')
]

STATUS = [
    ('undetermined','Undetermined'),
    ('good','Good'),
    ('fair','Fair'),
    ('serious','Serious')
]

class HmsPatientStateLog(models.Model):
    _name = "hms.patient.state.log"

    patient_id=fields.Many2one(comodel_name="hms.patient")
    description=fields.Text()


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
    state=fields.Selection(STATUS, default='undetermined')
    department_id=fields.Many2one(comodel_name="hms.department")
    department_capacity=fields.Integer(related="department_id.capacity")
    doctor_id=fields.Many2many(comodel_name="hms.doctor")

    api.onchange('state')
    def state_change(self):
        for rec in self:
            vars={
                'description': 'State Changed to %s'%(rec.state),
                'patient_id' : rec.id
            }
            self.env['hms.patient.state.log'].create(vars)