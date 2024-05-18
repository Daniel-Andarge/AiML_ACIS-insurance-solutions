# A/B Hypothesis Testing

```python
import sys
import os
import pandas as pd
from IPython.display import display
```

## Import Functions

```python
import sys

sys.path.append('../scripts')
from data_preparation_utills.data_preprocessor import *
from exploratory_data_analysis.data_understanding import *
from exploratory_data_analysis.visualization_handler import *
from AB_hypothesis_testing.risk_analyzing import *
```

## Load Cleaned Dataset

```python
# path to the CSV file
filename = 'cleaned_MachineLearningRating_v3.csv'
path = os.path.join('..', 'local_storage', filename)

# Load dataset
cleaned_dataset = load_dataset(path)
```

## Test 1

### Null Hypothesis: There are no risk differences across provinces

#### Prepare the Data

```python
prepared_data = prepare_data(cleaned_dataset)
```

```python
df_prepared_data = pd.DataFrame(prepared_data)
```

#### Display the prepared data

```python
display(df_prepared_data)
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TotalClaims</th>
    </tr>
    <tr>
      <th>Province</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Eastern Cape</th>
      <td>1.356427e+06</td>
    </tr>
    <tr>
      <th>Free State</th>
      <td>3.549223e+05</td>
    </tr>
    <tr>
      <th>Gauteng</th>
      <td>2.939415e+07</td>
    </tr>
    <tr>
      <th>KwaZulu-Natal</th>
      <td>1.430138e+07</td>
    </tr>
    <tr>
      <th>Limpopo</th>
      <td>1.016477e+06</td>
    </tr>
    <tr>
      <th>Mpumalanga</th>
      <td>2.044675e+06</td>
    </tr>
    <tr>
      <th>North West</th>
      <td>5.920250e+06</td>
    </tr>
    <tr>
      <th>Northern Cape</th>
      <td>8.949051e+04</td>
    </tr>
    <tr>
      <th>Western Cape</th>
      <td>1.038977e+07</td>
    </tr>
  </tbody>
</table>
</div>

#### Perform chi-square test on total claims across provinces

```python
perform_hypothesis_test(df_prepared_data)
```

    Null Hypothesis: There are no risk differences across provinces.
    Chi-Square: 0.0
    P-value: 0
    Reject the null hypothesis. There are risk differences across provinces.

```python

```

## Test 2

### Null Hypothesis: There are no risk differences between zipcodes

### Prepare and group the data

```python
zip_code_column = 'PostalCode'
group_column = 'TotalClaims'
group_a_label = 7750
group_b_label = 7580
```

```python
group_A, group_B = prepare_group_data(cleaned_dataset, zip_code_column, group_column, group_a_label, group_b_label)
```

```python
display(group_A)
```

    5002      0.0
    5004      0.0
    5005      0.0
    5006      0.0
    5007      0.0
             ...
    996970    0.0
    996971    0.0
    996972    0.0
    996973    0.0
    996974    0.0
    Name: TotalClaims, Length: 9408, dtype: float64

```python
display(group_B)
```

    26624     0.0
    26625     0.0
    26626     0.0
    26627     0.0
    26628     0.0
             ...
    992624    0.0
    992626    0.0
    992628    0.0
    992630    0.0
    992632    0.0
    Name: TotalClaims, Length: 2815, dtype: float64

### Perform test

```python
perform_ab_test(group_A, group_B)
```

    Null Hypothesis: There are no risk differences between zip codes.
    A/B Groups:
    Group A - Mean: 39.0206579133846 Standard Deviation: 1770.0128643315438
    Group B - Mean: 10.19111900532859 Standard Deviation: 372.4131384128883
    T-Statistic: 0.8584822540622764
    P-value: 0.39064306215409383
    Accept the null hypothesis. There are no risk differences between zip codes.

```python

```
