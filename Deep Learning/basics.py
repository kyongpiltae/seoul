
#%%
import torch

x = torch.rand(5,3)
print(x)

y = torch.zeros(5,3)
print(y)

z = y.view(15)
print(z)

# %%
# converting 
a = torch.ones(5)
print(a)

b = a.numpy()
print(b)

# %%
import numpy as np
# converting numpy array to tensor
a = np.ones(5)
b = torch.from_numpy(a)
print(a)
print(b)

# %%
x=np.random.normal(size=100)
x.resize(2,50)

# %%
#Autograd
#automatic differentiation for all operations on Tensors

x = torch.ones(2, 2)
print(x)

x.requires_grad=True
print(x)

x = torch.zeros(2,2, requires_grad=True)
print(x)

# %%
y = x + 2
print(y)
z = y * y * 3
out = z.mean()
print(x.grad)

out.backward()

print(x.grad)

# %%
print(x.requires_grad)
y = x.detach()
print(y.requires_grad)

# %%
#Part A. Linear Regression
#In this part, we will implement a simple linear regressor with PyTorch

import matplotlib.pyplot as plt

x_values = [i for i in range(11)]
x_train = np.array(x_values, dtype=np.float32)
x_train = x_train.reshape(-1, 1)

y_values = [2*i + 1 for i in x_values]
y_train = np.array(y_values, dtype=np.float32)
y_train = y_train.reshape(-1, 1)

# %%
class linearRegression(torch.nn.Module):
    def __init__(self, inputSize, outputSize):
        super(linearRegression, self).__init__()
        self.linear = torch.nn.Linear(inputSize, outputSize)

    def forward(self, x):
        out = self.linear(x)
        return out
       
#%% 
inputDim = 1        # takes variable 'x' 
outputDim = 1       # takes variable 'y'
learningRate = 0.01 
epochs = 10


##### For GPU #######
model = linearRegression(inputDim, outputDim) 
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
model.to(device)

criterion = torch.nn.MSELoss() 
optimizer = torch.optim.SGD(model.parameters(), lr=learningRate)

#%%
# Model Training
inputDim = 1        # takes variable 'x' 
outputDim = 1       # takes variable 'y'
learningRate = 0.01 
epochs = 10


##### For GPU #######
model = linearRegression(inputDim, outputDim) 
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
model.to(device)

criterion = torch.nn.MSELoss() 
optimizer = torch.optim.SGD(model.parameters(), lr=learningRate)

#%%
for epoch in range(epochs):
    # Converting inputs and labels to Variable
    inputs = torch.from_numpy(x_train).to(device) 
    labels = torch.from_numpy(y_train).to(device)

    # Clear gradient buffers because we don't want gradients to accumulate after every epoch
    optimizer.zero_grad()

    # get output from the model, given the inputs
    outputs = model(inputs)

    # get loss for the predicted output
    loss = criterion(outputs, labels)
    print(loss)
    # get gradients w.r.t to parameters
    loss.backward()

    # update parameters
    optimizer.step()

    print('epoch {}, loss {}'.format(epoch, loss.item()))


#%%
with torch.no_grad():
  predicted = model(torch.from_numpy(x_train).to(device)).cpu().data.numpy()
print(predicted)

plt.clf()
plt.plot(x_train, y_train, 'go', label='True data', alpha=0.5)
plt.plot(x_train, predicted, '--', label='Predictions', alpha=0.5)
plt.legend(loc='best')
plt.show()

# %%
'''
Part B. Logistic Regression
In this part, we will identify handwritten digits using Logistic Regression in PyTorch
'''

import torch 
import torch.nn as nn 
import torchvision.datasets as dsets 
import torchvision.transforms as transforms 
from torch.autograd import Variable 

#%%

# MNIST Dataset (Images and Labels) 
train_dataset = dsets.MNIST(root ='./data',  
                            train = True,  
                            transform = transforms.ToTensor(), 
                            download = True) 
  
test_dataset = dsets.MNIST(root ='./data',  
                           train = False,  
                           transform = transforms.ToTensor())
#%%
# Hyper Parameters 
input_size = 784
num_classes = 10
num_epochs = 20
batch_size = 100
learning_rate = 0.001

#%%
# Dataset Loader (Input Pipline) 
train_loader = torch.utils.data.DataLoader(dataset = train_dataset,  
                                           batch_size = batch_size,  
                                           shuffle = True) 
  
test_loader = torch.utils.data.DataLoader(dataset = test_dataset,  
                                          batch_size = batch_size,  
                                          shuffle = False)

#%%
# Model 
class LogisticRegression(nn.Module): 
    def __init__(self, input_size, num_classes): 
        super(LogisticRegression, self).__init__() 
        self.linear = nn.Linear(input_size, num_classes) 
  
    def forward(self, x): 
        out = self.linear(x) 
        return out 

model = LogisticRegression(input_size, num_classes).to(device)
  
# Loss and Optimizer 
# Softmax is internally computed. 
# Set parameters to be updated. 
criterion = nn.CrossEntropyLoss() 
optimizer = torch.optim.SGD(model.parameters(), lr = learning_rate)        


# %%
# Training the Model 
for epoch in range(num_epochs): 
    for i, (images, labels) in enumerate(train_loader): 
        images = images.view(-1, 28 * 28).to(device)
        labels = labels.to(device)
  
        # Forward + Backward + Optimize 
        optimizer.zero_grad() 
        outputs = model(images) 
        loss = criterion(outputs, labels) 
        loss.backward() 
        optimizer.step() 
  
        if (i + 1) % 100 == 0: 
            print(f'Epoch: [{epoch +1}/{num_epochs}],\
            Step: [{i+1}/{len(train_dataset)//batch_size}], Loss: {loss.data}')

#%% 
# Test the Model 
correct = 0
total = 0
for images, labels in test_loader: 
    images = images.view(-1, 28 * 28).to(device)
    outputs = model(images).cpu()
    _, predicted = torch.max(outputs.data, 1) 
    total += labels.size(0) 
    correct += (predicted == labels).sum() 
  
print(f'Accuracy of the model on the 10000 test images: {100*correct/total}')            