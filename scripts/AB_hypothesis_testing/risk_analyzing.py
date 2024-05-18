
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

from scipy.stats import ttest_ind


def prepare_data(data):
    # Select relevant columns for analysis
    columns_of_interest = ['Province', 'TotalClaims']
    data = data[columns_of_interest]

    # Calculate the total claims for each province
    province_claim_totals = data.groupby('Province')['TotalClaims'].sum()

    # Remove any provinces with missing or zero total claims (optional)
    province_claim_totals = province_claim_totals[province_claim_totals > 0]

    return province_claim_totals



def perform_hypothesis_test(data):
    # Perform chi-square test 
    observed = data.values.reshape(-1, 1) 
    expected = np.mean(data.values)

    # null hypothesis
    null_hypothesis = "There are no risk differences across provinces."

    # Perform chi-square test
    chi_square, _, p_value, _ = chi2_contingency(observed)

    # significance level
    alpha = 0.05

    # Print the test results
    print("Null Hypothesis:", null_hypothesis)
    print("Chi-Square:", chi_square)
    print("P-value:", p_value)

    # Accept or reject the null hypothesis based on the p-value
    if p_value < alpha:
        print("Reject the null hypothesis. There are risk differences across provinces.")
    else:
        print("Accept the null hypothesis. There are no risk differences across provinces.")




def prepare_group_data(data, zip_code_column, group_column, group_a_label, group_b_label):

    grouped_data = data.groupby(zip_code_column)[group_column]

    group_A = grouped_data.get_group(group_a_label)
    group_B = grouped_data.get_group(group_b_label)

    return group_A, group_B



def perform_ab_test(group_A, group_B, alpha=0.05):

    # t-test for independent samples
    t_statistic, p_value = ttest_ind(group_A, group_B)

    # Print the test results
    print("Null Hypothesis: There are no risk differences between zip codes.")
    print("A/B Groups:")
    print("Group A - Mean:", group_A.mean(), "Standard Deviation:", group_A.std())
    print("Group B - Mean:", group_B.mean(), "Standard Deviation:", group_B.std())
    print("T-Statistic:", t_statistic)
    print("P-value:", p_value)

   
    if p_value < alpha:
        print("Reject the null hypothesis. There are risk differences between zip codes.")
    else:
        print("Accept the null hypothesis. There are no risk differences between zip codes.")


