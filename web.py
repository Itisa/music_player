# -*- coding: utf-8 -*-  
import tornado.ioloop
import tornado.web
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MainHandler(tornado.web.RequestHandler):

	def get(self):
		self.render("music_player.html", title="MMM")
	
	def OPTIONS(self):
		pass

def make_app():
	return tornado.web.Application(
		[
			(r"/", MainHandler),
			(r"", MainHandler),
		],
		template_path=os.path.join(BASE_DIR, "templates"),
		static_path=os.path.join(BASE_DIR, "static")
	)
if __name__ == "__main__":
	app = make_app()
	app.listen(8080)
	tornado.ioloop.IOLoop.current().start()
