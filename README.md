# Automatización de Web Scraping con Autenticación de Sesión

## 📝 Descripción
Este proyecto proporciona una guía práctica y modular para extraer información de plataformas web protegidas detrás de un muro de autenticación. El script (`login.py`) automatiza el flujo completo de inicio de sesión, permitiendo acceder a áreas privadas de un sitio web de manera programática para realizar tareas de recolección de datos.

## 🎯 Objetivo
El objetivo principal es simular el comportamiento humano dentro de un navegador para superar formularios de acceso. El script ejecuta de forma secuencial los siguientes pasos técnicos:
* **Inyección de credenciales:** Escanea el código HTML del sitio web objetivo para localizar dinámicamente los campos de texto correspondientes al usuario (`Login`) y a la contraseña (`Password`).
* **Simulación de eventos:** Rellena los campos con las credenciales correspondientes y dispara de forma automatizada el evento de clic sobre el botón de envío (`submit`).
* **Gestión de variables de entorno:** Protege la información sensible centralizando la configuración en un archivo `.env` externo con las siguientes variables obligatorias:
  ```env
  URL="<url-del-sitio-web>"
  APP_USERNAME="<nombre-de-usuario>"
  APP_PASSWORD="<clave-o-contraseña>"
  ```

## 🚀 Aplicación y Casos de Uso
Esta arquitectura es indispensable para proyectos de integración y extracción de datos en plataformas que no ofrecen una API oficial, permitiendo auditar o unificar información de sistemas cerrados.

**Casos de uso principales:**
* **Monitoreo de portales privados:** Extracción automatizada de reportes financieros, facturas o estados de cuenta desde intranets corporativas.
* **Migración de datos:** Recuperación masiva de información desde sistemas antiguos (legados) hacia nuevas bases de datos.
* **Auditoría de plataformas:** Verificación automática de la disponibilidad y correcto funcionamiento de formularios de acceso de clientes.

**Impacto:** Elimina por completo las tareas repetitivas de ingreso manual a portales web para la descarga de archivos. Además, al implementar el uso de un archivo `.env`, garantiza la seguridad del desarrollo al evitar que las contraseñas queden expuestas directamente en el código fuente (Hardcoding).