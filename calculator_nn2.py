## ---- Use pytorch to train an addition, subtraction, multiplication and division calculator neural network, and randomly generate training and test data for addition, subtraction, multiplication and division. save model params and use model predict ' 32 * 3 = ? '

# To create a neural network in PyTorch that can perform basic arithmetic operations (addition, subtraction, multiplication, and division), we'll follow these steps:

# 1. **Define the Neural Network Architecture**: A simple feedforward neural network will suffice for this task.
# 2. **Generate Training and Test Data**: Randomly generate numbers and their corresponding arithmetic operations.
# 3. **Train the Model**: Use the generated data to train the model.
# 4. **Save the Model Parameters**: After training, save the model's parameters for later use.
# 5. **Predict an Arithmetic Operation**: Load the saved model and use it to predict the result of an operation like `32 * 3 = ?`.

# Let's start with the implementation:

# ### Step 1: Define the Neural Network Architecture

# We'll define a simple feedforward neural network with a few fully connected layers.

# ```python
import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np

# Define the neural network architecture
class CalculatorNN(nn.Module):
    def __init__(self):
        super(CalculatorNN, self).__init__()
        self.fc1 = nn.Linear(3, 128)  # Input: 2 numbers + operation
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)   # Output: the result

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
# ```

# ### Step 2: Generate Training and Test Data

# We will randomly generate pairs of numbers and apply the four operations.

# ```python
# Function to generate random training data
def generate_data(num_samples=10000):
    data = []
    for _ in range(num_samples):
        num1 = random.uniform(1, 100)
        num2 = random.uniform(1, 100)
        op = random.choice(['+', '-', '*', '/'])

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2

        data.append([num1, num2, op, result])

    return data

# Convert data to tensors
def preprocess_data(data):
    X, y = [], []
    for num1, num2, op, result in data:
        op_encoding = {'+': 0, '-': 1, '*': 2, '/': 3}[op]
        X.append([num1, num2, op_encoding])
        y.append(result)

    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).view(-1, 1)
    return X, y

# Generate and preprocess training data
train_data = generate_data(10000)
X_train, y_train = preprocess_data(train_data)

# Generate and preprocess test data
test_data = generate_data(1000)
X_test, y_test = preprocess_data(test_data)
# ```

# ### Step 3: Train the Model

# We'll set up the training loop to optimize the neural network.

# ```python
# Initialize the model, loss function, and optimizer
model = CalculatorNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 100
for epoch in range(num_epochs):
    model.train()

    # Forward pass
    predictions = model(X_train)
    loss = criterion(predictions, y_train)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
# ```

# ### Step 4: Save the Model Parameters

# After training, we'll save the model parameters.

# ```python
# Save the trained model parameters
torch.save(model.state_dict(), 'calculator_model.pth')
# ```

# ### Step 5: Predict an Arithmetic Operation

# Finally, we'll load the saved model and predict the result of `32 * 3`.

# ```python
# Load the model for inference
model = CalculatorNN()
model.load_state_dict(torch.load('calculator_model.pth'))
model.eval()

# Prepare the input (32 * 3)
input_data = torch.tensor([[32.0, 3.0, 2]], dtype=torch.float32)  # 2 corresponds to multiplication

# Perform the prediction
with torch.no_grad():
    prediction = model(input_data)
    print(f'Prediction for 32 * 3: {prediction.item():.4f}')
# ```

# This approach trains a simple feedforward neural network to perform basic arithmetic operations. The network learns to generalize from the training data, and once trained, it can be used to predict the result of unseen operations like `32 * 3`.

# ------- run -------
# @ python calculator_nn2.py
# Epoch [10/100], Loss: 2766880.7500
# Epoch [20/100], Loss: 2707016.0000
# Epoch [30/100], Loss: 2628090.2500
# Epoch [40/100], Loss: 2529375.0000
# Epoch [50/100], Loss: 2417974.7500
# Epoch [60/100], Loss: 2311074.5000
# Epoch [70/100], Loss: 2232561.0000
# Epoch [80/100], Loss: 2196610.5000
# Epoch [90/100], Loss: 2188764.2500
# Epoch [100/100], Loss: 2184328.2500
# /Users/emacspy/EmacsPyPro/emacspy-machine-learning/calculator_nn2.py:128: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
#   model.load_state_dict(torch.load('calculator_model.pth'))
# Prediction for 32 * 3: 296.8100
#
