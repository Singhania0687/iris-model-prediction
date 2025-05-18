import pickle

# Load model from file
with open("iris_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

