materia_prima = {
    "Agua": 40000,
    "Cafe en grano": 5000,
    "Leche entera": 12000,
    "Leche deslactosada": 12000,
}

recetas_cafe  = {
    "Cafe Expreso":{"Agua":250, "Cafe en grano":100},
    "Cafe Americano": {"Agua":250,"Cafe en grano":80},
    "Macchiato":{"Leche entera":250,"Cafe en grano":80},
    "Latte": {"Leche entera":250, "Cafe en grano":80}
}

precios_cafe = {
    "Cafe Expreso":80,
    "Cafe Americano":80,
    "Macchiato":120,
    "Latte":110
}

def pedir_orden(tipo_cafe, recetas_cafe, materia_prima):
    if tipo_cafe in recetas_cafe:
        receta = recetas_cafe[tipo_cafe]

        print("🔍 Verificando ingredientes para:", tipo_cafe)
        print("📌 Ingredientes en la receta:", list(receta.keys()))
        print("📦 Ingredientes en materia_prima:", list(materia_prima.keys()))

        for ingrediente, cantidad in receta.items():
            if materia_prima[ingrediente] < cantidad:
                print(f"⚠️ ERROR: No hay suficiente {ingrediente} para preparar {tipo_cafe}.")
                print ("❌ No pudimos procesar su orden")
                return False

            if ingrediente not in materia_prima:
                print(f"⚠️ ERROR: '{ingrediente}' no está en materia_prima.")
                print ("❌ No pudimos procesar su orden")
                return False
            
            for ingrediente, cantidad in receta.items():
                materia_prima[ingrediente] -= cantidad
                #print(f"✅ Se descontaron {cantidad} de {ingrediente}. Nuevo stock: {materia_prima[ingrediente]}")

        print("✅ Orden Aceptada")
        return True
    else:
        print("El tipo de café seleccionado no está en el menú.")
        return False

def calcular_total(orden_cliente,precios_cafe,cafe_usurio):
    if orden_cliente is True:
        pago = precios_cafe[cafe_usuario]
        print(f"Es un total de: ${pago}")
        return pago

def obtener_pago(total):
    moneda_centavos = 0.5
    moneda_peso = 1
    moneda_dos_pesos = 2
    moneda_cinco_pesos = 5
    moneda_diez_pesos = 10
    centavos = int(input("Centavos: "))
    moneda_centavos*=centavos
    pesos = int(input("Pesos: "))
    moneda_peso*=pesos
    dos_pesos = int(input("Monedas de dos pesos: "))
    moneda_dos_pesos*=dos_pesos
    cinco_pesos = int(input("Monedas de cinco pesos: "))
    moneda_cinco_pesos*=cinco_pesos
    diez_pesos = int(input("Monedas de diez pesos: "))
    moneda_diez_pesos*=diez_pesos
    total_usuario = moneda_centavos + moneda_peso + moneda_dos_pesos + moneda_cinco_pesos + moneda_diez_pesos
    if total_usuario==total:
        print("✅ Pago realizado")
        return True
    elif total_usuario<total:
        print("❌ Dinero insuficiente")
        return False
    else:
        print(f"✅ Pago realizado, su cambio es de: {total_usuario-total}")
        return True
    

while True:
    print("\n💰 Bienvenido a la Cafetería ☕")
    print("-------- Menú ------\n")
    for cafe, precio in precios_cafe.items():
        print(f"{cafe} - ${precio}")
        print(f"📌 Ingredientes: {recetas_cafe[cafe]}\n")

    total_pedido = 0 

    while True:
        cafe_usuario = input("🛒 ¿Qué café desea ordenar?: ")
        if cafe_usuario not in precios_cafe:
            print("❌ Ese café no está en el menú. Intente de nuevo.")
            continue 

        orden_cliente = pedir_orden(cafe_usuario, recetas_cafe, materia_prima)
        
        if orden_cliente: 
            total_pedido += precios_cafe[cafe_usuario]
        
        ans = input("➕ ¿Desea ordenar otro café? (S/N): ").lower()
        if ans == 'n':
            break  

    print(f"\n💳 Total a pagar: ${total_pedido}")
    obtener_pago(total_pedido)

    cerrar = input("👨‍💼 ¿Desea apagar la máquina? (S/N): ").lower()
    if cerrar == 's':
        print("🔴 Cerrando la cafetería... ¡Hasta luego!")
        break  # Termina el programa
