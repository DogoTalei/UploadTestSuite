import requests
from colorama import Fore, Style, init
import os

# Inicializar colorama
init()

# URL del endpoint de carga de archivos
upload_url = 'http://192.168.1.104/my_weblog/content/public/upload/'  # URL corregida

# Lista de tipos de archivos para probar
file_types = [
    # Archivos de texto
    ('text/plain', 'test.txt'),
    ('text/html', 'test.html'),
    ('text/css', 'test.css'),
    ('text/csv', 'test.csv'),
    ('text/xml', 'test.xml'),

    # Imágenes
    ('image/jpeg', 'test.jpg'),
    ('image/png', 'test.png'),
    ('image/gif', 'test.gif'),
    ('image/bmp', 'test.bmp'),
    ('image/tiff', 'test.tiff'),
    ('image/webp', 'test.webp'),

    # Documentos
    ('application/pdf', 'test.pdf'),
    ('application/msword', 'test.doc'),
    ('application/vnd.ms-excel', 'test.xls'),
    ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'test.docx'),
    ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'test.xlsx'),
    ('application/epub+zip', 'test.epub'),

    # Archivos comprimidos
    ('application/zip', 'test.zip'),
    ('application/x-rar-compressed', 'test.rar'),
    ('application/x-7z-compressed', 'test.7z'),
    ('application/x-tar', 'test.tar'),
    ('application/x-bzip', 'test.bz'),
    ('application/x-bzip2', 'test.bz2'),

    # Archivos ejecutables
    ('application/x-msdownload', 'test.exe'),
    ('application/x-shockwave-flash', 'test.swf'),
    ('application/x-java-archive', 'test.jar'),
    ('application/x-ms-dos-executable', 'test.com'),

    # Audio y video
    ('audio/mpeg', 'test.mp3'),
    ('audio/wav', 'test.wav'),
    ('audio/ogg', 'test.ogg'),
    ('video/mp4', 'test.mp4'),
    ('video/x-msvideo', 'test.avi'),
    ('video/x-flv', 'test.flv'),
    ('video/quicktime', 'test.mov'),

    # Otros formatos
    ('application/x-httpd-php', 'test.php'),  # Archivo PHP para prueba de ejecución de código
    ('application/javascript', 'test.js'),
    ('application/x-font-ttf', 'test.ttf'),
    ('application/x-font-woff', 'test.woff'),
    ('application/x-font-woff2', 'test.woff2'),
    ('application/json', 'test.json'),
    ('application/x-sqlite3', 'test.sqlite'),
    ('application/x-phar', 'test.phar')  # Archivo PHAR añadido
]

# Contenido del archivo de prueba (para archivos binarios, el contenido puede no ser relevante)
file_content = b'This is a test file.'

# Función principal
for file_type, file_name in file_types:
    # Crear un archivo de prueba
    with open(file_name, 'wb') as f:
        f.write(file_content)

    # Preparar el archivo para la carga
    with open(file_name, 'rb') as f:
        files = {
            'archivoSubido': (file_name, f, file_type)  # Usa el nombre correcto del campo
        }
        
        # Enviar solicitud de carga
        try:
            response = requests.post(upload_url, files=files)
            response.raise_for_status()  # Levanta una excepción para códigos de estado HTTP 4xx/5xx
            print(f'{Fore.CYAN}Trying file: {file_name} with type: {file_type}{Style.RESET_ALL}')
            print(f'{Fore.GREEN}Status Code: {response.status_code}{Style.RESET_ALL}')
            print(f'{Fore.YELLOW}Response: {response.text}{Style.RESET_ALL}\n')
        except requests.exceptions.RequestException as e:
            print(f'{Fore.RED}Error occurred with file {file_name} and type {file_type}: {e}{Style.RESET_ALL}')
        finally:
            # Elimina el archivo después de la prueba
            if os.path.exists(file_name):
                os.remove(file_name)

# Firma personalizada
print(f'\n{Fore.MAGENTA}--- Firma ---{Style.RESET_ALL}')
print(f'{Fore.MAGENTA}Script creado por Dogo Talei{Style.RESET_ALL}')
print(f'{Fore.MAGENTA}¡Gracias por usar este script de prueba!{Style.RESET_ALL}')
