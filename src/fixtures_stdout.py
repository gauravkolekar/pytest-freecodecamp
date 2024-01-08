import sys

def hello(name: str) -> None:
    print(f"Hello Hello {name}")

if __name__ == "__main__":
    exit(hello(sys.argv[1]))