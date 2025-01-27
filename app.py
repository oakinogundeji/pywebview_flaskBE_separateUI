import webview
import threading
import os
import sys
from be.start import startUp, create_app


def start_flask(ready_event):
    try:
        # Run the startup sequence
        startUp()
        # Signal that backend initialization is ready
        ready_event.set()
        # Start Flask server
        app = create_app()
        app.run(host="localhost", port=8080)
    except Exception as e:
        print(f"Backend startup failed: {str(e)}")
        ready_event.set()
        sys.exit(1)


def main():
    # Create an event to signal when backend initialization is ready
    backend_ready = threading.Event()

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask, args=(backend_ready,))
    flask_thread.daemon = True
    flask_thread.start()

    # Wait for backend initialization to complete
    print("Waiting for backend setup to complete...")
    backend_ready.wait()
    print("Backend initialized. Starting UI...")

    # Determine the base path for the app
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS  # Path for packaged app
    else:
        base_path = os.path.dirname(
            os.path.abspath(__file__)
        )  # Path for development mode

    svelte_app_path = os.path.join(base_path, "ui", "index.html")

    # Path to the built Svelte app's index.html
    print(f"svelte_app_path: {svelte_app_path}")

    # Create a PyWebView window
    webview.create_window("Ann Haliszt", svelte_app_path, width=1400, height=850)
    webview.start()


if __name__ == "__main__":
    main()
