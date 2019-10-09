# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",
    'version': '1.0',
    'category': 'Test',
    'summary': """Managing hospital""",
    'description': """hospital management""",
    'sequence' : '9',
    'license' : 'AGPL-3',
    'author': "GApps",
    'maintainer' : 'GApps',
    'website': "http://www.yourcompany.com",
    'depends': ['base','mail','sale'],
    'data': ['security/groups.xml',
             'security/ir.model.access.csv',
             'wizards/create_appointment.xml',
             'data/sequence.xml',
             'data/data.xml',
             'views/hospital_menu_view.xml',''
             'views/appointments.xml',
             'views/doctor.xml',
             'report/report.xml',
             'report/patient_card.xml'
             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
