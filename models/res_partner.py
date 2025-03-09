from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_account_payable_id = fields.Many2one(
        'account.account',
        company_dependent=True,
        string="Account Payable",
        domain="[('deprecated', '=', False), ('company_id', '=', current_company_id)]",
    )
    
    property_account_receivable_id = fields.Many2one(
        'account.account',
        company_dependent=True,
        string="Account Receivable",
        domain="[('deprecated', '=', False), ('company_id', '=', current_company_id)]",
    )

    @api.model
    def _commercial_fields(self):
        return super(ResPartner, self)._commercial_fields()

