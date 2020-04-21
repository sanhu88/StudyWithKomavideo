import feedparser
import pprint as pp

#print(feedparser.__version__)

rss_oschina = feedparser.parse('https://www.oschina.net/news/rss')
#pp.pprint(rss_oschina,depth =2)	#最大两层
rss_baidu_web = feedparser.parse('http://news.baidu.com/n?cmd=1&class=internet&tn=rss')

#pp.pprint(rss_baidu_web)
#https://www.baidu.com/search/rss.html
rss_people = feedparser.parse('http://www.people.com.cn/rss/politics.xml')

#pp.pprint(rss_people,depth =3)

#获取rss的编码方式
#print('encoding',rss_oschina.get('encoding'))
#print('encoding',rss_people.get('encoding'))
#print('rss_people encoding',rss_people['encoding'])

#新闻列表
#pp.pprint(rss_people['entries'],depth =1)
#
#
#循环获取内容
# for item in rss_people['entries']:
# 	#print(type(item['title']))
# 	#exit()
# 	print(item['title'])
# 	print('',item['link'])
# 	print('',item['published'])

titles = [item['title'] for item in rss_people['entries']]
#,item['link'] for item in rss_people['entries']
#pp.pprint(titles)
#
#字典列表
news = [{'title:':item['title'],'link':item['link']} for item in rss_people['entries']]
pp.pprint(news)