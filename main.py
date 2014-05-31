import web, random


render = web.template.render('templates/')

        
urls = (
    '/word', 'word',
    '/upload', 'upload',
    '/finalize', 'finalize',
    '/(.*)', 'index'
)
app = web.application(urls, globals())

def createWord():
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    a = random.sample(consonants,2)
    a.insert(1,random.choice(vowels))
    a.append(random.choice(vowels))
    
    return "".join(a)

class upload:
    def GET(self):
        return render.index("upload", render.uploadForm())

    def POST(self):
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) # This is the filename
        web.debug(x['myfile'].value) # This is the file contents
        web.debug(x['myfile'].file.read()) # Or use a file(-like) object
        raise web.seeother('/upload')

class finalize:
    def POST(self):
        return "This will convert the uploaded files to an application..."

class word:
    def GET(self):
        return createWord()

class index:
    def GET(self, args):
        title = "HELLO!"
        body = "PyRocket will be re-written in this soon!<br><br><a href='/upload'>Upload Python</a>"
        
        body += "<br><br>awesome words: "
        word = createWord()
        body += "<a href='"+word+"'>" + word + "</a>"
        return render.index(title, body)

if __name__ == "__main__":
    app.run()
