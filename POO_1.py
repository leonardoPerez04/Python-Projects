class Cafeteria:
    def __init__(self,materia_prima,recetas_cafe,precio_cafe):   #Creacion de un constructor
        self.materia_prima = materia_prima
        self.recetas_cafe = recetas_cafe
        self.precio_cafe = precio_cafe
    def mostrar_menu(self):
        print("\n💰 Bienvenido a la Cafetería ☕")
        print("-------- Menú ------\n")
        for cafe, precio in self.precio_cafe.items():
            print(f"{cafe} - ${precio}")
            print(f"📌 Ingredientes: {self.recetas_cafe[cafe]}\n")

    def verificar_ingredientes(self, cafe):
        if cafe not in self.recetas_cafe:
            print("❌ El café no está en el menú.")
            return False

        receta = self.recetas_cafe[cafe]
        for ingrediente, cantidad in receta.items():
            if self.materia_prima.get(ingrediente, 0) < cantidad:
                print(f"⚠️ ERROR: No hay suficiente {ingrediente} para preparar {cafe}.")
                return False
        return True
    def descontar_ingredientes (self,cafe):
        receta = self.recetas_cafe[cafe]
        for ingrediente, cantidad in receta.items():
            self.materia_prima[ingrediente] -= cantidad

    def pedir_orden(self, cafe):
        if self.verificar_ingredientes(cafe):
            self.descontar_ingredientes(cafe)
            print(f"✅ {cafe} ha sido preparado con éxito.")
            return True
        return False
    
class Pedido:
    def __init__(self):
        self.cafes_pedidos = []
        self.total = 0

    def agregar_cafe(self, cafe, precio):
        self.cafes_pedidos.append(cafe)
        self.total += precio
        print(f"🛒 {cafe} agregado al pedido. Total actual: ${self.total}")

    def mostrar_total(self):
        """Muestra el total del pedido"""
        print(f"\n💳 Total a pagar: ${self.total}")
        return self.total
    
class Pago:
    def __init__(self, total):
        self.total = total

    def recibir_pago(self):
        """Recibe el pago del usuario y verifica si es suficiente"""
        total_usuario = float(input("💵 Ingrese la cantidad a pagar: $"))
        if total_usuario == self.total:
            print("✅ Pago realizado con éxito. ¡Gracias!")
            return True
        elif total_usuario < self.total:
            print("❌ Dinero insuficiente. Transacción cancelada.")
            return False
        else:
            print(f"✅ Pago realizado. Su cambio es: ${total_usuario - self.total}")
            return True
        
materia_prima = {
    "Agua": 40000,
    "Cafe en grano": 5000,
    "Leche entera": 12000,
    "Leche deslactosada": 12000,
}

recetas_cafe = {
    "Cafe Expreso": {"Agua": 250, "Cafe en grano": 100},
    "Cafe Americano": {"Agua": 250, "Cafe en grano": 80},
    "Macchiato": {"Leche entera": 250, "Cafe en grano": 80},
    "Latte": {"Leche entera": 250, "Cafe en grano": 80},
}

precios_cafe = {
    "Cafe Expreso": 80,
    "Cafe Americano": 80,
    "Macchiato": 120,
    "Latte": 110,
}

cafeteria = Cafeteria(materia_prima, recetas_cafe, precios_cafe)

while True:
    cafeteria.mostrar_menu()
    pedido = Pedido()

    while True:
        cafe_usuario = input("🛒 ¿Qué café desea ordenar?: ")
        if cafe_usuario not in precios_cafe:
            print("❌ Ese café no está en el menú. Intente de nuevo.")
            continue

        if cafeteria.pedir_orden(cafe_usuario):
            pedido.agregar_cafe(cafe_usuario, precios_cafe[cafe_usuario])

        ans = input("➕ ¿Desea ordenar otro café? (S/N): ").lower()
        if ans == 'n':
            break

    total_pedido = pedido.mostrar_total()
    pago = Pago(total_pedido)

    if pago.recibir_pago():
        print("✅ Pedido completado. ¡Disfrute su café!")
    else:
        print("❌ El pedido ha sido cancelado.")

    cerrar = input("👨‍💼 ¿Desea apagar la máquina? (S/N): ").lower()
    if cerrar == 's':
        print("🔴 Cerrando la cafetería... ¡Hasta luego!")
        break 