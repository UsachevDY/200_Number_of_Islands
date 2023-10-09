from typing import List, Tuple


class Solution:

    def __find_next_island(self, grid: List[List[str]], visited: List[List[bool]], point_x: int) -> Tuple[int, int]:
        for row in range(point_x, len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == "1" and not visited[row][column]:
                    return row, column
        return -1, -1

    def __color(self, grid: List[List[str]], visited: List[List[bool]], point_x: int, point_y: int):
        queue = [(point_x, point_y)]
        while queue:
            x, y = queue.pop()
            visited[x][y] = True
            for next_x, next_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if -1 < next_x < len(grid) and -1 < next_y < len(grid[next_x]) and grid[next_x][next_y] == "1" and not \
                        visited[next_x][next_y]:
                    queue.append((next_x, next_y))

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = []
        for el in grid:
            visited.append([False] * len(el))

        finish = False
        x = 0
        while not finish:
            x, y = self.__find_next_island(grid, visited, x)
            if x == -1:
                finish = True
            else:
                count += 1
                self.__color(grid, visited, x, y)
        return count
