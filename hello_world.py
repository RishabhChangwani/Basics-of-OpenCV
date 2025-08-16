#!/usr/bin/env python3

"""
A simple script to print 'Hello, World!'.

This script serves as a basic example of a Python program.
"""


def main() -> None:
    """
    Main function to print 'Hello, World!'.

    Raises:
        Exception: If an unexpected error occurs.
    """
    try:
        print("Hello, World!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
