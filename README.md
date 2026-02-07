# 🛡️ Python Network Scanner
**Herramienta de reconocimiento de red local con auditoría de fabricantes y reportes PDF.**

Este proyecto es un escáner de red profesional desarrollado en Python. Utiliza el protocolo **ARP** para identificar dispositivos activos en una red local, consulta una base de datos de fabricantes mediante API y genera un reporte formal en formato PDF.

---

## ✨ Características Principales
* **Escaneo Modular:** Estructura organizada en tres módulos (Main, Scanner y Generador de Reportes).
* **Protocolo ARP:** Implementación mediante la librería `Scapy` para enviar paquetes de broadcast.
* **Identificación de Vendors:** Integración con API externa para reconocer marcas (ej. Samsung, WiZ, MSI).
* **Reporte Profesional:** Generación de archivos PDF con tablas estilizadas, alternancia de colores y diseño corporativo.

## 🛠️ Tecnologías y Librerías
* **Python 3.x**
* **Scapy:** Para la manipulación y envío de paquetes de red.
* **Requests:** Para el consumo de la API de MacVendors.
* **ReportLab:** Para la creación y diseño del documento PDF.

---

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/agus-gregoretti/Python-Network-Scanner.git](https://github.com/agus-gregoretti/Python-Network-Scanner.git)
