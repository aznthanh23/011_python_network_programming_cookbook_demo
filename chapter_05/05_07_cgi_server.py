#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 5
# This program is optimized for Python 2.7.
# It may run on any other Python version with/without modifications.

import os
import cgi
import argparse
import BaseHTTPServer
import CGIHTTPServer
import cgitb
cgitb.enable() ## eanble CGI error reporting

def web_server(port):
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler # RequestsHandler
    server_address = ("", port)
    handler.cgi_directories = ["/cgi-bin", ]
    httpd = server(server_address, handler)
    print "Starting web server with CGI supprot on port: %s ..." %port
    httpd.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CGI Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    web_server(given_args.port)

