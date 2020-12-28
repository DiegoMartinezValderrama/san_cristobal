from odoo import models, fields, api

class Compra(models.Model):
    _name = 'compra.compra'
   
    fecha_compra = fields.Datetime(String='Fecha')
    descripcion_compra = fields.Char(String='Descripción')

    #det_compra_ids = fields.One2many(comodel_name='compra.det_compra', inverse_name='compra_id', string='Det. compra')


class Proveedores(models.Model):
    _name = 'compra.proveedores'

    nombre_proveedor = fields.Char(String='Nombre')
    direccion_proveedor = fields.Char(String='Direccion')
    telefono_proveedor = fields.Char(String='Telefono')

class Producto (models.Model):
    _name = 'compra.producto'

    nombre_producto = fields.Char(String='Nombre')
    precio_procucto = fields.Char(String='Precio')

class Det_Compra (models.Model):
    _name = 'compra.det_compra'

    cantidad_producto = fields.Char(String='Cantidad')
    precio_por_producto = fields.Char(String='Precio')
