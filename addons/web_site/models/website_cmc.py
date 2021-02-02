from odoo import api, fields, models

class WebsiteCMC(models.Model):
    _name = "web_site"

    title = fields.Text("Title")