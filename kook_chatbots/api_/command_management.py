class CommandManager:
    def __init__(self):
        self.commands = {

        }
        self.register_command('help',self.print_help,description='列出所有机器人可用的命令')

    def register_command(self, command: str, func: callable,description: str ,allow_args=False):
        self.commands[command] = func, allow_args,description

    def print_help(self):
        ret = 'Allowed commands for the chatbots:\r\n'
        for command in self.commands.keys():
            ret += f'\\{command}'
            if self.commands[command][1]:
                ret +=f' <args>'
            else:
                ret +=f'       '
            ret+= f'\t\t\t{self.commands[command][2]}'
            ret += '\r\n'
        print(ret)
        return ret

    def has_command(self,command):
        return command in self.commands.keys()

    def exec_command(self,command,**kwargs):
        if self.has_command(command):
            return str(self.commands[command][0](**kwargs))
        else:
            return None

    def parse_command_and_exec(self,text:str):
        '''
        A text template: /help --arg1 10 --arg2 20 --arg3
        :param text:
        :return: command and its args
        '''

        tokens = text.split(' ')
        command = tokens[0][1:]
        kwargs = {}

        for i in range(1,len(tokens)):
            token = tokens[i]
            if token.startswith('--'):
                arg = token[2:]
                kwargs[arg] = True
            else:
                arg = tokens[i-1][2:]
                kwargs[arg] = token

        self.exec_command(command,**kwargs)

if __name__ == '__main__':
    manager = CommandManager()
    manager.register_command('hello',print,'test',True)
    manager.exec_command('help')
    manager.parse_command_and_exec('/help2 --info 10 --verbose')
