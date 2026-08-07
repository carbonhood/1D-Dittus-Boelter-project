import os

import torch
import torch.nn as nn

from create_model import MODEL_PATH


criterion = nn.MSELoss()
epochs = 30


def save_checkpoint(
    model, optimizer, epoch, feature_scaler=None, target_scaler=None, path=MODEL_PATH
):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(
        {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "feature_scaler": feature_scaler,
            "target_scaler": target_scaler,
        },
        path,
    )
    print(f"Checkpoint saved to {path} (epoch {epoch})")


def train_model(
    model,
    features_train_tensor,
    target_train_tensor,
    checkpoint=None,
    feature_scaler=None,
    target_scaler=None,
):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    start_epoch = 0

    if checkpoint is not None:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        start_epoch = checkpoint.get("epoch", 0)
        if feature_scaler is None:
            feature_scaler = checkpoint.get("feature_scaler")
        if target_scaler is None:
            target_scaler = checkpoint.get("target_scaler")
        print(f"Resuming training from epoch {start_epoch}")
    else:
        print("Starting training from scratch")

    end_epoch = start_epoch + epochs
    print(f"Training for {epochs} epochs (epochs {start_epoch + 1} to {end_epoch})")

    for epoch in range(start_epoch, end_epoch):
        model.train()
        optimizer.zero_grad()
        outputs = model(features_train_tensor)
        loss = criterion(outputs, target_train_tensor)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch + 1}, Loss: {loss.item()}")

    save_checkpoint(
        model, optimizer, end_epoch, feature_scaler, target_scaler, MODEL_PATH
    )
