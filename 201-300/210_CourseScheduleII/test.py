from solution import Solution


def main():
    cases = [
        (2, [[1, 0]]),
        (3, [[0,1],[0,2],[1,2]]),
    ]
    for numCourses, prerequisites in cases:
        print("Input: ", numCourses, prerequisites)
        print("Output: ", Solution().findOrder(numCourses, prerequisites))


if __name__ == '__main__':
    main()
