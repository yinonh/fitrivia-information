class Screen:
    name = ''
    icon = ''

    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(*args, **kwargs)

    def build(self):
        pass