#coding:utf8
import urllib2
from sgmllib import SGMLParser

class SingerInfoParser(SGMLParser):
    ''' 抓取歌手索引页面（http://music.baidu.com/artist），解析出歌手名称和歌手详情页相对链接地址。
    歌手索引页面的HTML格式如下：
    <h3>
        <a name="B"></a>
    </h3>
    <ul class="clearfix">                                                                            
        <li>
            <a title="班得瑞" href="/artist/88044320">班得瑞</a>
        </li>                                                           
        <li>
            <a title="白雪" href="/artist/1446">白雪</a>
        </li>
        <li class="last">
            <a title="贝多芬" href="/artist/4017">贝多芬</a>
        </li>
    </ul>
    标签<h3>是歌手拼音首字母的索引区域，后面紧跟进一个<ul>标签，其class为clearfix，里面每个<li>标签嵌一个<a>标签，<a>标签的title属性为歌手的名字，href属性是歌手详情页的相对链接地址。
    '''
    def reset(self):
        SGMLParser.reset(self)
        self.tagH3Ready = False   # 是否找到<h3>标签
        self.tagUlReady = False   # 是否找到紧跟在<h3>标签后的<ul>标签，且<ul>标签的class属性为clearfix
        self.tagLiReady = False   # 上面找到符合上述条件的<ul>标签中的<li>标签
        self.singerLink = {}   # 存储所有的歌手名字及歌手详情页相对链接地址

    def start_h3(self, attrs):
        pass

    def end_h3(self):
        self.tagH3Ready = True

    def start_ul(self, attrs):
        if not self.tagH3Ready:   # <ul>必须紧跟在<h3>标签后才行
            return
        
        for k,v in attrs:
            if "class" == k.strip() and "clearfix" == v.strip():   # <ul>标签的class属性值为clearfix
                self.tagUlReady = True
        
    def end_ul(self):   # 解析<ul>标签结束，重新找<h3>标签和<ul>标签
        self.tagH3Ready = False
        self.tagUlReady = False
        
    def start_li(self, attrs):
        if self.tagUlReady:
            self.tagLiReady = True
        
    def end_li(self):
        self.tagLiReady = False
    
    def start_a(self, attrs):
        if self.tagLiReady:
            title = ""
            href = ""
            for attrKey, attrVal in attrs:
                if "title" == attrKey:
                    title = attrVal
                if "href" == attrKey:
                    href = attrVal
            self.singerLink[""+title] = ""+href
        
    def end_a(self):
        self.tagAReady = False

    def unknown_starttag(self, tag, attrs):
        self.tagH3Ready = False

class SingerInfoCollector(object):
    ''' 百度音乐歌手信息收集器，调用类SingerInfoParser完成页面HTML的解析，获得歌手名称和歌手详情页相对链接地址 '''
    
    def analyze(self, url):
        ''' url为百度的歌手索引页面，如：http://music.baidu.com/artist。
        返回的数据为Dictionary类型，Key为歌手的名称，Value为歌手详情页相对链接地址。
        '''
#         httpHandler = urllib2.HTTPHandler(debuglevel=1)
#         httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#         opener = urllib2.build_opener(httpHandler, httpsHandler)
#         urllib2.install_opener(opener)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        parser = SingerInfoParser()
        parser.feed(response.read())
        response.close()
        return parser.singerLink
        
if __name__ == "__main__":
    singerPageUrl = "http://music.baidu.com/artist"
    collector = SingerInfoCollector()
    data = collector.analyze(singerPageUrl)
    for name, link in data:
            print name, link
