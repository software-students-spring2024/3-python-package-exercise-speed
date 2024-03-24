import argparse
import pydancer.songs as songs
import pydancer.display as display
import pydancer.dancer as dancer
import pydancer.howto as howto
# using this as reference for argument parser: https://github.com/grantjenks/free-python-games/blob/master/src/freegames/__main__.py

def main():
    
    parser = argparse.ArgumentParser(
        prog="pydancer",
        description="Rhythm Game on Python",
        epilog="Made by Speed"
    )
    subparsers = parser.add_subparsers(dest='command', help='sub-command help', required=True)

    playParser = subparsers.add_parser('play', help='play pydancer')

    displayParser = subparsers.add_parser('display', help='list display options')
    displayParser.add_argument('--characters', action="store_true", help='list only characters')
    displayParser.add_argument('--themes', action="store_true", help='list only themes')


    songsParser = subparsers.add_parser('songs', help='list available songs')
    songsParser.add_argument('--genre', choices=['country', 'pop'], help='genre name')

    howToParser = subparsers.add_parser('howto', help='print how-to guide')
    howToParser.add_argument('--long', action="store_true", help='print longer description')

    args = parser.parse_args()
    if args.command == 'play':
        dancer.play()
    elif args.command == 'display':
        display.listDisplay(args)
    elif args.command == 'songs':
        songs.listSongs(args.genre)
    elif args.command == 'howto':
        howto.printHowTo(args.long)



if __name__ == "__main__":
    main()