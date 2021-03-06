#!/usr/bin/env python

"""
Script that takes csv on stdin with a publishable column
and outputs the header row and all rows with publishable
= "Y". Columns publishable, record_created, record_modified
and user_modified are removed from output.
"""

import csv
import sys

FILTER_COLUMN = "publishable"
REMOVE_COLUMNS = [
    'publishable',
    'public_opinion_research',
    'contact_email',
    'policy_program_lead_email',
    'remarks_en',
    'remarks_fr',
    'record_created',
    'record_modified',
    'user_modified',
]

def main():
    reader = csv.DictReader(sys.stdin)
    outnames = [f for f in reader.fieldnames if f not in REMOVE_COLUMNS]
    writer = csv.DictWriter(sys.stdout, outnames)
    writer.writeheader()
    for row in reader:
        try:
            if row[FILTER_COLUMN] == 'Y':
                for rem in REMOVE_COLUMNS:
                    del row[rem]
                writer.writerow(row)
        except ValueError:
            pass

main()
