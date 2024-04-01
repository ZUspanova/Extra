import os

class CommandPrompt():
    def __init__(self):
        self.current_directory = os.path.abspath(os.getcwd())

    def pwd(self):
        print(f'Current directory: {self.current_directory}')

    def read_file(self, file):
        with open(self.current_directory+f'/{file}') as file_object:
            contents = file_object.read()
        print(contents)

    def ls(self):
        print('Files in the current directory:')
        for i in os.listdir():
            print(i)

    def cd(self, message):
        try:
            if message[3:5] == '..':
                os.chdir('..')
            else:
                os.chdir(self.current_directory + f'/{message[3:]}')
            self.__init__()
            self.pwd()
        except:
            print('Directory is not found')




command = CommandPrompt()

message = input()

while message != 'exit':
    if message[:4] == 'more':
        if message[5:] in os.listdir():
            command.read_file(message[5:])

    elif message == 'pwd':
        command.pwd()
    elif message == 'ls':
        command.ls()
    elif message[0:2] == 'cd':
        command.cd(message)


    message = input()
print('Exiting Command Prompt. GoodBye')

