import pandas as pd
import math
from scipy.stats import shapiro, anderson

# load data from file
df = pd.read_csv('shapiro.txt')

# convert p value to -log10(p-value)
df['log_pvalue'] = -1 * df['p value'].apply(lambda x: math.log10(x))

# check for linearity using Shapiro-Wilk test
stat, p = shapiro(df['log_pvalue'])
if p > 0.05:
    print("Data is normally distributed (fail to reject H0)")
else:
    print("Data is not normally distributed (reject H0)")

# check for linearity using Anderson-Darling test
result = anderson(df['log_pvalue'], dist='norm')
if result.statistic < result.critical_values[2]:
    print("Data is normally distributed (fail to reject H0)")
else:
    print("Data is not normally distributed (reject H0)")

