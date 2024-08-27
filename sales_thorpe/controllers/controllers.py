# -*- coding: utf-8 -*-
# from odoo import http


# class Sales-thorpe(http.Controller):
#     @http.route('/sales-thorpe/sales-thorpe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales-thorpe/sales-thorpe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales-thorpe.listing', {
#             'root': '/sales-thorpe/sales-thorpe',
#             'objects': http.request.env['sales-thorpe.sales-thorpe'].search([]),
#         })

#     @http.route('/sales-thorpe/sales-thorpe/objects/<model("sales-thorpe.sales-thorpe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales-thorpe.object', {
#             'object': obj
#         })
