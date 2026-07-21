import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score


column_names = [
    "pregnant",
    "glucose",
    "bp",
    "skin",
    "insulin",
    "bmi",
    "pedigree",
    "age",
    "label"
]

df = pd.read_csv("diabetes.csv")
df.columns = column_names


feature_sets = {
    "All Features":
        ["pregnant","glucose","bp","skin","insulin","bmi","pedigree","age"],

    "Without Insulin":
        ["pregnant","glucose","bp","skin","bmi","pedigree","age"],

    "Without Skin":
        ["pregnant","glucose","bp","insulin","bmi","pedigree","age"],

    "Important Features":
        ["glucose","bmi","age","pregnant","pedigree"]
}


criterions = ["gini", "entropy"]

depths = [3,4,5,6,7,8]

min_leaf = [1,2,5]

best_accuracy = 0
best_tree = None
best_features = None
best_parameters = None

print("="*60)

for feature_name, features in feature_sets.items():

    X = df[features]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42,
        stratify=y
    )

    for criterion in criterions:

        for depth in depths:

            for leaf in min_leaf:

                clf = DecisionTreeClassifier(
                    criterion=criterion,
                    max_depth=depth,
                    min_samples_leaf=leaf,
                    random_state=42
                )

                clf.fit(X_train, y_train)

                pred = clf.predict(X_test)

                acc = accuracy_score(y_test, pred)

                if acc > best_accuracy:

                    best_accuracy = acc
                    best_tree = clf
                    best_features = features

                    best_parameters = {
                        "criterion": criterion,
                        "max_depth": depth,
                        "min_samples_leaf": leaf
                    }

print("BEST MODEL")
print(best_parameters)
print("Features:", best_features)
print("Accuracy:", round(best_accuracy,4))

print("="*60)


X = df[best_features]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

best_tree.fit(X_train,y_train)

prediction = best_tree.predict(X_test)

accuracy = accuracy_score(y_test,prediction)
precision = precision_score(y_test,prediction)
recall = recall_score(y_test,prediction)

print("Accuracy :",accuracy)
print("Precision:",precision)
print("Recall   :",recall)


train_sizes = [0.5,0.6,0.7,0.8,0.9]

accuracy_scores = []
precision_scores = []

for size in train_sizes:

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        train_size=size,
        random_state=42,
        stratify=y
    )

    model = DecisionTreeClassifier(
        criterion=best_parameters["criterion"],
        max_depth=best_parameters["max_depth"],
        min_samples_leaf=best_parameters["min_samples_leaf"],
        random_state=42
    )

    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    accuracy_scores.append(
        accuracy_score(y_test,pred)
    )

    precision_scores.append(
        precision_score(y_test,pred)
    )

plt.figure(figsize=(8,5))

plt.plot(train_sizes,
         accuracy_scores,
         marker="o",
         label="Accuracy")

plt.plot(train_sizes,
         precision_scores,
         marker="o",
         label="Precision")

plt.xlabel("Training Set Proportion")
plt.ylabel("Score")
plt.title("Accuracy and Precision vs Training Set Size")
plt.grid(True)
plt.legend()

plt.savefig("accuracy_precision.png")
plt.close()


plt.figure(figsize=(18,10))

plot_tree(
    best_tree,
    feature_names=best_features,
    class_names=["No Diabetes","Diabetes"],
    filled=True,
    rounded=True
)

plt.savefig("decision_tree.png")
plt.close()

print("\nImages saved:")
print("accuracy_precision.png")
print("decision_tree.png")
