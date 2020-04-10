#!/usr/bin/env python3
import time
from http.server import HTTPServer
from server import HTTPServer_handler
import constants

if __name__ == '__main__':
	print('starting server...')
	httpd = HTTPServer((constants.HOST_NAME, constants.PORT_NUMBER), HTTPServer_handler)
	print('running server...')
	print(time.asctime(), 'Server UP - %s:%s' % (constants.HOST_NAME, constants.PORT_NUMBER))
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), 'Server DOWN - %s:%s' % (constants.HOST_NAME, constants.PORT_NUMBER))
