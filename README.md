# 🛡️ PyNet-Scanner: Auditoría de Red con Python

¡Buenas! Les comparto un proyecto en el que estuve trabajando. La idea nació de la necesidad de tener una herramienta propia, rápida y ligera para mapear dispositivos en una red local sin depender de software de terceros más pesado.

Es un escáner modular que no solo detecta quién está conectado, sino que también identifica fabricantes y genera un reporte profesional en PDF, ideal para presentar en una auditoría o simplemente para mantener un registro ordenado de la infraestructura.

---

## 🛠️ ¿Cómo funciona?
El script utiliza el protocolo **ARP** para realizar un barrido en el rango de IP indicado. Decidí estructurarlo de forma modular para que sea escalable y fácil de mantener:

* **Scanner.py:** El motor que realiza el envío de paquetes con `Scapy` y consulta los fabricantes (vendors) mediante API.
* **GeneradorDeReportes.py:** Se encarga de toda la lógica estética del PDF utilizando `ReportLab`.
* **Main.py:** El punto de entrada que coordina la ejecución de los módulos.

## 🚀 Tecnologías y Librerías
* **Python 3.x**
* **Scapy:** Manipulación y forja de paquetes de red.
* **Requests:** Consumo de la API de MacVendors.
* **ReportLab:** Generación de documentos PDF con diseño corporativo.

---

## 💻 Ejemplo de Uso y Salida
Para correrlo, es necesario instalar las dependencias y ejecutar el `Main.py` con privilegios de administrador (requerido para el manejo de paquetes de red):


```bash
pip install scapy requests reportlab
python Main.py
```

Introduce el rango de tu red (ej. 192.168.0.1/24): 192.168.0.1/24
[!] Escaneando: 192.168.0.1/24

[+] Dispositivos encontrados:
--------------------------------------------------
IP: 192.168.0.1   | MAC: 02:10:18:XX:XX:XX | Vendor: N/A
IP: 192.168.0.116 | MAC: 2c:f0:5d:XX:XX:XX | Vendor: Micro-Star INTL CO., LTD.
IP: 192.168.0.21  | MAC: cc:6e:a4:XX:XX:XX | Vendor: Samsung Electronics Co.,Ltd
IP: 192.168.0.89  | MAC: 76:5d:bc:XX:XX:XX | Vendor: N/A
IP: 192.168.0.219 | MAC: cc:40:85:XX:XX:XX | Vendor: WiZ
--------------------------------------------------

[+] Proceso finalizado. Revisá tu PDF.
