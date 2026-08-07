## here we need to unscale the numbers from the prediction to get the actual values

## then we will print with units

## this will be an input parameters ----> recieve a predicted H, the final part of the project

## then it will loop over again and ask if wanting to make more predictions

## start with a function that will take in user made inputs for temperature, diameter, and velocity and return the predicted H

## then we will unscale the prediction from the model and print with units

import torch
from sklearn.preprocessing import StandardScaler
from generate_data import make_parameters
import numpy as np


def predict_user_situation(model, user_input_temperature, user_input_diameter, user_input_velocity):
    user_scaler = StandardScaler()
    unscaler = StandardScaler()
    user_density, user_specific_heat, user_dynamic_viscosity, user_thermal_conductivity = make_parameters([user_input_temperature])
    
    user_input_data = np.array([user_input_temperature, user_density, user_specific_heat, user_dynamic_viscosity, user_thermal_conductivity, user_input_diameter, user_input_velocity])
    user_input_scaled = user_scaler.fit_transform(user_input_data)
    user_input_tensor = torch.tensor(user_input_scaled, dtype=torch.float32)
## then make everything into a tensor

    model.eval()
    with torch.no_grad():
        prediction = model(user_input_tensor)
        unscaled_prediction = unscaler.inverse_transform(prediction)
        return unscaled_prediction

def ask_user_for_input_and_predict(model):
    user_input_temperature = float(input("Enter the temperature: "))
    user_input_diameter = float(input("Enter the diameter: "))
    user_input_velocity = float(input("Enter the velocity: "))
    prediction = predict_user_situation(model, user_input_temperature, user_input_diameter, user_input_velocity)
    print(f"The predicted H is {prediction[0][0]} W/m^2/K")
    return prediction