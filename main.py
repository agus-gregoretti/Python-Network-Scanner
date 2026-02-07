import generadordereportes
import scanner

def main():
    target = input("Introduce el rango de tu red (ej. 192.168.0.1/24): ")
    
    # 1. Llamamos al motor
    resultados = scanner.run_scan(target)
    
    #--- Printear resultados en pantalla ---
    print("\n[+] Dispositivos encontrados:")
    print("-" * 50)
    for fila in resultados[1:]: # Usamos [1:] para saltarnos la cabecera ["IP", "MAC", "Fabricante"]
        print(f"IP: {fila[0]} | MAC: {fila[1]} | Vendor: {fila[2]}")
    print("-" * 50)
    # ----------------------------------------------
    
    # 2. Llamamos al diseñador
    generadordereportes.generate_pdf(resultados, target)
    
    print("\n[+] Proceso finalizado. Revisá tu PDF.")

if __name__ == "__main__":
    main()