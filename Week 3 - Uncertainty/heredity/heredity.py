import csv
import itertools
from random import triangular
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    p = [] # list we'll store each P(has gene) * P(has trait) in
    
    for name in people:
        # get # of genes
        if name in one_gene:
            has_gene = 1
        if name in two_genes:
            has_gene = 2
        else: has_gene = 0
        # get trait: true/false
        has_trait = name in have_trait

        mother, father = people[name]["mother"], people[name]["father"]
        if mother and father:
            # getting probilities for inheriting from mother / father
            if mother in two_genes:
                p_mother = 1-PROBS["mutation"]
            elif mother in one_gene:
                p_mother = .5
            else: p_mother = PROBS["mutation"]

            if father in two_genes:
                p_father = 1-PROBS["mutation"]
            elif father in one_gene:
                p_father = .5
            else: p_father = PROBS["mutation"]

            #calculating odds of getting gene from parents
            if has_gene == 2:
                x = p_mother*p_father
            elif has_gene == 1:
                x = (1- p_mother) * p_father + p_mother * (1 - p_father)
            else:
                x = (1 - p_mother) * (1 - p_father)
            y = PROBS['trait'][has_gene][has_trait]
            p.append(x*y)
        else:
            #no parents data
            x = PROBS['gene'][has_gene]
            y = PROBS['trait'][has_gene][has_trait]
            p.append(x*y)

    # combine joint probabilities
    a = 1
    for i in p:
        a *= i
    return a


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            has_gene = 1
        elif person in two_genes:
            has_gene = 2
        else: has_gene = 0
        if person in have_trait:
            has_trait = True
        else:
            has_trait = False
        probabilities[person]['gene'][has_gene] += p
        probabilities[person]['trait'][has_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        # normalize genes, find total genes and divide each probability by total
        total_gene = sum(probabilities[person]['gene'].values())
        probabilities[person]['gene'] = {genes: pgene / total_gene for genes, pgene in probabilities[person]['gene'].items()}
        
        # normalize traits, find total traits and divide each probability by total
        total_trait = sum(probabilities[person]['trait'].values())
        probabilities[person]['trait'] = {trait: ptrait/total_trait for trait, ptrait in probabilities[person]['trait'].items()}
        



if __name__ == "__main__":
    main()
