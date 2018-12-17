# -*- coding: utf-8 -*-
from odoo.http import route, request, Controller

class CustomSiteController(Controller):

    @route("/custom_channels", type="http", auth="user", website=True)
    def route(self):
        channels = request.env['mail.channel'].search([])
        return request.render("custom_site.channels", {"channels": channels})
