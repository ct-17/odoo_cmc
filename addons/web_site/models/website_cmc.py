from odoo import api, fields, models

class WebsiteCMCTemplate(models.Models):

    _inherit = "ir.ui.view"

    is_webpage_template = fields.Boolean(string="Webpage Template")