from utils.read_config import read_config

if __name__ == '__main__':
    testBot_token = read_config()['testBot']
    xiaoxin = read_config()['xiaoxin']
    print(testBot_token)
    print(xiaoxin)