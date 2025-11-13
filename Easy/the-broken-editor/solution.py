# Written by Joseph Garcia

class Editor:

    def __init__(self, typed_keys):
        self.typed_keys = typed_keys
        self.pos = 0
        self.result = list()
        self.load()

    def load(self):
        for key in self.typed_keys:
            if not key in "<>-":
                self.result.insert(self.pos, key)
                self.pos += 1
            else:
                if key == '<': self.pos -= 1
                elif key == '>': self.pos += 1
                elif key == '-':
                    if self.pos != 0:
                        self.result.pop(self.pos - 1)
                        self.pos -= 1

            self.normalize_pos()

        self.result = "".join(self.result)
        print(self.result)

    def normalize_pos(self) -> None:
        if self.pos < 0: 
            self.pos = 0

        elif self.pos > len(self.result):
            self.pos = len(self.result)

typed_keys = input()
editor = Editor(typed_keys)
