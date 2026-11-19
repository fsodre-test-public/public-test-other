"""A simple command-line greeter."""

import argparse


def greet(name: str) -> str:
    return f"Hello, {name}!"


def greet_many(name: str, times: int) -> list[str]:
    """Return the greeting repeated `times` times."""
    return [greet(name) for _ in range(times)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    parser.add_argument("-n", "--times", type=int, default=1, help="Repeat count")
    args = parser.parse_args()
    for line in greet_many(args.name, args.times):
        print(line)


if __name__ == "__main__":
    main()
