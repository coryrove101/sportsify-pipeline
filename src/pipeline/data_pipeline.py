from src.api.sportsify_client import fetch_sports_data
from src.db.postgres_client import insert_data, retrieve_data
from src.model.neural_network import NeuralNetwork

def run_data_pipeline():
    # Step 1: Fetch data from Sportsify API
    sports_data = fetch_sports_data()
    
    # Step 2: Store data in PostgreSQL database
    insert_data(sports_data)
    
    # Step 3: Retrieve data from the database for processing
    data_for_model = retrieve_data()
    
    # Step 4: Initialize and train the neural network
    model = NeuralNetwork()
    model.train(data_for_model)
    
    # Step 5: Make predictions using the trained model
    predictions = model.predict(data_for_model)
    
    return predictions

if __name__ == "__main__":
    results = run_data_pipeline()
    print(results)