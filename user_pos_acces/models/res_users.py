# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
from odoo import api, fields, models, _
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError, AccessError

class ResUsers(models.Model):
    _inherit = "res.users"
    
    pos_conf_ids = fields.Many2many('pos.config','pos_users_rel','user_id','pos_config_id','Puntos de Ventas')
    
    
    
