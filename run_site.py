import http.server
import socketserver
import socket

PORT = 8000  # порт можна змінити

# Отримати локальний IP
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # не має значення, просто щоб визначити IP інтерфейсу
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    print(f"Сайт запущено! Відкрий у браузері: http://{local_ip}:{PORT}")
    print("Для зупинки натисни CTRL+C")
    httpd.serve_forever()

