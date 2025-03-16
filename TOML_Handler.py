import toml

class TOML_Handler:
    def __init__(self, path):
        self.config = None
        self.path = path

    def load(self):
        with open(self.path, 'r') as f:
            self.config = toml.load(self.path)
        return self.config

    def save(self):
        with open(self.path, 'w') as file:
            toml.dump(self.config, file)

if __name__ == '__main__':
    t = TOML_Handler('Sample_Files\\DummyData.toml')
    print(t.load())
    t.config['test']['username'] = 'Arindam'
    t.save()