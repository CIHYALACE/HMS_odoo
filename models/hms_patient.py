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
    pcr = fields.Boolean(default=True)
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()
    state=fields.Selection(STATUS, default='undetermined')
    department_id=fields.Many2one(comodel_name="hms.department")
    department_capacity=fields.Integer(related="department_id.capacity")
    doctor_id=fields.Many2many(comodel_name="hms.doctor")
    state_log_ids = fields.One2many(
        comodel_name="hms.patient.state.log",
        inverse_name="patient_id",
        string="State Logs"
    )

    @api.onchange('state')
    def _onchange_state(self):
        if self.state:
            return {
                'warning': {
                    'title': "State Changed",
                    'message': f"State has been changed to: {self.state}",
                    'type': 'notification',
                }
            }

    def write(self, vals):
        if 'state' in vals:
            for rec in self:
                rec.env['hms.patient.state.log'].create({
                    'description': f"State Changed to {vals['state']}",
                    'patient_id': rec.id
                })
        return super().write(vals)

    def create(self, vals):
        patient = super().create(vals)
        if 'state' in vals:
            patient.env['hms.patient.state.log'].create({
                'description': f"State Changed to {vals['state']}",
                'patient_id': patient.id
            })
        return patient

    @api.onchange('departmnet_id')
    def department_change(self):
        if self.department_id == 'Null':
            return 
    
    @api.onchange('age')
    def age_change(self):
        if self.age and self.age < 30:
            self.pcr = True
            return{
            'warning':{
                'title':"Warning",
                'message':"The Pcr Setted True Cause The Edge Under 30"
                }
            }