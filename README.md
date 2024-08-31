# UploadTestSuite
 es una herramienta para pruebas de penetración que automatiza la carga de una amplia variedad de archivos a un servidor. Permite verificar la seguridad del manejo de archivos en diferentes formatos, incluidos tipos especiales como PHAR, detectando vulnerabilidades en el procesamiento de cargas.

# Requisitos de Librerías de Python

pip install requests

pip install colorama

1. Python: El script está escrito en Python, por lo que necesitarás tener Python instalado en tu sistema. Recomiendo Python 3.6 o superior.

2. PHP CLI: Para crear archivos PHAR, tu entorno debe tener el comando php disponible, ya que el script usa PHP CLI para generar archivos PHAR. Asegúrate de tener PHP instalado y accesible desde la línea de comandos.

3. ervidor de Pruebas: Un servidor con el endpoint http://192.168.56.102/backup/upload.php debe estar en funcionamiento para recibir las cargas de archivos. Asegúrate de que la URL esté accesible y correcta. 

