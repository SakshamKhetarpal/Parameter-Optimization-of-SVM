import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.svm import SVC
from scipy.stats import uniform

# Load the data
df = pd.read_csv("/Shill Bidding Dataset.csv")
df = df.drop(['Record_ID', 'Auction_ID', 'Bidder_ID'], axis=1)
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

# Initialize empty lists to store the results
best_kernel = []
best_nu = []
best_epsilon = []
best_accuracy = []

# Run the cross-validation experiment 10 times
for i in range(10):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=i)
    
    # Define the SVM model and the parameter distributions to be searched
    svc = SVC()
    param_distributions = {'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
                           'nu': uniform(0.01, 1.0),
                           'epsilon': uniform(0.01, 1.0)}
    
    # Run the randomized search with cross-validation
    random_search = RandomizedSearchCV(svc, param_distributions, n_iter=1000, cv=5, random_state=i)
    random_search.fit(X_train, y_train)
    
    # Store the best parameters and accuracy score
    best_kernel.append(random_search.best_params_['kernel'])
    best_nu.append(random_search.best_params_['nu'])
    best_epsilon.append(random_search.best_params_['epsilon'])
    best_accuracy.append(random_search.best_score_)

# Create a table to display the results
samples = ['Sample ' + str(i+1) for i in range(10)]
data = {'Sample Number': samples,
        'Best Accuracy': best_accuracy,
        'Best Kernel': best_kernel,
        'Best Nu': best_nu,
        'Best Epsilon': best_epsilon}
table = pd.DataFrame(data)
print(table)
