def format_data(data):
    # Function to format data for the neural network
    formatted_data = []
    for item in data:
        formatted_data.append({
            'feature1': item['feature1'],
            'feature2': item['feature2'],
            'feature3': item['feature3'],
            'feature4': item['feature4']
        })
    return formatted_data

def log_message(message):
    # Function to log messages
    with open('app.log', 'a') as log_file:
        log_file.write(f"{message}\n")