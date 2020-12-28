# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'venta.cliente'

    nombre_cliente = fields.Char(String='Nombre')
    direccion_cliente = fields.Char(String='Dirección')
    telefono_cliente = fields.Char(String='Teléfono')

    #factura(One2many)

class Factura(models.Model):
    _name = 'venta.factura'

    fecha_factura = fields.Datetime(String='Fecha de la factura')
    descripcion_factura = fields.Text(String='Descripción')

    #cliente(Many2one)
    #det_factura(One2many)

class Det_factura(models.Model):
    _name = 'venta.det_factura'

    cantidad_venta = fields.Integer(String='Cantidad de la venta')

    #factura(Many2one)
    #producto(Many2one)

