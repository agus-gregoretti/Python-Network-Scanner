# 🛡️ Python-Net-Scanner

¡Buenas! Les comparto un proyecto en el que estuve trabajando, un escáner modular que no solo detecta quién está conectado a una red, sino que también identifica fabricantes y genera un reporte en PDF, ideal para presentar en una auditoría o simplemente para mantener un registro ordenado.

---

## 🛠️ ¿Cómo funciona?
El script utiliza el protocolo **ARP** para realizar un rastreo en el rango de IP indicado. Decidí estructurarlo de forma modular para tener un mejor manejo de cambios a posterior:

* **scanner.py:** El motor que realiza el envío de paquetes con `Scapy` y consulta los fabricantes (vendors) mediante API.
* **generadordereportes.py:** Se encarga de toda la lógica estética del PDF utilizando `ReportLab`.
* **main.py:** El punto de entrada que coordina la ejecución de los módulos.

## 🚀 Tecnologías y Librerías
* **Python 3.x**
* **Scapy:** Manipulación de paquetes de red.
* **Requests:** Consumo de la API de MacVendors.
* **ReportLab:** Generación de documentos PDF.

---

## 💻 Dependencias
```bash
pip install scapy requests reportlab
python Main.py
```
es necesario ejecutar el `Main.py` con privilegios de administrador (requerido para el manejo de paquetes de red)

## 💻 Ejemplo de Uso y Salida:

```text
Introduce el rango de tu red (ej. 192.168.0.1/24): 192.168.0.1/24
[!] Escaneando: 192.168.0.1/24

[+] Dispositivos encontrados:
-----------------------------------------------------------------------
IP              | MAC Address          | Vendor
-----------------------------------------------------------------------
192.168.0.1     | 02:10:18:XX:XX:XX    | N/A
192.168.0.116   | 2c:f0:5d:XX:XX:XX    | Micro-Star INTL CO., LTD.
192.168.0.21    | cc:6e:a4:XX:XX:XX    | Samsung Electronics Co.,Ltd
192.168.0.89    | 76:5d:bc:XX:XX:XX    | N/A
192.168.0.219   | cc:40:85:XX:XX:XX    | WiZ
-----------------------------------------------------------------------

[+] Proceso finalizado. Revisá tu PDF.

---
```
## 🤝 Contribuciones y Contacto
¡Gracias por leerme! Este es uno de mis primeros proyectos, así que si el programa te sirve, te resulta interesante o tenés alguna idea para mejorarlo, sentite libre de clonarlo y probarlo!

Si te gustó, dale una ⭐ al repositorio, que sin duda ayuda.

---
