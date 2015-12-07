import tornado.torndb as torndb
import tornado.web
import tornado.ioloop
from tornado.options import define,options,parse_command_line

define('port',default=8888,help='run on the port',type=int)
database=torndb.Connection('localhost','learn',user='root',password='123456')
l=[]
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('a.html',title='haha',items=l)
	def post(self):
		count=1
		print self.request.remote_ip
		talk=self.get_argument('talk')
		talk=str(talk)
		database.execute('insert into chatting(id,content) values(%d,"%s")'%(count,talk))
		l.append(talk)
		self.render('a.html',title='haha',items=l)
def main():
	parse_command_line()
	app=tornado.web.Application(
			[
				(r'/',MainHandler),
				],
			)

	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
	
if __name__=='__main__':
	main()