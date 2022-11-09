bruto_total = 0
descontado_total = 0
total_a_pagar = 0
impreso = f''

n = int(input('Numero de productos para descuento: '))
n_productos = int(input('Cantidad de productos: '))

for i in range(n_productos):
    descuento = 20
    cantidad_producto = int(input(f'Cantidad del producto {i+1}: '))
    precio_producto = int(input(f'Precio del producto {i+1}: '))
    precio_a_pagar_por_producto = 0
    precio_total_por_producto = 0
    descontado = 0
    bruto_total += cantidad_producto * precio_producto
    precio_total_por_producto = cantidad_producto * precio_producto
    precio_con_descuento_total_por_producto = 0
    for j in range(cantidad_producto//n):
        if descuento > 0:
            descontado += (n*precio_producto)*(descuento/100)
            precio_con_descuento_total_por_producto += (n*precio_producto)-(descuento/100)
            descuento = descuento // 2
    descontado_total+=descontado
    total_a_pagar += precio_con_descuento_total_por_producto
    impreso += f'Producto {i+1} Precio: {precio_producto} Total bruto: {precio_total_por_producto} Descontado: {descontado} A pagar: {precio_con_descuento_total_por_producto}'
print(impreso)
print(f'Total bruto de la venta: {bruto_total} Total descontado: {descontado_total} Total a pagar: {total_a_pagar}')