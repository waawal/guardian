# Python Wrapper for the Guardian API

    >>> from guardian import Guardian
    >>> g = Guardian()
    >>> g('twitter')
    [{u'sectionName': u'UK news', u'webTitle': u"Royal Mail's first-class returns fail to silence critics", u'webUrl': u'http://www.theguardian.com/uk-news/2013/oct/06/royal-mail-returns-fail-to-silence-critics', u'apiUrl': u'http://content.guardianapis.com/uk-news/2013/oct/06/royal-mail-returns-fail-to-silence-critics', u'webPublicationDate': u'2013-10-05T23:05:51Z', u'id': u'uk-news/2013/oct/06/royal-mail-returns-fail-to-silence-critics', u'sectionId': u'uk-news'}, {u'sectionName': u'Football', u'webTitle': u'Why the future of English football should not be about John Beck | Daniel Taylor', u'webUrl': u'http://www.theguardian.com/football/blog/2013/oct/05/english-football-john-beck-fa-coaching', u'apiUrl': u'http://content.guardianapis.com/football/blog/2013/oct/05/english-football-john-beck-fa-coaching', u'webPublicationDate': u'2013-10-05T21:01:01Z', u'id': u'football/blog/2013/oct/05/english-football-john-beck-fa-coaching', u'sectionId': u'football'}]
    >>> g.item('football/blog/2013/oct/05/english-football-john-beck-fa-coaching')
    {u'sectionName': u'Football', u'webTitle': u'Why the future of English football should not be about John Beck | Daniel Taylor', u'webUrl': u'http://www.theguardian.com/football/blog/2013/oct/05/english-football-john-beck-fa-coaching', u'apiUrl': u'http://content.guardianapis.com/football/blog/2013/oct/05/english-football-john-beck-fa-coaching', u'webPublicationDate': u'2013-10-05T21:01:01Z', u'id': u'football/blog/2013/oct/05/english-football-john-beck-fa-coaching', u'sectionId': u'football'}