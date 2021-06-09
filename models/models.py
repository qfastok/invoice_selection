# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    invoice_selection = fields.Selection([
        ('standard', 'Standard'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ], string='Quality', default='standard')


