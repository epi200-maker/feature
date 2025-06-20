import pytest
from descuentos import calcular_descuento

def test_calcular_descuento():
    casos = [
        (100, 20, 80),
        (200, 50, 100),
        (150, 0, 150),
        (99.99, 10, 89.991),
        (0, 10, 0),
        (100, 100, 0),
        (100, 5, 95),
    ]
    for precio, porcentaje, esperado in casos:
        assert calcular_descuento(precio, porcentaje) == pytest.approx(esperado)
