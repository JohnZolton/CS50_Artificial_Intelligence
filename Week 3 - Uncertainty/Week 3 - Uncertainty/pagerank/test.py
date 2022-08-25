import random
#from pagerank import transition_model, crawl, main
damping_factor = .85
page = '1.html'
corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
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
        
    # if {page number : no links} then equal odds for all pages
    else:
        dist = {}
        for i in corpus.keys():
            dist[i]= 1/len(corpus.keys())
    
    return dist

dist1 = {}
    # choose a page at random
randpage = random.choice(list(corpus.keys()))
# add that probability to the distribution dictionary
dist1[randpage] = 1/1000
#choose rest of samples by using transition model from the first page
# transition model returns a probability distribution
# pick next page based on probability distribution

dist1 = {}
    # choose a page at random
randpage = random.choice(list(corpus.keys()))
# add that probability to the distribution dictionary
dist1[randpage] = 1/1000
    # choose rest of samples by using transition model from the first page
for i in range(1000-1):
    # transition model returns a probability distribution
    dist = transition_model(corpus, randpage, damping_factor)
    # pick next page based on probability distribution
    probdist = random.choices(list(dist.keys()), weights = dist.values(), k=1)
    if probdist[0] in dist1:
        dist1[probdist[0]] += 1/1000
    else:
         dist1[probdist[0]] = 1/1000
    print(dist1)   
print(sum(dist1.values())) 