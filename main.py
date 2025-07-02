import webview


class Client:
    def __init__(self, version="a"):
        self.version = version
        self.window = webview.create_window("Telegram", f"https://web.telegram.org/{version}")
        webview.start()
    def title(self, new=f"Telegram"):
        self.window.title = new
    def set_version(self, version="a"):
        self.version = version
    def save(self):
        print(self.window.get_cookies())



if __name__ == "__main__":
    telegram = Client()
