# Iris Flower Classification 🌸

## Project Overview

This project uses a machine learning model to classify Iris flowers based on four numerical features. The model predicts the flower species using the measurements of its sepals and petals.

The project uses the **MLforKidsNumbers** library to communicate with a trained machine learning model and predict the species of Iris flowers.

## Dataset

The dataset is stored in `iris_dataset.xlsx` and contains measurements of Iris flowers.

The features used for classification are:

- `SepalLength`: Length of the sepal
- `SepalWidth`: Width of the sepal
- `PetalLength`: Length of the petal
- `PetalWidth`: Width of the petal

The target column is `Species`, which represents the flower species.

## Project Workflow

1. Load the Iris dataset from an Excel file using Pandas.
2. Split the dataset into training and testing sets using `train_test_split`.
3. Save the training and testing datasets as `train.xlsx` and `test.xlsx`.
4. Filter the training dataset to select flowers belonging to the `virginica` species.
5. Save the filtered data as `train_virginica.csv`.
6. Connect to the trained machine learning model using the `MLforKidsNumbers` library.
7. Submit flower measurements to the model for classification.
8. Predict the species of each flower in the test dataset.
9. Store the predicted species in a new column named `prediction`.
10. Save the results to `test.xlsx`.

## Model Prediction

The model receives four input features:

```python
testvalue = {
    "SepalLength": 5,
    "SepalWidth": 8,
    "PetalLength": 3,
    "PetalWidth": 0.2
}
```

The model returns the predicted flower species and its confidence score.



## Technologies Used

- Python
- Pandas
- OpenPyXL
- Scikit-learn
- MLforKidsNumbers
- Excel (.xlsx)
- CSV

## Output Files

| File | Description |
|---|---|
| `train.xlsx` | Training dataset |
| `test.xlsx` | Test dataset with predictions |
| `train_virginica.csv` | Training data filtered for the Virginica species |
| `a.png` | Screenshot of the software output and results |

## How to Run

1. Install the required Python libraries:

   ```bash
   pip install pandas openpyxl scikit-learn
   ```

2. Install or configure the `mlforkidsnumbers` package according to its documentation.

3. Place `iris_dataset.xlsx` and your Python script in the same directory.

4. Run the Python script.

5. Open `test.xlsx` to view the actual and predicted flower species.

## Conclusion

This project demonstrates how a machine learning model can classify Iris flowers using numerical measurements. It also demonstrates dataset splitting, data filtering, model inference, and saving prediction results to an Excel file.
