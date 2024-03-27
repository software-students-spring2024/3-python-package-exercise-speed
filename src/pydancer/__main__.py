import argparse
import sys
import pydancer.songs as songs
import pydancer.display as display
import pydancer.dancer as dancer
import pydancer.howto as howto

def main():
    parser = argparse.ArgumentParser(
        prog="pydancer",
        description="Rhythm Game on Python",
        epilog="Made by Speed"
    )
    subparsers = parser.add_subparsers(dest='command', help='sub-command help', required=True)

    playParser = subparsers.add_parser('play', help='play pydancer')
    playParser.add_argument('--difficulty', choices=['easy', 'medium', 'hard'], default='easy', help='choose difficulty level')
    playParser.add_argument('--character', choices=['boy', 'girl'], default='girl', help='choose character')

    displayParser = subparsers.add_parser('display', help='list display options')
    displayParser.add_argument('--characters', action="store_true", help='list only characters')
    displayParser.add_argument('--themes', action="store_true", help='list only themes')


    songsParser = subparsers.add_parser('songs', help='list available songs')
    songsParser.add_argument('--genre', choices=['country', 'pop'], help='genre name')

    howToParser = subparsers.add_parser('howto', help='print how-to guide')
    howToParser.add_argument('--long', action="store_true", help='print longer description')

    args = parser.parse_args()
    if args.command == 'play':
        dancer.play(args.difficulty, args.character)
    elif args.command == 'display':
        line = display.listDisplay(args)
        print(line)
    elif args.command == 'songs':
        line = songs.listSongs(args.genre)
        print(line)
    elif args.command == 'howto':
        line = howto.printHowTo(args.long)
        print(line)

if __name__ == "__main__":
    main()