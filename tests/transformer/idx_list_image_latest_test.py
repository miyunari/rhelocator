"""Tests for transforming the images by name."""
import filecmp
import os

from cloudimagedirectory import transformer


def test_list_names_of_images(runner, tmp_path):
    """Run transformer end to end and generate a small list that contains image
    names."""
    result = runner.invoke(
        transformer.run,
        [
            "-f",
            (
                "tests/transformer/testdata/input/raw/google/all.json,"
                "tests/transformer/testdata/input/raw/aws/af-south-1.json,"
                "tests/transformer/testdata/input/raw/azure/eastus.json"
            ),
            "-op=.",
            f"-dp={tmp_path}",
            "--filter.until=none",
        ],
    )

    if "0" != f"{result.exit_code}":
        assert (
            ""
            == f"expected no error, but got code: {result.exit_code} and output:"
            f" {result.output}"
        )

    # Get current directory
    pwd = os.getcwd()

    # Check image data by comparing the expected file and the output file byte by byte.
    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date/0",
        f"{tmp_path}/v1/idx/list/sort-by-date/0",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date-aws/0",
        f"{tmp_path}/v1/idx/list/sort-by-date-aws/0",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date-google/0",
        f"{tmp_path}/v1/idx/list/sort-by-date-google/0",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date-azure/0",
        f"{tmp_path}/v1/idx/list/sort-by-date-azure/0",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date/pages",
        f"{tmp_path}/v1/idx/list/sort-by-date/pages",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date-aws/pages",
        f"{tmp_path}/v1/idx/list/sort-by-date-aws/pages",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date-azure/pages",
        f"{tmp_path}/v1/idx/list/sort-by-date-azure/pages",
    )

    assert filecmp.cmp(
        f"{pwd}/tests/transformer/testdata/expected/v1/idx/list/sort-by-date-google/pages",
        f"{tmp_path}/v1/idx/list/sort-by-date-google/pages",
    )
