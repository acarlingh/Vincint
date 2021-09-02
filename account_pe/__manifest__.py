# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Account normalice peruvian',
    'depends': ['account','l10n_pe_edi'],
    'description': """
Arreglos en contabilidad para peru
    """,
    'author': "Oswaldo Lopez S. (Cabalcon S.A.C.)",
    'category': 'Accounting',
    'data': [
        'views/account_move_view.xml',
        'views/account_journal.xml',
    ],
    'application': False,
    'auto_install': False
}
