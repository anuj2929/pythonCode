'''
<<<<<<< Updated upstream
Created on Dec 9, 2016

@author: anuj.b.rastogi
=======
Created on 09-Dec-2016

@author: Anuj
>>>>>>> Stashed changes
'''
import SimpleHTTPServer
import SocketServer

<<<<<<< Updated upstream
PORT=8010
handler=SimpleHTTPServer.SimpleHTTPRequestHandler
httpd=SocketServer.TCPServer(("",PORT),handler)
print "Server started"

httpd.serve_forever()
=======
PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
>>>>>>> Stashed changes
