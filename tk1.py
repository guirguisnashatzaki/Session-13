from tkinter import *
import linearRegressionmodel

class LinearRegressionApp:
    
    coef = 0.0
    intercept = 0.0
    
    def __init__(self, root, coef, intercept):
        self.coef = coef
        self.intercept = intercept
        self.root = root
        self.root.geometry("500x300")
        self.root.title("Salary prediction")
        self.root.configure(bg="white")

        # Title
        title = Label(self.root, text="AMIT-Machine learning Diploma", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", pady=10)
        title.pack(fill=X)

        # Input for x value
        frame = Frame(self.root, bg="white", pady=20)
        frame.pack(fill=X, padx=20)

        Label(frame, text="Enter years of experience:", font=("Arial", 14), bg="white").grid(row=0, column=0, pady=10, sticky=W)
        self.entry_x = Entry(frame, font=("Arial", 14), width=10)
        self.entry_x.grid(row=0, column=1, pady=10)

        # Button to calculate y
        btn_calculate_y = Button(self.root, text="Execute", command=self.calculate_y, font=("Arial", 14), bg="#4CAF50", fg="white")
        btn_calculate_y.pack(pady=10)

        # Display y value
        self.label_y = Label(self.root, text="", font=("Arial", 16), bg="white", fg="black")
        self.label_y.pack(pady=10)

    def calculate_y(self):
        try:
            x = float(self.entry_x.get())
            y = self.coef * x + self.intercept
            self.label_y.config(text=f"Your Expected Salary is:  {y:.2f}")
        except ValueError:
            self.label_y.config(text="Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    
    linear_model = linearRegressionmodel.linear_regression_model()
    
    root = Tk()
    app = LinearRegressionApp(root,linear_model.coefficient,linear_model.intercept)
    root.mainloop()
