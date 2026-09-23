#!/usr/bin/env python3
"""
Lab: Debugging with logging.

Goal: summarize sensor records and compute average over valid entries.
The script runs but average is wrong due to a counting bug. Logging is
intended to make the issue visible quickly.
"""

# Review observations (compute_average_valid):
# - records is supposed to be a list,
# if we send him none or an int the program crash with a TypeError
# - each records is supposed to be a dictionnary
# if an element of the list is None or an str, the program crash too.
# - valid_value_sum / valid_count can't happen if 0
# if the list is empty, valid_count would be equal to 0, the program will crash (ZeroDivisionError)
# - Nothing checks if the value isn't too high or negative
#
# Fix:
# - Checking if record is a dictionnary in is_valid_record()
# - Adding validation for records type (check if None or not list/tuple) in compute_average_valid()
# - Skipping non-dictionnary elements inside the loop with a warning
# - Adding a check for valid_count == 0 to return 0.0 and avoid ZeroDivisionError


import logging


def configure_logging(level=logging.INFO):
    """Configure basic logging for this script."""
    logging.basicConfig(level=level, format="%(levelname)s:%(message)s")


def is_valid_record(record):
    """Return True when record has non-empty id and numeric value."""
    if not isinstance(record, dict):
        return False

    sensor_id = record.get("sensor_id")
    value = record.get("value")

    is_id_ok = isinstance(sensor_id, str) and bool(sensor_id.strip())
    is_value_ok = isinstance(value, (int, float)) and not isinstance(value, bool)
    return is_id_ok and is_value_ok


def compute_average_valid(records):
    """Return average value considering only valid records."""
    # Fix 1: Valider le paramètre d'entrée 'records'
    if records is None:
        raise ValueError("records argument cannot be None")

    if not isinstance(records, (list, tuple)):
        raise TypeError(f"expected list or tuple, got {type(records).__name__}")

    valid_value_sum = 0.0
    valid_count = 0

    for record in records:
        if not isinstance(record, dict):
            logging.warning("ignored non-dict item in records: %r", record)
            continue

        sensor_id = record.get("sensor_id")
        value = record.get("value")
        logging.debug("processing record sensor_id=%r value=%r", sensor_id, value)

        if is_valid_record(record):
            valid_value_sum += value
            valid_count += 1
            logging.info("accepted sensor_id=%s value=%s", sensor_id, value)
        else:
            logging.warning("ignored invalid record sensor_id=%r value=%r", sensor_id, value)

    if valid_count == 0:
        logging.warning("no valid records found to compute average")
        return 0.0

    avg = round(valid_value_sum / valid_count, 2)
    logging.info(
        "final valid_value_sum=%s valid_count=%s average=%s",
        valid_value_sum,
        valid_count,
        avg,
    )
    return avg


def main():
    configure_logging(logging.INFO)
    records = [
        {"sensor_id": "A-1", "value": 10.0},
        {"sensor_id": "A-2", "value": 20.0},
        {"sensor_id": "", "value": 50.0},
        {"sensor_id": "A-3", "value": 30.0},
    ]
    average = compute_average_valid(records)
    print("Average valid value:", average)


if __name__ == "__main__":
    main()
