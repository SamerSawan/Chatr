import asyncio
import tornado
import tornado.websocket


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", EchoWebSocket),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),  # Serve static files
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())