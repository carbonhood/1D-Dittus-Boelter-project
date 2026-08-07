import os

import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
import torch.nn as nn
import torch.nn.functional as functional


MODEL_PATH = "data/model.pth"
hidden_layer1_size = 64
hidden_layer2_size = 32


# Columns: temp, rho, cp, mu, k, diameter, velocity, Re, Pr, Nu, h
# Use the 7 physical inputs only (exclude Re, Pr, Nu) and predict h
def prepare_data():
    data = numpy.loadtxt("data/data.csv", delimiter=",", skiprows=1)

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

    features_train_tensor = torch.tensor(features_train_scaled, dtype=torch.float32)
    target_train_tensor = torch.tensor(target_train_scaled, dtype=torch.float32)
    features_test_tensor = torch.tensor(features_test_scaled, dtype=torch.float32)
    target_test_tensor = torch.tensor(target_test_scaled, dtype=torch.float32)

    print(f"Features shape: {features.shape}")
    print(f"Target shape: {target.shape}")

    return (
        features_train_tensor,
        target_train_tensor,
        features_test_tensor,
        target_test_tensor,
    )


class DittusBoelterModel(nn.Module):
    def __init__(self, input_size, hidden_layer1_size, hidden_layer2_size, output_size):
        super(DittusBoelterModel, self).__init__()
        self.hidden_layer1 = nn.Linear(input_size, hidden_layer1_size)
        self.hidden_layer2 = nn.Linear(hidden_layer1_size, hidden_layer2_size)
        self.output_layer = nn.Linear(hidden_layer2_size, output_size)

    def forward(self, x):
        x = functional.relu(self.hidden_layer1(x))
        x = functional.relu(self.hidden_layer2(x))
        x = self.output_layer(x)
        return x


def build_model(input_size=7, output_size=1):
    model = DittusBoelterModel(
        input_size, hidden_layer1_size, hidden_layer2_size, output_size
    )
    return model


def create_model():
    model = build_model()
    print(model)
    print("Created a new model from scratch")
    return model, None


def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"No saved model found at {path}. Create a new model first."
        )

    model = build_model()
    try:
        checkpoint = torch.load(path, weights_only=False)
    except TypeError:
        checkpoint = torch.load(path)
    model.load_state_dict(checkpoint["model_state_dict"])
    print(model)
    print(
        f"Loaded existing model from {path} "
        f"(trained through epoch {checkpoint.get('epoch', '?')})"
    )
    return model, checkpoint
