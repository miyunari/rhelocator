"""Test all endpoint."""
import os


def test_all():
    """Run transformer end to end and generate a list with all image
    details."""

    assert 0 == os.system(
        "poetry run cloudimagedirectory-transformer -f "
        "${PWD}/tests/transformer/testdata/input/raw/azure/eastus.json,"
        "${PWD}/tests/transformer/testdata/input/raw/google/all.json,"
        "${PWD}/tests/transformer/testdata/input/raw/aws/af-south-1.json"
        " -op=${PWD} -dp=${PWD}/tests/transformer/testdata"
        " --filter.until=none"
    )
    assert 0 == os.system(
        "diff ${PWD}/tests/transformer/testdata/expected/v2/all"
        " ${PWD}/tests/transformer/testdata/v2/all"
    )
