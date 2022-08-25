import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


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


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dist1 = {}
    # choose a page at random
    randpage = random.choice(list(corpus.keys()))
    # add that probability to the distribution dictionary
    dist1[randpage] = 1/n
    # choose rest of samples by using transition model from the first page
    for i in range(n-1):
        # transition model returns a probability distribution
        dist = transition_model(corpus, randpage, damping_factor)
        # pick next page based on probability distribution
        probdist = random.choices(list(dist.keys()), weights = dist.values(), k=1)
        if probdist[0] in dist1:
            dist1[probdist[0]] += 1/n
        else:
            dist1[probdist[0]] = 1/n
    return dist1


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    return NotImplementedError


if __name__ == "__main__":
    main()
