import ezgmail, webbrowser
from urlextract import URLExtract

resultThreads = ezgmail.search('unsubscribe')
for x in resultThreads:
    summary = ''.join(list(str(x)))
    extractor = URLExtract()
    urls = extractor.find_urls(summary)
    if urls != []:
        webbrowser.open(urls[-1])