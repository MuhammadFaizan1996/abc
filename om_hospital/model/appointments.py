# -*- coding:utf-8 -*-

from odoo import fields, models, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'hospital appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def get_default_note(self):
        return "hello!!!"

    def get_default_new(self):
        return 18

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_Id = fields.Many2one('hospital.patient', string='Patient', required=True, default=get_default_new)
    patient_age = fields.Integer('Age', related='patient_Id.patient_age')
    notes = fields.Text(string='Registration Note', default=get_default_note)
    appointment_date = fields.Date(string='Date', required=True)
    appointment_lines = fields.One2many('hospital.appointment.lines','appointment_id',string='Appointment Lines')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancelled')],
                             string='Status', readonly=True, default='draft')
    doctor_notes = fields.Text(string='Note')
    pharmacy_notes = fields.Text(string='Note')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'hospital appointment lines'

    product_id = fields.Many2one('product.product','Medicine')
    product_qty = fields.Integer('Quantity')
    appointment_id = fields.Many2one('hospital.appointment',string='Appointment Id',ondelete='cascade')
