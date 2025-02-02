from sklearn.metrics import classification_report
from tuw_nlp.common.eval import get_cat_stats, print_cat_stats

from brise_plandok.baselines.constants import NOT, ALL_LABELS_SORTED, RULE_BASED_ATTRIBUTES
from brise_plandok.baselines.utils import (
    get_x_y_dataframes,
    filter_gold_list,
    get_attributes_for_experiment,
)
from brise_plandok.constants import TRAIN, VALID


class BaselineClassifier:
    def __init__(self, name, classifier, top=None, min_freq=11):
        self.name = name
        self.classifier = classifier
        self.top = len(ALL_LABELS_SORTED.keys()) if top is None else top
        self.min_freq = 1 if min_freq is None else min_freq
        self.labels = get_attributes_for_experiment(self.top, self.min_freq)

    def run(self, hyperparams=None):
        if hyperparams is None:
            hyperparams = {}
        print(f"# {self.name} classifier - report")
        print(f"Run for attributes: top {self.top}, with minimum frequency of {self.min_freq}.")
        print(f"Run with hyperparams: {hyperparams}.")
        _, x_train, y_train_all_labels = get_x_y_dataframes(TRAIN)
        _, x_valid, y_valid_all_labels = get_x_y_dataframes(VALID)
        golds = y_valid_all_labels.Labels.tolist()
        golds = filter_gold_list(golds, self.labels)
        preds = [set() for _ in range(len(golds))]
        for label in self.labels:
            print(f"## {label}")
            print("```bash")
            y_train = y_train_all_labels.loc[:, [label]]
            y_valid = y_valid_all_labels.loc[:, [label]]
            self._fit(x_train, y_train[label], x_train.columns.tolist())
            y_pred = self.classifier.predict(x_valid)
            for i, pred in enumerate(y_pred):
                if pred > 0.5:
                    preds[i].add(label)
            print(
                classification_report(
                    y_valid[label], y_pred, labels=[0, 1], target_names=[NOT, label]
                )
            )
            self._additional_output_for_label(
                self.classifier, x_train.columns.tolist(), [NOT, label], label
            )
            print("```")
        print("## Summary")
        print_cat_stats(get_cat_stats(preds, golds))
        print()
        print("## Summary - only with rule based attributes")
        print_cat_stats(get_cat_stats(preds, golds, RULE_BASED_ATTRIBUTES, True))

    def _fit(self, x, y, feature_names=None):
        self.classifier = self.classifier.fit(x, y)

    def _additional_output_for_label(self, clf, feature_names, class_names, label):
        pass
