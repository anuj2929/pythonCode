'''
Created on Dec 9, 2016

@author: anuj.b.rastogi
'''
import SimpleHTTPServer
import SocketServer

PORT=8010
handler=SimpleHTTPServer.SimpleHTTPRequestHandler
httpd=SocketServer.TCPServer(("",PORT),handler)
print "Server started"

httpd.serve_forever()
