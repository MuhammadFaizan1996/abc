from odoo import models, api
from urllib.request import urlopen
from xml.dom.minidom import parseString
import json
from urllib.parse import urlencode
from odoo.exceptions import Warning


class GAProductIntegration(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    @api.onchange('product_id')
    def product_uom_change(self):

        if self.product_id:
            if self.product_id.default_code:
                #super(GAProductIntegration, self).product_id_change()
                res = super(GAProductIntegration, self).product_uom_change()
                data = {'ItemCode': self.product_id.default_code, 'Zone': self.order_id.partner_id.zone_id.code}
                url = "http://sap.stile.com.pk/api/api/demo?"
                content = urlopen(url + urlencode(data)).read()
                self.price_unit = parseString(json.loads(str(content, 'utf-8'))).getElementsByTagName('Price')[0].childNodes[0].data
                return res

        GAProductIntegration()

