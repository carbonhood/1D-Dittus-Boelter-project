## here we need to unscale the numbers from the prediction to get the actual values

## then we will print with units

## this will be an input parameters ----> recieve a predicted H, the final part of the project

## then it will loop over again and ask if wanting to make more predictions

## start with a function that will take in user made inputs for temperature, diameter, and velocity and return the predicted H

## then we will unscale the prediction from the model and print with units

import torch
from generate_data import make_parameters
import numpy as np


def user_prediction(
    model,
    user_input_temperature,
    user_input_diameter,
    user_input_velocity,
    feature_scaler,
    target_scaler,
):
    user_density, user_specific_heat, user_dynamic_viscosity, user_thermal_conductivity = make_parameters(
        [user_input_temperature]
    )
    ##define the units and make into a numpy array
    #came across an error here where the array was not the correct shape, I think we need to do column.stack(), as it is the same as in generate_data.py
    user_input_data = np.column_stack(
        [
            user_input_temperature,
            user_density,
            user_specific_heat,
            user_dynamic_viscosity,
            user_thermal_conductivity,
            user_input_diameter,
            user_input_velocity,
        ]
    )
    # Must use the same fitted scalers from training — not new StandardScalers
    user_input_scaled = feature_scaler.transform(user_input_data)
    user_input_tensor = torch.tensor(user_input_scaled, dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        scaled_prediction = model(user_input_tensor)
        unscaled_user_prediction = target_scaler.inverse_transform(
            scaled_prediction.numpy()
        )
        return unscaled_user_prediction


def ask_user_for_input_and_predict(model, feature_scaler, target_scaler):
    user_input_temperature = float(input("Enter the temperature (in degrees Kelvin): "))
    user_input_diameter = float(input("Enter the diameter (in meters): "))
    user_input_velocity = float(input("Enter the velocity (in meters per second): "))
    prediction = user_prediction(
        model,
        user_input_temperature,
        user_input_diameter,
        user_input_velocity,
        feature_scaler,
        target_scaler,
    )
    print(f"The predicted H is {prediction[0][0]} W/m^2/K")
