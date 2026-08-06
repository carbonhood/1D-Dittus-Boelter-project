from generate_data import create_synthetic_dataset

if __name__ == "__main__":
    Create_data = input("Do you want to create a new dataset? (y/n)")
    if Create_data == "y":
        create_synthetic_dataset()
    else:
        print("Using existing dataset")
        pass
