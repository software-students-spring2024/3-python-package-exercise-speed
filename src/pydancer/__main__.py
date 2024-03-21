import argparse
import pydancer.songs as songs
# import pydancer.dancer as dancer
# use this as reference for argument parser: https://github.com/grantjenks/free-python-games/blob/master/src/freegames/__main__.py

def main():
    parser = argparse.ArgumentParser(
        prog="pydancer",
        description="Rhythm Game on Python",
        epilog="Made by Speed"
    )
    subparsers = parser.add_subparsers(dest='command', help='sub-command help', required=True)

    songsParser = subparsers.add_parser('songs', help='list available songs')
    songsParser.add_argument('--genre', choices=['country', 'pop'], help='genre name')

    args = parser.parse_args()
    if args.command == 'songs':
        songs.listSongs(args.genre)



if __name__ == "__main__":
    main()