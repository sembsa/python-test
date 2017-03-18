import SimpleHTTPServer
import SocketServer

hostname = "localhost"
port = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", port), Handler)

print "Server starts: ", port

httpd.serve_forever()