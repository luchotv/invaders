import sys
from invad.game import Game

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    app = Game()
    app.run()

if __name__ == '__main__':
    sys.exit(main())