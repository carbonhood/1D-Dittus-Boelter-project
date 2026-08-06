import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn 
import torch.nn.functional as functional



# Columns: temp, rho, cp, mu, k, diameter, velocity, Re, Pr, Nu, h
# Use the 7 physical inputs only (exclude Re, Pr, Nu) and predict h
data = numpy.loadtxt('data/data.csv', delimiter=',', skiprows=1)

hidden_layer1_size = 64
hidden_layer2_size = 32

features = data[:, :7]
target = data[:, -1].reshape(-1, 1)

features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

feature_scaler = StandardScaler()
target_scaler = StandardScaler()

features_train_scaled = feature_scaler.fit_transform(features_train)
features_test_scaled = feature_scaler.transform(features_test)
target_train_scaled = target_scaler.fit_transform(target_train)
target_test_scaled = target_scaler.transform(target_test)

print(f"Features shape: {features.shape}")
print(f"Target shape: {target.shape}")
print(f"Train features shape: {features_train_scaled.shape}")
print(f"Train target shape: {target_train_scaled.shape}")

class DittusBoelterModel(nn.Module):
    def __init__(self, features_train_scaled, hidden_layer1_size, hidden_layer2_size, target_train_scaled):
        super(DittusBoelterModel, self).__init__()

        self.hidden_layer1 = nn.Linear(features_train_scaled.shape[1], hidden_layer1_size)

        self.hidden_layer2 = nn.Linear(hidden_layer1_size, hidden_layer2_size)

        self.output_layer = nn.Linear(hidden_layer2_size, target_train_scaled.shape[1])

    def forward(self, x):
        x = functional.relu(self.hidden_layer1(x))
        x = functional.relu(self.hidden_layer2(x))
        x = self.output_layer(x)
        return x

model = DittusBoelterModel(features_train_scaled, hidden_layer1_size, hidden_layer2_size, target_train_scaled)

print(model)