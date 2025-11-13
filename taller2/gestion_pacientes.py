# pacientes = []

# # Paciente de prueba
# datos_paciente = {
#     "ID": 23,
#     "nombre": "josejulio",
#     "apellido": "Lopez",
#     "edad": 45,
#     "genero": "M",
#     "diagnostico": "cancer",
#     "historial": ["diabetes"]
# }


# ===== FUNCIÓN DE BÚSQUEDA =====
def buscar_paciente(criterio, valor):
    """Busca pacientes según criterio"""
    return [p for p in pacientes if valor.lower() in str(p.get(criterio, "")).lower()]


def buscar_pacientes():
    
    if not pacientes:
        print("\n no hay pacientes registrados\n")
        return
    
    print("\n===== BUSCAR PACIENTES =====")
    print("1) Buscar por ID")
    print("2) Buscar por Nombre") 
    print("3) Buscar por Diagnóstico")
    
    opcion = input("\nseleccione: ").strip()
    
    if opcion not in ["1", "2", "3"]:
        print("opcion invalida.")
        return
    
    valor = input("ingrese valor a buscar: ").strip()
    
    criterios = {"1": "ID", "2": "nombre", "3": "diagnostico"}
    resultados = buscar_paciente(criterios[opcion], valor)
    
    if resultados:
        print(f"\n✓ encontrados {len(resultados)} paciente(s):\n")
        for p in resultados:
            print(f"  ID: {p.get('ID')}")
            print(f"  Nombre: {p.get('nombre')} {p.get('apellido')}")
            print(f"  Edad: {p.get('edad')}")
            print(f"  Género: {p.get('genero')}")
            print(f"  Diagnóstico: {p.get('diagnostico')}")
            print(f"  Historial: {p.get('historial')}")
            print("-" * 40)
    else:
        print("\n✗ No se encontró ningún paciente.\n")