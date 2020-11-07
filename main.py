import spider

sp = spider.twitter_spider()

data = sp.make_request("realDonaldTrump")

print(data)