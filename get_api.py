def get_api_key():
    l=""
    with open('secret.txt') as file:
        for line in file:
            l=str(line)
    return l