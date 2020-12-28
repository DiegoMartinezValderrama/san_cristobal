# -*- coding: utf-8 -*-
from odoo import http

# class SanCristobal(http.Controller):
#     @http.route('/san_cristobal/san_cristobal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/san_cristobal/san_cristobal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('san_cristobal.listing', {
#             'root': '/san_cristobal/san_cristobal',
#             'objects': http.request.env['san_cristobal.san_cristobal'].search([]),
#         })

#     @http.route('/san_cristobal/san_cristobal/objects/<model("san_cristobal.san_cristobal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('san_cristobal.object', {
#             'object': obj
#         })