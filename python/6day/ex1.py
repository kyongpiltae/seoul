import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

print("start")
x = [[ i ] for i in range(10) ]
y = [[ np.random.random()*10 ] for _ in range(10) ]
regr = linear_model.LinearRegression()

print("x shape {} y shape {}".format(len(x),len(y)))
regr.fit(x, y)
print(regr.coef_)

# N -> N,1 행렬로 만드는 방법.
#df.X.values.reshape(N,1)
#df.data[:,np.newaxis,2]


from sklearn import datasets,neighbors


# %% 
%matplotlib inline
import numpy as np
import matplotlib as plt
from sklearn import datasets, neighbors
# Load the iris dataset
iris = datasets.load_iris()


# %%
iris_X = iris.data[:, :2]
iris_y = iris.target

n_neighbors = 15
# Create KNeighborsClassifier object
neigh = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
# Train the model using the training sets
neigh.fit(iris_X, iris_y)


new_sample = [[3.7, 4.5]]
iris_class = neigh.predict(new_sample)
print('The iris class for new sample:', iris.target_names[iris_class[0]])
# %% 
import matplotlib.colors as matcol
import matplotlib.pyplot as plt
cmap_iris = matcol.ListedColormap(['#ff0000', '#00ff00', '#0000ff'])
plt.scatter(iris_X[:, 0], iris_X[:, 1], c=iris_y,cmap=cmap_iris)


# %%
%matplotlib inline
import numpy as np
import matplotlib as plt
from sklearn import datasets, tree
# Load the iris dataset
iris = datasets.load_iris()
# Train with DecisionTreeClassifier
dt = tree.DecisionTreeClassifier()
dt.fit(iris.data, iris.target)
a = dt.predict([[4.8, 3.1, 1.5, 0.2]])
print(a)
# %%
import io
import pydotplus
# Convert the decision tree in dot language code
dot_data = io.StringIO()
tree.export_graphviz(dt, out_file=dot_data, feature_names=iris.feature_names,
class_names=iris.target_names, filled=True, rounded=True,
special_characters=True)
# Transform dot language code to graph by calling GraphViz
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')

# %%
arr1 = np.arange(27).reshape(3,3,3)

# %%
