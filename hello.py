#!/usr/bin/env python3
"""A simple greeting module with enhanced functionality."""

import argparse
import datetime


def hello(name: str = "World") -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def get_time_greeting() -> str:
    """Return a greeting based on the current time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def greet(name: str = "World") -> str:
    """Return a time-aware greeting message."""
    return f"{get_time_greeting()}, {name}!"


def main() -> None:
    """Main entry point with CLI argument support."""
    parser = argparse.ArgumentParser(description="Greeting utility")
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="Name to greet (default: World)",
    )
    parser.add_argument(
        "--time-aware",
        action="store_true",
        help="Use time-aware greeting",
    )
    args = parser.parse_args()

    if args.time_aware:
        print(greet(args.name))
    else:
        print(hello(args.name))


if __name__ == "__main__":
    main()
