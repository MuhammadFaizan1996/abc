from odoo import fields, models


class Zone(models.Model):
    _name = 'zone.zone'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    zone_id = fields.Many2one('zone.zone', 'Zone', required=True)