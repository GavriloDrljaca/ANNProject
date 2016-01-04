from urllib2 import Request, urlopen, URLError
import json

#tag can be sport, politics and etc, date is in YYYY-MM-DD format
def get_train_tweets(tag, number_of_pages, date):
    request_string = 'http://influencedb.com/buzz-api/api/twitter/tweets?skip=0&take='+number_of_pages+'&tags='+tag+'&cacheOnly=false&showResultsFromSolr=false&isoDate='+date+'&language=en&_=1451483470386'
    request = Request(request_string)
    try:
        response = urlopen(request)
        tweets = response.read()
    except URLError, e:
        print "Error retrieving tweets from influence.db ",e

    json_tweets = json.loads(tweets);

    tweetsID = []
    for tw in json_tweets['data']:
        id_string = tw['statusId']
        #id_string = id_string.lstrip()
        tweetsID.append(int (id_string))
    return tweetsID
