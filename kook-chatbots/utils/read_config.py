'''
make sure that a config.json file is located under root of the project
'''
import json
from definitions import get_project_root

ROOT_DIR = get_project_root()
def read_config():
     config_file = ROOT_DIR / 'config.json'
     if not config_file.exists():
          raise IOError("config.json does not exit")
     with open(config_file, 'r', encoding='UTF-8') as f:
          config = json.load(f)['tokens']
          ret = {}

          for i in config:
               index = i.find(':')
               botName = i[:index]
               token = i[index+1:]
               ret[botName] = token

          return ret


if __name__ == '__main__':
    print(read_config())