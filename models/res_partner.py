from odoo import models, fields, api

class AccountAccount(models.Model):
    _inherit = 'account.account'

    company_id = fields.Many2one(
        'res.company', 
        string='Company',
        index=True,
        readonly=False
    )

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _get_simple_domain(self):
        return [('deprecated', '=', False)]

    property_account_payable_id = fields.Many2one(
        'account.account',
        company_dependent=True,
        string="Account Payable",
        domain=lambda self: self._get_simple_domain(),
    )
    
    property_account_receivable_id = fields.Many2one(
        'account.account',
        company_dependent=True,
        string="Account Receivable",
        domain=lambda self: self._get_simple_domain(),
    )

    @api.model
    def _commercial_fields(self):
        return super(ResPartner, self)._commercial_fields()

