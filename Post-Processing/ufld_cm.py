import os
import ast

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

folders = {"0_100": None, "30_70": None, "40_60": None, "50_50": None, "60_40": None, "70_30": None, "100_0": None}
fp_dict = {"0-100": None, "30-70": None, "40-60": None, "50-50": None, "60-40": None, "70-30": None, "100-0": None}
fn_dict = {"0-100": None, "30-70": None, "40-60": None, "50-50": None, "60-40": None, "70-30": None, "100-0": None}
tp_dict = {"0-100": None, "30-70": None, "40-60": None, "50-50": None, "60-40": None, "70-30": None, "100-0": None}
tn_dict = {"0-100": None, "30-70": None, "40-60": None, "50-50": None, "60-40": None, "70-30": None, "100-0": None}

root_path = "UFLD_results"
eval_file_name = "eval_result.txt"

for folder, key in zip(folders.keys(), fp_dict.keys()):
    eval_file = os.path.join(root_path, folder, eval_file_name)
    with open(eval_file, 'r') as r_file:
        lines = r_file.readlines()
        lines = ast.literal_eval(lines[0])

        for line in lines:
            if line['name'] == "FP":
                fp_dict[key] = int(line['value'] * 100)
            if line['name'] == "FN":
                fn_dict[key] = int(line['value'] * 100)
            if line['name'] == "TP":
                tp_dict[key] = int(line['value'] * 100)
            if line['name'] == "TN":
                tn_dict[key] = int(line['value'] * 100)


fp_val = list(fp_dict.values())
fn_val = list(fn_dict.values())
tp_val = list(tp_dict.values())
tn_val = list(tn_dict.values())

for name, FP, FN, TP, TN in zip(fp_dict.keys(), fp_val, fn_val, tp_val, tn_val):
    cf_matrix = [[TP, FP], [FN, TN]]
    labels = ['True Positive', 'False Positive', 'False Negative', 'True Negative']
    perc = [TP, FP, FN, TN]

    labels = [f"{v1}\n{v2}%" for v1, v2 in zip(labels, perc)]
    labels = np.asarray(labels).reshape(2, 2)

    sns.heatmap(cf_matrix, annot=labels, cmap='Blues', fmt='')
    plt.title(f"Confusion Matrix for Dataset Split {name}")
    plt.show()
