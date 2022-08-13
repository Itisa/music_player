# -*- coding: utf-8 -*-  
import tornado.ioloop
import tornado.web
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class MainHandler(tornado.web.RequestHandler):

	def get(self):
		# print(self.request.headers)
		# print(type(self.request.headers))
		# print("##########")
		# print(self.request.headers["User-Agent"])
		# print(type(self.request.headers["User-Agent"]))

		# Mobile
		ifmobile = bool( reMobile.search(self.request.headers["User-Agent"]) )
		self.render("music_player.html", title="MMM",online=True,ifmobile=ifmobile)
	
	def post(self):

		def changetime2seconds(t):
			minute,second = t.split(":")
			return int(minute)*60 + float(second)

		data = json.loads(self.request.body)
		print(data)
		if (data["action"] == "get_lyric"):
			# songname,songformat = data["song"].split(".")
			ind = data["song"].rfind(".")
			songname = data["song"][:ind]
			songformat = data["song"][ind:]
			lyricfile = songname+".lrc"
			# print(lyricfile)
			# print("./static/lyrics/"+lyricfile)
			if (os.path.isfile("./static/lyrics/"+lyricfile) == True):
				
				with open("./static/lyrics/"+lyricfile,"r") as f:
					data = f.read()
					f.close()
				dd = re.split("\n",data)
				# lyric = []
				l = []
				r = []
				for i in dd:
					if (i == ""): continue
					ind = i.find("]")
					l.append(changetime2seconds(i[1:ind]))
					r.append(i[ind+1:])
				lyric = [l,r]
				self.write(json.dumps(lyric))
			else:
				self.write("[]")
		
		

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
	reMobile = re.compile("Mobile")
	tornado.ioloop.IOLoop.current().start()
