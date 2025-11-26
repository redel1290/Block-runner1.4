import subprocess
import time
import psutil
import threading
import sys

SCRIPT = "run_site.py"
process = None  # для збереження процесу main.py

def is_running(script_name):
    """Перевіряє, чи є процес з заданим скриптом"""
    for proc in psutil.process_iter(['pid', 'cmdline']):
        try:
            if proc.info['cmdline'] and script_name in proc.info['cmdline']:
                return proc  # повертаємо об’єкт процесу
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def listen_quit():
    """Слухає введення користувача"""
    global process
    while True:
        user_input = input()
        if user_input.strip().lower() == 'q':
            if process:
                print("Закриваємо main.py...")
                process.terminate()
                process = None

# Запускаємо окремий потік для прослуховування клавіатури
threading.Thread(target=listen_quit, daemon=True).start()

while True:
    if not is_running(SCRIPT):
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {SCRIPT} не запущений, запускаємо...")
        process = subprocess.Popen(['python', SCRIPT])
        print(f"Запущено {SCRIPT} з PID: {process.pid}")
    time.sleep(0.5)

