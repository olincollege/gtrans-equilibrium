"""
Test library functions to find and identify the equilibrium steps
"""
import pytest
from translate import find_max_equilibrium


################################################################################
# It should be noted that all other functions scrapes data from google translate
# and would therefore take toll on the maximum amount of retries for a certain
# ip address to translate. This means that Google detects frequent access and
# would block handshakes should the request overreaches the maximum limit.
################################################################################


# Define test cases
find_max_equilibrium_cases = [
    # Test for single equilibrium case
    ({"en": 2},("en", 2)),
    # Test for double equilibrium case
    ({"zh-TW": 5, "ko": 2}, ("zh-TW", 5)),
    # Test for two maximums, where the first occurrance will be taken
    ({"zh-CN": 1, "de": 2, "ja": 2}, ("de", 2))
]


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("equilibriums,maximum", find_max_equilibrium_cases)
def test_find_max_equilibrium(equilibriums, maximum):
    """
    Test that the correct maximum equilibrium is found.

    Given a man-made dictionary of equilibriums, test for the maximum step and
    see if it is returned correctly.

    Args:
        equilibriums: A dictionary of languages directed to their respective
            steps.
        maximum: An int that represents the largest amount of steps within the
            dictionary.
    """
    assert find_max_equilibrium(equilibriums) == maximum
