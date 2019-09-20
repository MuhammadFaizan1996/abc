# -*- coding: utf-8 -*-
{
 'name': "SAP Integration",
 'summary': "Updates unit price of Product on reference of it's ItemCode and Zone.",
 'description': """This app integrates SAP api by posting ItemCode and Zone on api link and getting unit price in response from it. Then, this response is used to update unit price of that referenced product""",
 'author': "Gapps",
 'license': "AGPL-3",
 'website': "",
 'category': 'sale',
 'version': '1.0',
 'depends': ['base','sale'],
 'data' : ['views/menu_display.xml','security/manager_group.xml','security/ir.model.access.csv','views/zone_view.xml'],
 'demo': [],
}