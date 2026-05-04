# 🚚❄️ NOC: Cold Chain Intelligence (Real-Time IoT Streaming)

[🇪🇸 Español](#-español) | [🇬🇧 English](#-english)

---

## 🇪🇸 Español

### 📖 Resumen del Proyecto
Este proyecto demuestra una arquitectura de **Streaming de Datos en Tiempo Real** diseñada para un Centro de Operaciones de Red (NOC) logístico. Utilizando el ecosistema de **Microsoft Fabric**, el sistema ingesta telemetría IoT de una flota de camiones frigoríficos, analiza los datos al milisegundo y los visualiza en un panel táctico para prevenir roturas en la cadena de frío.

### 📊 Fuente de Datos (Simulador IoT)
A diferencia de usar un dataset estático, desarrollé un **Simulador IoT en Python** personalizado. Este script genera y empuja eventos térmicos sintéticos (ID de camión, ruta, temperatura, estado de carga) continuamente hacia un *Eventstream* en la nube, imitando el comportamiento de sensores reales en movimiento.

### 🎯 Puntos Clave
*   **Ingesta en Streaming:** Uso de *Eventhouse* y *Eventstream* en Microsoft Fabric para procesar datos sin latencia.
*   **Análisis de Series Temporales:** Consultas avanzadas utilizando **Kusto Query Language (KQL)** para calcular medias móviles y detectar picos críticos.
*   **Dashboard Táctico (NOC):** Visualización "Clean UI" con auto-refresh a 30 segundos, diseñada para la toma de decisiones instantánea.
*   **Scripting:** Generador de cargas de trabajo (Payloads) en Python utilizando las librerías `azure-messaging-eventhubs` y `datetime`.

### 💡 Retos y Soluciones Técnicas

#### 1️⃣ El espejismo del "Dato Perdido" (Consultas temporales) 🏜️
*   **Reto:** Al intentar visualizar la telemetría histórica, las gráficas KQL devolvían *0 registros* y mostraban el error `"This series no longer exists"`.
*   **Solución:** Al ser un entorno de tiempo real, las consultas KQL estaban limitadas por defecto a `where timestamp > ago(1h)`. Como el simulador de Python no estuvo corriendo de madrugada, la ventana temporal estaba vacía. Modifiqué los filtros de tiempo en KQL (`ago(2d)`) para análisis histórico y mantuve `ago(5m)` para el NOC en vivo.

#### 2️⃣ El cuello de botella de la Ingesta Directa 🚦
*   **Reto:** Enviar cada micro-variación de temperatura de forma individual amenazaba con saturar la conexión del Eventhub.
*   **Solución:** Implementé la función `EventDataBatch` en el código Python. El script acumula las lecturas de los sensores en un lote (batch) antes de despacharlas hacia Fabric, optimizando drásticamente el ancho de banda y simulando protocolos MQTT/AMQP eficientes.

#### 3️⃣ Estética Funcional vs. Sobrecarga Visual (Diseño NOC) 🎨
*   **Reto:** La interfaz por defecto de los paneles KQL en Fabric carece de las opciones de diseño profundo de Power BI, corriendo el riesgo de parecer un simple volcado de datos.
*   **Solución:** Adopté un enfoque "Clean UI" (minimalista). Eliminé fondos recargados y utilicé formato condicional estricto en las métricas clave (ej. alertas en rojo) y una paleta de alto contraste en las series temporales, centrando la atención puramente en el cambio del dato vivo.

---

## 🇬🇧 English

### 📖 Project Overview
This project showcases a **Real-Time Data Streaming** architecture designed for a logistics Network Operations Center (NOC). Built on the **Microsoft Fabric** ecosystem, the system ingests IoT telemetry from a fleet of refrigerated trucks, analyzes the data with millisecond latency, and visualizes it on a tactical dashboard to prevent cold chain failures.

### 📊 Data Source (Custom IoT Simulator)
Instead of relying on a static dataset, I engineered a custom **Python IoT Simulator**. This script generates and pushes synthetic thermal events (Truck ID, route, temperature, cargo status) continuously into a cloud *Eventstream*, mimicking the behavior of real-world mobile sensors.

### 🎯 Key Features
*   **Streaming Ingestion:** Leveraged *Eventhouse* and *Eventstream* in Microsoft Fabric for zero-latency data processing.
*   **Time Series Analysis:** Advanced querying using **Kusto Query Language (KQL)** to calculate moving averages and detect critical temperature spikes.
*   **Tactical NOC Dashboard:** "Clean UI" visualization with a 30-second auto-refresh, designed for split-second decision-making.
*   **Scripting:** Payload generation in Python utilizing `azure-messaging-eventhubs` and `datetime` libraries.

### 💡 Challenges & Technical Solutions

#### 1️⃣ The "Lost Data" Mirage (Temporal Queries) 🏜️
*   **Challenge:** When attempting to visualize historical telemetry, KQL charts returned *0 records* and displayed a `"This series no longer exists"` error.
*   **Solution:** Being a real-time environment, default KQL queries were strictly bounded to `where timestamp > ago(1h)`. Since the Python simulator was paused overnight, the temporal window was completely empty. I adjusted the KQL time filters (`ago(2d)`) for historical analysis while keeping `ago(5m)` strictly for the live NOC.

#### 2️⃣ Direct Ingestion Bottleneck 🚦
*   **Challenge:** Sending every micro-variation in temperature individually threatened to throttle the Eventhub connection.
*   **Solution:** I implemented the `EventDataBatch` function within the Python code. The script now accumulates sensor readings into a batch before dispatching them to Fabric, drastically optimizing bandwidth and simulating efficient MQTT/AMQP protocols.

#### 3️⃣ Functional Aesthetics vs. Visual Clutter (NOC Design) 🎨
*   **Challenge:** The default KQL dashboard interface in Fabric lacks the deep design capabilities of Power BI, risking a layout that looks like a raw data dump.
*   **Solution:** I adopted a strict "Clean UI" (minimalist) approach. I stripped away heavy backgrounds, applied strict conditional formatting to key metrics (e.g., alerts in red), and used a high-contrast palette for time-series lines, focusing the user's attention purely on the live data mutations.

---

### 🔗 Conectemos / Connect
*   🌐 **Portfolio:** [yatawek.vercel.app](https://yatawek.vercel.app)
*   💼 **LinkedIn:** [floresdelolmo](https://www.linkedin.com/in/floresdelolmo/)
*   📧 **Email:** jfloresdelolmo@gmail.com
