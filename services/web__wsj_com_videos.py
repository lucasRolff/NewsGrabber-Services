refresh = 7200
version = 20161106.01

urls = ['http://www.wsj.com/video/',
	'http://feeds.wsjonline.com/wsj/video/most-popular/feed',
	'http://feeds.wsjonline.com/wsj/video/most-popular-this-week/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-section&query=The News Hub&count=30',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=AM Report %26 PM Report&count=30',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Hot Stocks&count=30',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=News Hub Extra&count=30',
	'http://feeds.wsjonline.com/wsj/video/news/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Page+One&fields=all&count=30',
	'http://feeds.wsjonline.com/wsj/video/politics/feed',
	'http://feeds.wsjonline.com/wsj/video/world/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-package&query=The Middle East',
	'http://feeds.wsjonline.com/wsj/video/business/feed',
	'http://feeds.wsjonline.com/wsj/video/economy/feed',
	'http://feeds.wsjonline.com/wsj/video/health/feed',
	'http://feeds.wsjonline.com/wsj/video/law/feed',
	'http://feeds.wsjonline.com/wsj/video/media-and-marketing/feed',
	'http://feeds.wsjonline.com/wsj/video/environmental-capital/feed/',
	'http://feeds.wsjonline.com/wsj/video/management/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Viewpoints',
	'http://feeds.wsjonline.com/wsj/video/business-insight/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-section&query=Leadership',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-section&query=The+Big+Interview',
	'http://feeds.wsjonline.com/wsj/video/markets/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Markets+Hub&fields=all&count=30',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Heard on the Street',
	'http://feeds.wsjonline.com/wsj/video/tech/feed',
	'http://feeds.wsjonline.com/wsj/video/andy-jordan/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-package&query=Science',
	'http://www.marketwatch.com/rss/video/wsj.asp?value=wsj-subsection&query=Worth+It',
	'http://www.marketwatch.com/rss/video/wsj.asp?value=wsj-subsection&query=Digits',
	'http://feeds.wsjonline.com/wsj/video/personal-finance/feed',
	'http://feeds.wsjonline.com/wsj/video/funds/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Taxes',
	'http://feeds.wsjonline.com/wsj/video/life-and-style/feed',
	'http://feeds.wsjonline.com/wsj/video/autos/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-package&query=A-Heds&count=30',
	'http://feeds.wsjonline.com/wsj/video/books/feed',
	'http://feeds.wsjonline.com/wsj/video/arts-and-entertainment/feed',
	'http://feeds.wsjonline.com/wsj/video/fashion/feed',
	'http://feeds.wsjonline.com/wsj/video/food-and-drink/feed',
	'http://feeds.wsjonline.com/wsj/video/sports/feed',
	'http://feeds.wsjonline.com/wsj/video/travel/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-playlist&query=WSJ Cafe',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=WSJ Magazine',
	'http://feeds.wsjonline.com/wsj/video/opinion/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-subsection&query=Opinion+Journal&fields=all&count=30',
	'http://feeds.wsjonline.com/wsj/video/careers/feed',
	'http://feeds.wsjonline.com/wsj/video/real-estate/feed',
	'http://www.marketwatch.com/rss/video/wsj.asp?type=wsj-package&query=Wendy Bounds',
	'http://feeds.wsjonline.com/wsj/video/small-business/feed',
	'http://feeds.wsjonline.com/wsj/video/journal-reports/feed',
	'http://www.marketwatch.com/mw2/rss/video/wsj.asp?type=wsj-package&query=Weekend+Conversations&count=30',
	'http://www.marketwatch.com/mw2/mediarss/wsj/copyflow.asp?type=wsj-package&query=New+York&count=30',
	'http://www.marketwatch.com/mw2/mediarss/wsj/copyflow.asp?type=wsj-package&query=Bay+Area&count=30',
	'http://feeds.wsjonline.com/wsj/video/special_reports']
regex = [r'^https?:\/\/[^\/]*wsj\.com', r'^https?:\/\/[^\/]*wsj\.net', r'^https?:\/\/[^\/]*wsjonline\.com', r'^https?:\/\/[^\/]*feedburner\.com', r'^https?:\/\/[^\/]*marketwatch\.com']
videoregex = [r'video']
liveregex = [r'live']