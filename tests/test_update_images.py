"""Test image updates from remote cloud APIs."""
from __future__ import annotations

from unittest.mock import MagicMock
from unittest.mock import patch

from src.rhelocator import update_images


def test_get_aws_regions() -> None:
    """Test AWS region request."""
    with patch("botocore.client.BaseClient._make_api_call") as boto:
        update_images.get_aws_regions()

    boto.assert_called_with("DescribeRegions", {"AllRegions": "True"})


def test_get_aws_cloud_access_images() -> None:
    """Test AWS image request."""
    with patch("botocore.client.BaseClient._make_api_call") as boto:
        update_images.get_aws_cloud_access_images("us-east-1")

    boto.assert_called_with(
        "DescribeImages", {"IncludeDeprecated": "False", "Owners": ["309956199498"]}
    )


@patch("rhelocator.update_images.requests.post")
def test_get_azure_access_token(mock_requests: MagicMock) -> None:
    """Test retrieving Azure locations."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"foo": "bar", "access_token": "secrete"}
    mock_requests.return_value = mock_response

    access_token = update_images.get_azure_access_token()
    assert access_token == "secrete"  # nosec B105


@patch("rhelocator.update_images.requests.get")
def test_get_azure_locations(mock_requests: MagicMock) -> None:
    """Test getting Azure location list."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "value": [
            {
                "id": "/subscriptions/id/locations/eastus",
                "name": "eastus",
                "displayName": "East US",
                "regionalDisplayName": "(US) East US",
                "metadata": {
                    "regionType": "Physical",
                    "regionCategory": "Recommended",
                    "geographyGroup": "US",
                    "longitude": "-79.8164",
                    "latitude": "37.3719",
                    "physicalLocation": "Virginia",
                    "pairedRegion": [
                        {
                            "name": "westus",
                            "id": "/subscriptions/id/locations/westus",
                        }
                    ],
                },
            },
        ]
    }
    mock_requests.return_value = mock_response

    regions = update_images.get_azure_locations("secrete")
    assert regions == ["eastus"]
