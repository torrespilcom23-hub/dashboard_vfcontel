import os
import sys
import socket
import threading
import webbrowser
import time
from flask import Flask, render_template, redirect

def resource_path(relative_path: str) -> str:
    """Devuelve ruta absoluta, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS  # type: ignore[attr-defined]
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

template_dir = resource_path("templates")
static_dir = resource_path("static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

def obtener_puerto_libre(host: str = "127.0.0.1") -> int:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, 0))  # 0 = el SO asigna un puerto libre
    puerto = s.getsockname()[1]
    s.close()
    return puerto


def abrir_navegador(url: str):
    time.sleep(1)  # espera a que Flask levante
    webbrowser.open(url)


# ✅ Genera 1..45 con un enlace por defecto (cámbialo a tu dominio/IP real)
BOCINAS = {i: f"https://example.com/bocina{i}" for i in range(1, 46)}

# ✅ Si algunas bocinas tienen enlaces distintos, aquí las sobreescribes:
BOCINAS.update({
    1: "https://192.168.0.201/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    2: "https://192.168.0.202/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    3: "https://192.168.0.203/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    4: "https://192.168.0.204/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    5: "https://192.168.0.205/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    6: "https://192.168.0.206/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    7: "https://192.168.0.207/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    8: "https://192.168.0.208/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    9: "https://192.168.0.209/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    10: "https://192.168.0.210/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    11: "https://192.168.0.211/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    12: "https://192.168.0.212/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    13: "https://192.168.0.213/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    14: "https://192.168.0.214/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    15: "https://192.168.0.215/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    16: "https://192.168.0.216/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    17: "https://192.168.0.217/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    18: "https://192.168.0.218/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    19: "https://192.168.0.219/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    20: "https://192.168.0.220/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    21: "https://192.168.0.221/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    22: "https://192.168.0.222/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    23: "https://192.168.0.223/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    24: "https://192.168.0.224/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    25: "https://192.168.0.225/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    26: "https://192.168.0.226/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    27: "https://192.168.0.227/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    28: "https://192.168.0.228/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    29: "https://192.168.0.229/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    30: "https://192.168.0.230/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    31: "https://192.168.0.231/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    32: "https://192.168.0.232/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    33: "https://192.168.0.233/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    34: "https://192.168.0.234/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    35: "https://192.168.0.235/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    36: "https://192.168.0.236/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    37: "https://192.168.0.237/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    38: "https://192.168.0.238/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    39: "https://192.168.0.239/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    40: "https://192.168.0.240/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    41: "https://192.168.0.241/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    42: "https://192.168.0.242/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    43: "https://192.168.0.243/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    44: "https://192.168.0.244/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",
    45: "https://192.168.0.245/doc/index.html#/config/broadcast/realTimeBroadcast?t=1768324316371",

})

# --- Validación rápida (opcional pero recomendado) ---
esperadas = set(range(1, 46))
actuales = set(BOCINAS.keys())

faltan = sorted(esperadas - actuales)
sobran = sorted(actuales - esperadas)

print("TOTAL BOCINAS:", len(actuales))
if faltan:
    print("FALTAN:", faltan)
if sobran:
    print("SOBRAN:", sobran)


@app.get("/")
def dashboard():
    bocinas_ordenadas = dict(sorted(BOCINAS.items()))

    bloques = [
        {"titulo": "BOCINAS 1 - 10",  "bocinas": [(i, bocinas_ordenadas[i]) for i in range(1, 11)]},
        {"titulo": "BOCINAS 11 - 20", "bocinas": [(i, bocinas_ordenadas[i]) for i in range(11, 21)]},
        {"titulo": "BOCINAS 21 - 30", "bocinas": [(i, bocinas_ordenadas[i]) for i in range(21, 31)]},
        {"titulo": "BOCINAS 31 - 40", "bocinas": [(i, bocinas_ordenadas[i]) for i in range(31, 41)]},
        {"titulo": "BOCINAS 41 - 45", "bocinas": [(i, bocinas_ordenadas[i]) for i in range(41, 46)]},
    ]

    return render_template("dashboard.html", bloques=bloques)

@app.get("/bocina/<int:bocina_id>")
def ir_bocina(bocina_id: int):
    url = BOCINAS.get(bocina_id)
    if not url:
        return "Bocina no encontrada", 404
    return redirect(url)


@app.get("/salir")
def salir():
    return "<h2>Sesión finalizada</h2><p>Puedes cerrar esta pestaña.</p>"


if __name__ == "__main__":
    host = "127.0.0.1"
    port = obtener_puerto_libre(host)
    url = f"http://{host}:{port}"

    threading.Thread(target=abrir_navegador, args=(url,), daemon=True).start()
    app.run(host=host, port=port, debug=False, use_reloader=False)


@app.get("/salir")
def salir():
    return "<h2>Sesión finalizada</h2><p>Puedes cerrar esta pestaña.</p>"


