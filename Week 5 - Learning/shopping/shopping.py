import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer - 0
        - Administrative_Duration, a floating point number - 1
        - Informational, an integer - 2
        - Informational_Duration, a floating point number - 3 
        - ProductRelated, an integer - 4 
        - ProductRelated_Duration, a floating point number - 5
        - BounceRates, a floating point number - 6
        - ExitRates, a floating point number - 7
        - PageValues, a floating point number - 8
        - SpecialDay, a floating point number - 9
        - Month, an index from 0 (January) to 11 (December) - 10
        - OperatingSystems, an integer - 11
        - Browser, an integer - 12
        - Region, an integer - 13
        - TrafficType, an integer - 14
        - VisitorType, an integer 0 (not returning) or 1 (returning) - 15
        - Weekend, an integer 0 (if false) or 1 (if true) - 16

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    labels = []
    evidence = []
    months = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'April':3, 'May': 4, 'June': 5, 'Jul':6,
    'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec':11}
    with open(filename, newline = "") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip first row
        for row in reader:
            formatted = [
                int(row[0]), float(row[1]), int(row[2]), float(row[3]), int(row[4]),
                float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]),
                int(months[row[10]]),
                int(row[11]), int(row[12]), int(row[13]), int(row[14]),
                int(1) if row[15]=='Returning_Visitor' else int(0), 
                int(1) if row[16] == 'TRUE' else int(0)
            ]
            if row[17] == "TRUE": 
                label = 1
            else: 
                label = 0

            evidence.append(formatted)
            labels.append(label)
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors= 1)
    model.fit(evidence, labels)
    return model

def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    true_positives = 0
    true_negatives = 0
    total = 0
    for actual, predicted in zip(labels, predictions):
        total += 1
        if actual == predicted:
            if actual == 1: 
                true_positives +=1
            else: true_negatives +=1
    sensitivity = true_positives/total
    specificity = true_negatives/total
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
