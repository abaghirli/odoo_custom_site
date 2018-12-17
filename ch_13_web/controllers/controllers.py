# -*- coding: utf-8 -*-
from odoo.http import route, request, Controller


class WebBooks(Controller):

    @route('/books', type='http', auth="user", website=True)
    def route(self):
        return request.render(
            'ch_13_web.books',
            {
                'books': request.env['library.book'].search([]),
            })