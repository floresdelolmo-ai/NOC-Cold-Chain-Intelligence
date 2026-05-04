import time
import json
import random
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# Tu llave maestra de Microsoft Fabric
CONNECTION_STR = "AQUI TU CONEXION"

# Nuestra flota inicial con sus coordenadas de salida
camiones = [
    {"camion_id": "TRK-001", "ruta": "Madrid-Paris", "lat": 40.4168, "lon": -3.7038},
    {"camion_id": "TRK-002", "ruta": "Barcelona-Lyon", "lat": 41.3851, "lon": 2.1734},
    {"camion_id": "TRK-003", "ruta": "Valencia-Berlin", "lat": 39.4699, "lon": -0.3763},
    {"camion_id": "TRK-004", "ruta": "Sevilla-Milan", "lat": 37.3891, "lon": -5.9845}
]

def generar_telemetria():
    eventos = []
    for camion in camiones:
        # Simulamos que los camiones se mueven un poco en el mapa
        camion["lat"] += random.uniform(-0.05, 0.05)
        camion["lon"] += random.uniform(-0.05, 0.05)
        
        # Simulamos la temperatura del frigorífico (Lo normal es entre 2ºC y 4ºC)
        # De vez en cuando, simulamos un fallo donde la temperatura sube a 6ºC o 7ºC (¡Alerta!)
        es_anomalia = random.random() < 0.1  # 10% de probabilidad de fallo
        temp_actual = round(random.uniform(5.5, 8.0) if es_anomalia else random.uniform(1.5, 4.5), 1)
        
        evento = {
            "timestamp": datetime.utcnow().isoformat(),
            "camion_id": camion["camion_id"],
            "ruta": camion["ruta"],
            "latitud": round(camion["lat"], 4),
            "longitud": round(camion["lon"], 4),
            "temperatura_celsius": temp_actual,
            "estado_carga": "ALERTA" if temp_actual > 4.5 else "OPTIMO"
        }
        eventos.append(evento)
    return eventos

print("🚀 Iniciando el Centro de Control Logístico...")
print("📡 Conectando a Microsoft Fabric...")

# Creamos el cliente de conexión
producer = EventHubProducerClient.from_connection_string(conn_str=CONNECTION_STR)

try:
    with producer:
        while True:
            # Generamos los datos de este segundo
            datos_nuevos = generar_telemetria()
            
            # Preparamos el paquete de datos para enviarlo
            event_data_batch = producer.create_batch()
            for dato in datos_nuevos:
                event_data_batch.add(EventData(json.dumps(dato)))
                
            # ¡Disparamos los datos hacia Fabric!
            producer.send_batch(event_data_batch)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ 4 eventos enviados. Moviendo flota...")
            
            # Pausamos 3 segundos para no saturar el sistema
            time.sleep(3)
            
except KeyboardInterrupt:
    print("\n🛑 Simulador detenido por el usuario.")
except Exception as e:
    print(f"\n❌ Error al enviar datos: {e}")