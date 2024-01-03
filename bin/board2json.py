#!/usr/bin/env python3

import json
import sys
import yaml


def convert(dst, src):
    '''Convert a YAML file to JSON.'''

    with open(src, 'r') as fd:
        definition = yaml.safe_load(fd)

    with open(dst, 'w') as fd:
        json.dump(definition, fd, indent=4)
        fd.write('\n')


def run():
    '''Run the converter as a CLI command.'''

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('destination')
    args = parser.parse_args()
    return convert(args.destination, args.source)


if __name__ == '__main__':
    sys.exit(run())