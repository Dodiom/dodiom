# Dodiom Datasets

In this folder you can download the datasets created by the Dodiom community. 

For Turkish and Italian, one CSV and one Excel file are provided.

## Dataset Structure

Dataset consists of X columns:

| Column        | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| idiom         | Name of the idiom                                            |
| submission    | Content of the submission                                    |
| category      | Submission category (idiom or nonidiom)                      |
| rating        | likes / total votes                                          |
| likes         | number of likes                                              |
| dislikes      | number of dislikes                                           |
| reports       | number of reports                                            |
| idiom_indices | submission token indices which are associated with the idiom |
| idiom_words   | submission words that are associated with the idiom          |
| lemmas        | Lemmas of the submission                                     |
| words         | Words of the submission                                      |

## Example Usage

You can easily load the dataset with [Pandas](https://pandas.pydata.org) like this:

````py
import pandas as pd

dataset = pd.read_csv("dataset_tr.csv")

print(len(dataset))  # prints 6861
````

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png).

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)