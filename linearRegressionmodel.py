import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')


class linear_regression_model:
    
    coefficient = 0.0
    intercept = 0.0
    
    def __init__(self):
        self.run_my_model()
        
    def run_my_model(self):
        data = pd.read_csv("Salary_Data.csv")

        print(data.describe())


        plt.figure(figsize=(3,3))
        sns.scatterplot(x="YearsExperience",y="Salary",data=data)
        plt.title("Salary vs Experience")
        plt.show()

        x = data.iloc[:,:-1]
        y = data.iloc[:,-1]

        x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,random_state=10)

        my_model = LinearRegression()
        my_model.fit(x_train,y_train)

        plt.scatter(x_train, y_train, color = 'red')
        plt.scatter(x_test, y_test, color='green', label='Test data')
        plt.plot(x_train, my_model.predict(x_train), color = 'blue')
        plt.title('Salary vs Experience (Training set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.show()

        print('Intercept of the model:',my_model.intercept_)
        print('Coefficient of the line:',my_model.coef_[0])
        self.coefficient = my_model.coef_[0]
        self.intercept = my_model.intercept_

            

