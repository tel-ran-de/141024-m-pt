def process_data(data):
    def filter_data(data):
        return [item for item in data if item > 0]

    def transform_data(data):
        return [item * 2 for item in data]

    filtered_data = filter_data(data)
    transformed_data = transform_data(filtered_data)
    return transformed_data


data = [-1, 2, -3, 4, 5]
result = process_data(data)
print(result)
