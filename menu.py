class Menu:
    def __init__(self):
        self.text_descriptions = {}

    def add_option(self, key, description, keyFunction):
        self.text_descriptions[key] = description
        self.functions[key] = keyFunction

    def __str__(self):
        texts = [f'{key}: {self.text_descriptions[key]}' for key in self.text_descriptions.keys()]
        return '\n'.join(texts)