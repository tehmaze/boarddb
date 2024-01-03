#!/usr/bin/env python3

import json
import sys
from jsonschema import validate


def load_schema(name: str) -> dict:
    with open(name, 'r') as fd:
        return json.load(fd)


def validate_against_schema(name: str, schema: dict):
    with open(name, 'r') as fd:
        definition = json.load(fd)
        validate(instance=definition, schema=schema)


def run() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('schema')
    parser.add_argument('definition')

    args = parser.parse_args()
    schema = load_schema(args.schema)
    validate_against_schema(args.definition, schema=schema)

    return 0


if __name__ == '__main__':
    sys.exit(run())