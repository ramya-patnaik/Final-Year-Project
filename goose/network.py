# -*- coding: utf-8 -*-

import urllib2
import cookielib

class HtmlFetcher(object):

    def __init__(self):
        pass

    def get_http_client(self):
        pass

    def get_html(self, config, url):
        """\

        """
        if isinstance(url, unicode):
            url = url.encode('utf-8')
        
        cookiejar = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
        urllib2.install_opener(opener)

        headers = {'User-agent': config.browser_user_agent}
        request = urllib2.Request(url, headers=headers)

        try:
            result = urllib2.urlopen(request).read()
        except:
            return None

        return result
