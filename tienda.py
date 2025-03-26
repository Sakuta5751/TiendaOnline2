# Tienda Online Básica 🛒

# Lista de productos disponibles en la tienda
productos = [
    {"id": 1, "nombre": "Camisa", "precio": 19.99, "stock": 50},
    {"id": 2, "nombre": "Zapatos", "precio": 59.99, "stock": 30},
    {"id": 3, "nombre": "Gorra", "precio": 9.99, "stock": 100}
]

# Lista de pedidos hechos en la tienda
pedidos = [
    {"id_pedido": 101, "cliente": "juan@email.com", "productos": [1, 3], "estado": "En proceso"},
    {"id_pedido": 102, "cliente": "maria@email.com", "productos": [2], "estado": "Pendiente"}
]

# Lista de clientes registrados en la tienda
clientes = [
    {"nombre": "Juan Pérez", "email": "juan@email.com", "direccion": "Calle Falsa 123"},
    {"nombre": "María López", "email": "maria@email.com", "direccion": "Avenida Siempre Viva 742"}
]

# 📌 Agregando un nuevo producto (Reto Extra)
nuevo_producto = {"id": 4, "nombre": "Pantalón", "precio": 39.99, "stock": 75}
productos.append(nuevo_producto)

# 📌 Cambiando el estado del pedido 101 a "Entregado"
for pedido in pedidos:
    if pedido["id_pedido"] == 101:
        pedido["estado"] = "Entregado"
        break

# 📌 Encontrando todos los pedidos de un cliente por email
def pedidos_por_cliente(email):
    return [pedido for pedido in pedidos if pedido["cliente"] == email]

# Probando la función con un cliente específico
email_cliente = "juan@email.com"
pedidos_de_juan = pedidos_por_cliente(email_cliente)

# Mostrando resultados sin llaves {}
print("Lista de productos actualizada:")
for producto in productos:
    print(f'ID: {producto["id"]}, Nombre: {producto["nombre"]}, Precio: ${producto["precio"]}, Stock: {producto["stock"]}')

print("\nLista de pedidos actualizada:")
for pedido in pedidos:
    print(f'ID Pedido: {pedido["id_pedido"]}, Cliente: {pedido["cliente"]}, Productos: {", ".join(map(str, pedido["productos"]))}, Estado: {pedido["estado"]}')

print(f"\nPedidos de {email_cliente}:")
for pedido in pedidos_de_juan:
    print(f'ID Pedido: {pedido["id_pedido"]}, Cliente: {pedido["cliente"]}, Productos: {", ".join(map(str, pedido["productos"]))}, Estado: {pedido["estado"]}')
