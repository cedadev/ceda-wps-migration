# -*- coding: utf-8 -*-

"""Console script for ceda_wps_migration."""

__author__ = """Ag Stephens"""
__contact__ = "ag.stephens@stfc.ac.uk"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
import argparse
import sys


def main():
    """Console script for ceda_wps_migration."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "ceda_wps_migration.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
