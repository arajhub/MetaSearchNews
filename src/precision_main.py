#Precision = No. of relevant documents retrieved / No. of total documents retrieved
import csv
'''
Find precision@5, precision@10, precision@15, precision@20, precision@25, precision@30 with respect to the ranked aggregated collections formed based on
ranking approach 1 and approach 2 (i.e. ResultantRanks_A1.txt and ResultantRanks_A2.txt respectively).

ResultantRanks_A1.txt compared with RankedDocuments.csv

P@5 = 1 / 5 = 0.2
P@10 = 3 / 10 = 0.3
P@15 = 8 / 15 = 0.533
P@20 = 10 / 20 = 0.5
P@25 = 11 / 25 = 0.44
P@30 = 14 / 30 = 0.46

ResultantRanks_A2.txt compared with RankedDocuments.csv

P@5 = 2 / 5 = 0.1
P@10 = 4 / 10 = 0.4
P@15 = 6 / 15 = 0.4
P@20 = 13 / 20 = 0.65
P@25 = 15 / 25 = 0.6
P@30 = 25 / 30 = 0.833

'''

import pandas as pd
import glob

manual_ranked_fileName = "/Users/aaraj/PycharmProjects/MetaSearchNews/RankedDocuments.csv"
df_manual = pd.read_csv(manual_ranked_fileName, index_col=None, header=1)

rank_a2_file = "/Users/aaraj/PycharmProjects/MetaSearchNews/ResultantRanks_A2.txt"
df_rank_A2 = pd.read_csv(rank_a2_file, sep="\t", index_col=None, header=1)

print(df_rank_A2)
print(df_manual.join(df_rank_A2, rsuffix="r_"))


