import web
import citys
import json
urls = (
    '/hello', 'hello',
    '/provinces', 'provinces'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
class provinces:
    def GET(self):
        data = json.loads(citys.data);


if __name__ == "__main__":
    app.run()