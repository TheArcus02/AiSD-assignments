## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/TheArcus02/AiSD-assignments.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Set the constant variables in main.py file. 

- MAX_LEN - Lenght of data array will contain
- STEP - Number of data sets to be messured
- ALGORITHM - Sorting algorithm used for setTimesComplexity function
- DATA_TYPE - Data type used for compareAlgorithms function
```python
from merge import merge_sort

def main():
    # constants
    MAX_LEN = 50000
    STEP = MAX_LEN // 15
    ALGORITHM = merge_sort
    DATA_TYPE = 'ascending'
    ...
```

Uncoment one of the following functions. To either generate plot for one algorithm but all data types or to generate plot for one data type but all algorithms.
```python
setTimesComplexity(MAX_LEN, STEP, ALGORITHM)
```
```python
compareAlgorithms(MAX_LEN, STEP, DATA_TYPE, [
                      insertion_sort, selection_sort, heap_sort, merge_sort])
```
To run the script:
```sh
py main.py
```




<!-- LICENSE -->
## License

Distributed under the MIT License.


