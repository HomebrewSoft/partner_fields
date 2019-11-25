# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    activity_id = fields.Many2many(
        comodel_name='economic_activity',
        string='Actividad Económica',
        required=True,
    )
    barrio = fields.Char(string='Barrio', size=75)
    referencia = fields.Char(string='Referencia', size=125)
    phone2 = fields.Char(string='Teléfono 2', size=24)
    email2 = fields.Char(string='Correo electrónico 2', size=24)
    cia_tag_id = fields.Char(
        string='Etiquetas de la Cia',
        related="parent_id.name",
        searchable=True
    )
