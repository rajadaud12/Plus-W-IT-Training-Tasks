
# Python Data Systems and Automation
## PLUS W - IT Training
*Date: March 6, 2025*

---

## 1. House Price Prediction with Linear Regression
The first section introduces linear regression for predicting house prices using scikit-learn.

### Core Concepts Covered

1. **Linear Regression Setup**
   - Model initialization and training
   - Feature selection and preprocessing
   - Target variable definition
   - Prediction generation

2. **House Price Analysis**
   - Dataset loading and cleaning
   - Categorical variable encoding
   - Numerical feature scaling
   - Model fitting and evaluation

3. **Plot Customization**
   - Predicted vs. actual price scatter plots
   - Regression line visualization
   - Axis labeling and titling
   - Visual clarity enhancement

4. **Evaluation Metrics**
   - Mean Squared Error (MSE)
   - R-squared score
   - Residual distribution analysis

---

## 2. Salary Prediction with Regression
The second section explores regression techniques for predicting salaries based on employee data.

### Key Components

1. **Salary Prediction Model**
   - Feature engineering (e.g., experience, role)
   - Data splitting for training/testing
   - Linear regression implementation
   - Prediction accuracy assessment

2. **Visualization Techniques**
   ```python
   # Scatter plot for salary prediction
   plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
   plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
   plt.xlabel('Actual Salary')
   plt.ylabel('Predicted Salary')
   plt.title('Salary Prediction Comparison')
   ```

3. **Salary Data Insights**
   - Trend identification
   - Error visualization
   - Outlier detection
   - Model performance tracking

4. **Metric Implementation**
   - MSE calculation
   - R-squared evaluation
   - Prediction interpretation

---

## 3. Stock Price Trend Prediction
The third section covers time series regression for predicting stock price trends.

### Implementation Details

1. **Stock Price Visualization**
   - Data retrieval with `yfinance`
   - Time series data preparation
   - Linear regression for trend prediction
   - Temporal pattern analysis

2. **Trend Visualization**
   - Line plot of historical prices
   - Scatter plot of predicted prices
   - Trend line overlay
   - Grid and legend integration

3. **Key Functions**
   ```python
   # Stock price trend prediction
   import yfinance as yf
   stock = yf.Ticker('AAPL')
   df = stock.history(period='5y')
   X = df[['Day']].values
   y = df['Close'].values
   model.fit(X_train, y_train)
   ```

---

## 4. Customer Churn Prediction with Logistic Regression
This section explores logistic regression for binary classification in customer churn analysis.

1. **Churn Prediction Setup**
   - Binary outcome encoding (0/1)
   - Feature preprocessing (one-hot encoding)
   - Logistic regression model training
   - Probability threshold adjustment

2. **Visualization Techniques**
   - Confusion matrix heatmap
   - Predicted vs. actual churn comparison
   - Class distribution visualization
   - Annotation for clarity

3. **Code Implementation**
   ```python
   # Confusion matrix visualization
   from sklearn.metrics import confusion_matrix
   import seaborn as sns
   cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
   sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
   plt.xlabel('Predicted')
   plt.ylabel('Actual')
   plt.title('Customer Churn Confusion Matrix')
   ```

4. **Evaluation Metrics**
   - Accuracy score
   - Precision, recall, and F1-score
   - Confusion matrix interpretation

---

## 5. Energy Consumption Prediction
The fifth section applies regression to predict energy consumption using multi-feature data.

1. **Energy Prediction Model**
   - Dataset preprocessing and feature selection
   - Linear regression training
   - Multi-dimensional analysis
   - Prediction generation

2. **Visualization Techniques**
   - Scatter plot of predicted vs. actual consumption
   - Regression line visualization
   - Error distribution plotting
   - Feature importance visualization

3. **Implementation Details**
   ```python
   # Energy consumption prediction
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   model = LinearRegression()
   model.fit(X_train, y_train)
   y_pred = model.predict(X_test)
   ```

4. **Performance Metrics**
   - Mean Squared Error (MSE)
   - R-squared score
   - Prediction error analysis
   - Model optimization potential

---

*Note: This documentation covers the implementation of regression-based prediction tasks for Assignment #7 using scikit-learn and visualization libraries. For detailed code examples and datasets, refer to the accompanying Jupyter Notebook (`assignment_7.ipynb`).*

---
