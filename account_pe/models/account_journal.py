
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    serie = fields.Char(string='Serie', size=3)