class Parser:

    def __init__(self):
        self.tokens = []

    def parse(self, file_content):
        for line in file_content.splitlines():
            if not line:
                continue

            self.parse_line(line)

        self.parse_tokens()

    def parse_line(self, line):
        if line.startswith('#'):
            return

        if ' ' not in line:
            self.tokens.append(line)
            return

        line_part = line.split(' ')
        instruction = line_part[0]
        self.tokens.append(instruction)

        for part in line_part[1:]:
            if part.startswith('#'):
                break

            if not part:
                continue

            self.tokens.append(part)

    def parse_tokens(self):
        print(self.tokens)
