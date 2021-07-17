"""
Articulo
Cliente
Venta
VentaDet
"""


class Articulo:
    def __init__(self, codig, desc, prec, stock):
        self.codigo = codig
        self.descripcion = desc
        self.precio = prec
        self.stock = stock