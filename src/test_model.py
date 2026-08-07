

## Test model will take in the input parameters from features_test_tensor and target_test_tensor and test the model against the test data

## the error calculation is simple arithmetic mean of the absolute difference between the predicted and actual values

## basically we need to loop over the test data and calculate the value that the model predicts 

## i think this is already pretty much done in train_model 

## then we need to sum up all of the errors over a 30 epoch run and divide by the number of epochs to get the errro

##make sure to have separation of feature and test data

import torch
import torch.nn as nn

test_iterations = 100
criterion = nn.L1Loss()

def test_model(model, features_test_tensor, target_test_tensor):
    
    with torch.no_grad():   
        prediction = model(features_test_tensor)
        error = criterion(prediction, target_test_tensor)
        return error

def test_multiple_times(model, features_test_tensor, target_test_tensor):
    total_error = 0
    model.eval()
    for _ in range(test_iterations):
        error = test_model(model, features_test_tensor, target_test_tensor)
        total_error += error.item()
    average_error = total_error / test_iterations
    print(f"Average error: {average_error}")
    return average_error

