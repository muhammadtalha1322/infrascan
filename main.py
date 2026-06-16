from core.engine import InfraEngine
from utils.banner import banner
import argparse


def main():
    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Target domain")
    args = parser.parse_args()

    if not args.target:
        print("Usage: python main.py -t example.com")
        return

    engine = InfraEngine(args.target)
    result = engine.run()

    print("\n[ FINAL REPORT ]")
    print(result)


if __name__ == "__main__":
    main()
