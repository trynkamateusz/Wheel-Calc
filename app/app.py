import webview
from pathlib import Path

from calculator import Api

asset_path = Path(__file__).parent.parent / 'assets'

class App:
    def __init__(self):
        self.window = webview.create_window(
            'Wheel Calculator',
            str(asset_path / 'index.html'),
            min_size=(800, 600),
            js_api=Api(),
        )

    def run(self):
        webview.start()

if __name__ == "__main__":
    apk = App()
    apk.run()