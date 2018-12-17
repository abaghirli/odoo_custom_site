# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class BookCategory(models.Model):
    _name = 'library.book.category'
    _parent_store = True
    name = fields.Char('Category')
    parent_id = fields.Many2one('library.book.category', string='Parent Category', ondelete='restrict', index=True)
    child_ids = fields.One2many('library.book.category', 'parent_id', string='Child Categoties')
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You can not create recursive categories')


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    name = fields.Char('Title', required=True)
    active = fields.Boolean('Active', default=True)
    short_name = fields.Char('Short Title')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    notes = fields.Text('internal Notes')
    state = fields.Selection([('draft', 'Not Available'),
                              ('available', 'Available'),
                              ('lost', 'Lost')],
                             'State')
    description = fields.Html('Description')
    cover = fields.Binary('Book Cover')
    out_of_prints = fields.Boolean('Out Of Print?')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of pages')
    reader_rating = fields.Float('Reader Average Rating', (14, 4))
    cost_price = fields.Float('Book Cost', dp.get_precision('Book Price'))
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price', currency_field='currency_id')
    publisher_id = fields.Many2one('res.partner', string='Publisher',
                                   ondelete='set null', context={}, domain=[])

    _sql_constraints = [('name_uniq', 'UNIQUE (name)', 'Book title must be unique')]

    @api.constrains('date_release')
    def _check_release_date(self):
        for r in self:
            if r.date_release > fields.Date.today():
                raise models.ValidationError('Release date must be in the past')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    book_ids = fields.One2many('library.book', 'publisher_id', string='Published Books')
