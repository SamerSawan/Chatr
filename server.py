import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),  # Serve static files
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())