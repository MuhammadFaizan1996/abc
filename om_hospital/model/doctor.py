# -*- coding:utf-8 -*-

from odoo import fields,models,api,_


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'hospital doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    Gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default=False)
    Related_User = fields.Many2one('res.users')