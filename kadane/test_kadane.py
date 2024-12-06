from kanane import kadane


def test_kadane():
    # Test 1: General case with positive and negative numbers
    assert kadane([-3, 2, 3, -4, -5]) == 5  # Maximum subarray is [2, 3]

    # Test 2: All negative numbers  # Maximum subarray is [-2]
    assert kadane([-8, -3, -6, -2, -5, -4]) == -2

    # Test 3: All positive numbers  # Maximum subarray is [1, 2, 3, 4, 5]
    assert kadane([1, 2, 3, 4, 5]) == 15

    # Test 4: Mixed numbers with the largest sum at the end
    # Maximum subarray is [4, -1, 2, 1]
    assert kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test 5: Single element array (positive)  # Maximum subarray is [7]
    assert kadane([7]) == 7

    # Test 6: Single element array (negative)  # Maximum subarray is [-7]
    assert kadane([-7]) == -7

    # Test 7: Large input array with a mix of values
    # Maximum subarray is [3, -1, 6, -3, 2, 7, -5, 3]
    assert kadane([3, -2, 5, -1, 6, -3, 2, 7, -5, 3]) == 17

    # Test 8: Subarray in the middle
    # Maximum subarray is [6, -2, 4]
    assert kadane([-1, -2, 6, -2, 4, -1, -2, -3]) == 8

    # Test 9: Edge case with empty array
    # (should raise an error or handle gracefully)
    try:
        kadane([])
        assert False, "Should raise an exception for empty input"
    except IndexError:
        pass  # Expected behavior

    print("All tests passed!")


test_kadane()

