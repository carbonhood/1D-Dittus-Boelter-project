from generate_data import create_synthetic_dataset
from create_model import create_model, load_model, prepare_data
from train_model import train_model
from test_model import test_multiple_times
from clean_up_prediction import ask_user_for_input_and_predict
import sys


if __name__ == "__main__":
    Create_data = input("Do you want to create a new dataset? (y/n)")
    if Create_data == "y":
        create_synthetic_dataset()
    else:
        print("Using existing dataset")
        


    Create_model = input("Do you want to create a new model? (y/n)")
    if Create_model == "y":
        model, checkpoint = create_model()    
    else:
        print("Using existing model")
        model, checkpoint = load_model()
        
    feature_scaler = None
    target_scaler = None
    if checkpoint is not None:
        feature_scaler = checkpoint.get("feature_scaler")
        target_scaler = checkpoint.get("target_scaler")
    
    while True:
        Train_model = input("Do you want to train the model? (y/n)")
        if Train_model == "y":
            (
                features_train_tensor,
                target_train_tensor,
                features_test_tensor,
                target_test_tensor,
                feature_scaler,
                target_scaler,
            ) = prepare_data()
            train_model(
                model,
                features_train_tensor,
                target_train_tensor,
                checkpoint,
                feature_scaler,
                target_scaler,
            )
            model, checkpoint = load_model()
            feature_scaler = checkpoint.get("feature_scaler")
            target_scaler = checkpoint.get("target_scaler")
        elif Train_model == "n":
            print("Skipping training")
            break

    Test_model = input("Do you want to test the model? (y/n)")
    if Test_model == "y":
        (
            _,
            _,
            features_test_tensor,
            target_test_tensor,
            feature_scaler,
            target_scaler,
        ) = prepare_data()
        test_multiple_times(model, features_test_tensor, target_test_tensor)

    elif Test_model == "n":
        print("Skipping testing")

    User_ask = input("Do you want to ask the model a question? (y/n)")
    if User_ask == "y":
        if feature_scaler is None or target_scaler is None:
            (
                _,
                _,
                _,
                _,
                feature_scaler,
                target_scaler,
            ) = prepare_data()
        ask_user_for_input_and_predict(model, feature_scaler, target_scaler)
    elif User_ask == "n":
        print("Closing Program")
        sys.exit()


    ## Then add another input to test the model against the test data
