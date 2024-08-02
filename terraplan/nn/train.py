import pandas as pd
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split

from nn.neural_network import Model
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model = Model()

def train_model():
    df = pd.read_csv(BASE_DIR / 'nn/data/soil_data.csv')
    X, y = sanitise_data(df)

    # Convert to numpy arrays
    X = X.values
    y = y.values

    # We will use 20% of our data for testing, 80% will be used for training the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Convert X feature to float tensors
    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)

    # Convert y features to float tensors
    y_train = torch.LongTensor(y_train)
    y_test = torch.LongTensor(y_test)

    # Set criterion of model to measure error, how far off the predictions are from the data
    criterion = nn.CrossEntropyLoss()

    # Choose an optimiser, lr = learning rate (if error does not go down after a bunch of training iterations,
    # lower the learning rate)
    optimiser = torch.optim.Adam(model.parameters(), lr=0.01)

    # Training the model
    # epoch - running all the data through the network one time
    epochs = 400
    losses = []
    for i in range(epochs):
        # Go forward and get a prediction
        y_pred = model.forward(X_train)

        # Measure the loss
        loss = criterion(y_pred, y_train)

        # Keep track of losses
        losses.append(loss)  # Convert loss from Tensor to numbers

        # Print ever 10 epochs (for testing purposes)
        # if i % 10 == 0:
        #     print(f'Epoch: {i} and loss: {loss}')

        # Back propagation
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()

    # Evaluate data
    with torch.no_grad():
        y_eval = model.forward(X_test)
        loss = criterion(y_eval, y_test)

    # This loss value must match the los on the last epoch or be very close to it
    print(f'Loss: {loss}')

    # Test the network
    correct = 0
    count = 0

    with torch.no_grad():
        for i, data in enumerate(X_test):
            y_val = model.forward(data)

            # Tell us what crop is good for that soil
            print(f'{i + 1}.) {str(y_val)} \t {y_test[i]}')

            if y_val.argmax().item() == y_test[i]:
                correct += 1
            count += 1

    print(f'Accuracy: {correct}/{count}')


def sanitise_data(df):
    # We need data in numbers rather than strings to make the neural
    # network more efficient at learning
    df['crop_type'] = df['crop_type'].replace('corn', 0.0)
    df['crop_type'] = df['crop_type'].replace('soybean', 1.0)
    df['crop_type'] = df['crop_type'].replace('wheat', 2.0)

    df['soil_type'] = df['soil_type'].replace('clayey', 0.0)
    df['soil_type'] = df['soil_type'].replace('sandy', 1.0)
    df['soil_type'] = df['soil_type'].replace('loamy', 2.0)

    X = df.drop([
        'sensor_id',
        'potassium_level', 'location_latitude', 'location_longitude', 'location_longitude',
        'soil_type', 'field_size', 'crop_type', 'timestamp'
    ], axis=1)
    y = df['crop_type']

    return X, y


def evaluate(data: list):
    new_crop = torch.tensor(data)
    with torch.no_grad():
        prediction = model(new_crop)
        return prediction.argmax().item()



