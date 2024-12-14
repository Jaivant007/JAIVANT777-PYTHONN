def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        max_area = max(max_area, height * width)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(max_area([1, 5, 4, 3]))
print(max_area([3, 1, 2, 4, 5]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
print(max_area([7, 3]))
