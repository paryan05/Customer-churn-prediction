# Customer Churn Prediction

![Customer Churn Prediction](https://img.shields.io/badge/Project-Customer%20Churn%20Prediction-brightgreen)


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Customer churn prediction is a critical task for businesses, especially in the telecommunications industry. This project aims to predict whether a customer will churn based on various features such as tenure, monthly charges, and service usage.Logistic Regression Model is trained and saved for predicting and is deployed as a web application using Streamlit. By leveraging machine learning, this project provides insights that can help companies improve customer retention strategies.

## Features

- **Predictive Modeling**: Utilizes a Logistic Regression Model to predict customer churn.
- **User -Friendly Interface**: A web application built with Streamlit for easy interaction.
- **Data Preprocessing**: Handles missing values and categorical variables to prepare data for modeling.
- **Real-Time Predictions**: Users can input customer data and receive immediate predictions on churn likelihood.

## Technologies Used

- **Python**: The primary programming language used for data analysis and model building.
- **Pandas**: A powerful data manipulation and analysis library.
- **NumPy**: A library for numerical computations and handling arrays.
- **Scikit-learn**: A machine learning library for model training, evaluation, and preprocessing.
- **Streamlit**: A framework for building interactive web applications.
- **Joblib**: A library for saving and loading Python objects, such as trained models.

## Dataset

The dataset used in this project is the Telco Customer Churn dataset, which contains information about customers and their subscription details. The dataset includes features such as:

- Customer demographics (gender, partner status, dependents)
- Account information (tenure, monthly charges, total charges)
- Services used (internet service, online security, tech support)
- Churn status (target variable)

The dataset can be found in the `data` folder as `Telco-Customer-Churn.csv`.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Customer-Churn-Prediction.git
   cd Customer-Churn-Prediction

## Usage

1. **Train the Model**:
   - Open the Jupyter Notebook for model training. You can find it in the `notebook` directory, typically named `customer_churn.ipynb`.
   - Run all the cells in the notebook to preprocess the data, train the model, and save the model and preprocessor. Make sure to execute the cells in order to ensure that all dependencies are loaded correctly.

2. **Run the Streamlit Application**:
   - After training the model, start the Streamlit app to make predictions:
   ```bash
   streamlit run app.py

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request. Please ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

