import requests
from colorama import Fore, Style, init
import os

# Inicializar colorama
init()

# URL del endpoint de carga de archivos
upload_url = 'http://192.168.56.102/backup/upload.php'  # URL corregida

# Lista de tipos de archivos para probar
file_types = [
    # Archivos de texto
    ('text/plain', 'DogoTalei.txt'),
    ('text/html', 'DogoTalei.html'),
    ('text/css', 'DogoTalei.css'),
    ('text/csv', 'DogoTalei.csv'),
    ('text/xml', 'DogoTalei.xml'),

    # Imágenes
    ('image/jpeg', 'DogoTalei.jpg'),
    ('image/png', 'DogoTalei.png'),
    ('image/gif', 'DogoTalei.gif'),
    ('image/bmp', 'DogoTalei.bmp'),
    ('image/tiff', 'DogoTalei.tiff'),
    ('image/webp', 'DogoTalei.webp'),

    # Documentos
    ('application/pdf', 'DogoTalei.pdf'),
    ('application/msword', 'DogoTalei.doc'),
    ('application/vnd.ms-excel', 'DogoTalei.xls'),
    ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'DogoTalei.docx'),
    ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'DogoTalei.xlsx'),
    ('application/epub+zip', 'DogoTalei.epub'),

    # Archivos comprimidos
    ('application/zip', 'DogoTalei.zip'),
    ('application/x-rar-compressed', 'DogoTalei.rar'),
    ('application/x-7z-compressed', 'DogoTalei.7z'),
    ('application/x-tar', 'DogoTalei.tar'),
    ('application/x-bzip', 'DogoTalei.bz'),
    ('application/x-bzip2', 'DogoTalei.bz2'),

    # Archivos ejecutables
    ('application/x-msdownload', 'DogoTalei.exe'),
    ('application/x-shockwave-flash', 'DogoTalei.swf'),
    ('application/x-java-archive', 'DogoTalei.jar'),
    ('application/x-ms-dos-executable', 'DogoTalei.com'),

    # Audio y video
    ('audio/mpeg', 'DogoTalei.mp3'),
    ('audio/wav', 'DogoTalei.wav'),
    ('audio/ogg', 'DogoTalei.ogg'),
    ('video/mp4', 'DogoTalei.mp4'),
    ('video/x-msvideo', 'DogoTalei.avi'),
    ('video/x-flv', 'DogoTalei.flv'),
    ('video/quicktime', 'DogoTalei.mov'),

    # Otros formatos
    ('application/x-httpd-php', 'DogoTalei.php'),  # Archivo PHP para prueba de ejecución de código
    ('application/javascript', 'DogoTalei.js'),
    ('application/x-font-ttf', 'DogoTalei.ttf'),
    ('application/x-font-woff', 'DogoTalei.woff'),
    ('application/x-font-woff2', 'DogoTalei.woff2'),
    ('application/json', 'DogoTalei.json'),
    ('application/x-sqlite3', 'DogoTalei.sqlite'),
]

# Contenido del archivo de prueba (para archivos binarios, el contenido puede no ser relevante)
file_content = b'This is a test file.'

# Función principal
for file_type, file_name in file_types:
    # Crear un archivo de prueba
    with open(file_name, 'wb') as f:
        f.write(file_content)

    # Preparar el archivo para la carga
    files = {
        'archivoSubido': (file_name, open(file_name, 'rb'), file_type)  # Usa el nombre correcto del campo
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
