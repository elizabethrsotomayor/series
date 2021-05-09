from typing import List


def slices(series: str, length: int) -> List[str]:
    """Return a list of contiguous digits in a string of digits based on the length provided."""
    nums = []
    count = 0
    if len(series) >= length > 0:
        for num in range(0, len(series)):
            if len(series[num:length+count]) == length:
                nums.append(series[num:length+count])
                count += 1
            else:
                break
    else:
        raise ValueError("Invalid input, try again.")

    return nums
