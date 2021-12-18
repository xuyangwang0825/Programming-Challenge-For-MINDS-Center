import json
from textblob import TextBlob
from pre_process import pre_process

def sentiment_analysis(str):
    sentiment = TextBlob(str)
    return sentiment.sentiment.polarity

def compute():
    sentiment_result = {}

    try:
        fd = open("./data.json", 'r')
        data = json.load(fd)
    except:
        data = pre_process()

    for k,v in data.items():
        sentiment_result[k] = {}
        sentiment_result[k]["res"] = []
        sum, count = 0, 0
        for sentence in v:
            polarity = sentiment_analysis(sentence)
            sentiment_result[k]["res"].append(polarity)
            sum += polarity
            count += 1
        avg = sum / count
        sentiment_result[k]["avg"] = avg
        sentiment_result[k]["count"] = count
    return sentiment_result

# print(compute())