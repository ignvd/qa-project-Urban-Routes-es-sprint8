# Proyecto QA: Urban Routes

## Descripción
Este proyecto automatiza las pruebas de la interfaz de usuario (IU) para el sistema Urban Routes, cubriendo el flujo completo desde pedir un taxi hasta obtener la información del conductor.

## Instalación
1. Clona este repositorio:
   git clone git@github.com:username/qa-project-Urban-Routes-es.git

## directorio del proyecto
cd qa-project-Urban-Routes-es

## Instala las dependencias
pip install -r requirements.txt

## Para ejecutar las pruebas
pytest tests/test_urban_routes.py

## Tecnologías utilizadas
Python 3.8+
Selenium WebDriver: Para automatizar la interacción con la interfaz de usuario.
Pytest: Para organizar y ejecutar las pruebas.
Page Object Model (POM): Para estructurar los selectores y métodos relacionados con la IU.

## Flujo de pruebas automatizadas
Las pruebas incluyen:

1.Configurar una dirección.
2.Seleccionar una tarifa Comfort.
3.Ingresar un número de teléfono.
4.Agregar una tarjeta de crédito (simulando eventos de enfoque).
5.Escribir un mensaje para el conductor.
6.Pedir una manta, pañuelos y 2 helados.
7.Validar que el modal de búsqueda de conductor aparezca.
8.Validar la información del conductor (opcional).

