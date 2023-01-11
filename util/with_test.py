class WithTestClass():
    def __init__(self):
        self.name = 'withName'
        print('init')

    def __enter__(self):
        print('enter')
        return 'enter'

    def __exit__(self, *args):
        print('exit')
