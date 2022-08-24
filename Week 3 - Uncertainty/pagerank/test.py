#from pagerank import transition_model, crawl, main
damping_factor = .85
page = '1.html'
corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}


dist = {}
    # {page number : probability}
    # initialize each (page #) with base probability
    # p = (1-damping)/(# of pages)
for i in corpus.keys():
    base = (1-damping_factor)/len(corpus.keys())
    dist[i] = base

# probability damping_factor choose link at random linked by page
# given a current page
if corpus[page]:
    # need to iterate over the values in corpus[page]
    for j in corpus[page]:
        dist[j] = base + (damping_factor)/len(corpus[page])
    print('corpus lenght: ', len(corpus[page]))
# if {page number : no links} then equal odds for all pages
else:
    dist = {}
    for i in corpus.keys():
        dist[i]= 1/len(corpus.keys())
    
print(dist)