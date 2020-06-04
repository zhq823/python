def get(data = []):
    if 'list' in str(type(data)):
        return [[row[index] for row in data] for index in range(len(data[0]))]
    else:
        return data