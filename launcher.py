import webview
import multiprocessing
import uvicorn
import os
import time
import sys

# Add backend to path so we can import main
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))
from main import app

def run_backend():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    # 1. Start the Python backend in a separate process
    backend_process = multiprocessing.Process(target=run_backend)
    backend_process.daemon = True
    backend_process.start()

    # Give the backend a second to start
    time.sleep(1)

    # 2. Get the path to the index.html
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_path = os.path.join(current_dir, "index.html")

    # 3. Launch the native OS window
    print(f"Launching Sentairos AI from: {frontend_path}")
    webview.create_window('Sentairos AI', f'file://{frontend_path}', width=1200, height=800, background_color='#0f172a')
    webview.start()
