# -*- coding:utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'
    patient = fields.Char(string='Patient')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'patient record'
    _order = 'id desc'  # id desc, patient_age desc

    _rec_name = 'patient_name'
    patient_name = fields.Char(string='Name', required=True)
    # name = fields.Char(string='Name', required = True)  ### alternative for _rec_name
    patient_age = fields.Integer('Age', track_visibility='always')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default=False, string='Gender')
    test = fields.Char('Test')
    doctor = fields.Many2one('hospital.doctor')
    age_group = fields.Selection([('minor', 'Minor'), ('major', 'Major')], string='Age Group', compute='set_age_group')
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    name_seq = fields.Char(string='Patient Id', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))  # automatic seq numbers
    active = fields.Boolean('Active', default=True)
    appointment_count = fields.Integer(string='Appointments', compute='get_appointment_count')
                                                                    # smart button count field

    _sql_constraints = [('patient_name_unique', 'unique(patient_name)',
                         'This name is already assigned to other employee, please enter another name')]

     # smart button action
    def open_patients_appointment(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_Id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

     # smart button compute field
    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_Id', '=', self.id)])
        self.appointment_count = count

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age >= 18:
                    rec.age_group = 'major'
                else:
                    rec.age_group = 'minor'

    @api.constrains('patient_age')
    def age_constraint(self):
        for rec in self:
            if rec.patient_age > 50:
                raise ValidationError(_('Age should be less than 50.'))

    @api.model
    def create(self, vals):  #### HERE #####
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
            # raise ValidationError(_('At least one language must be active.'))
        result = super(HospitalPatient, self).create(vals)
        return result
