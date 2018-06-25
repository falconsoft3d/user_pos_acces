# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError, AccessError

class PosConfigUsers(models.Model):
    _inherit = "pos.config"
    
    user_ids = fields.Many2many('res.users','pos_users_rel','pos_config_id','user_id','Usuarios Autorizados POS')
    
