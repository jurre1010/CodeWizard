import web

urls = (
    '/', 'Home'
)

render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/Routes

class Home:
    def GET(self):
        return render.Home()
    
if __name__ == "__main__":
    app.run()