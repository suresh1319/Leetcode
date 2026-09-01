from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])

        dq = deque()

        # Give every litter cell an ID
        litter_id = {}
        total_litter = 0

        start_r = start_c = 0

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'L':
                    litter_id[(r, c)] = total_litter
                    total_litter += 1

                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

        # mask = which litter cells have been collected
        start_mask = 0

        # State:
        # (row, col, remaining_energy, mask)
        dq.append((start_r, start_c, energy, start_mask))

        # visited[row][col][energy][mask]
        visited = set()
        visited.add((start_r, start_c, energy, start_mask))

        directions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while dq:
            size = len(dq)

            for _ in range(size):
                row, col, e, mask = dq.popleft()

                # All litter collected
                if mask == (1 << total_litter) - 1:
                    return moves

                # Cannot move without energy
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    # Check boundaries
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    # Cannot pass obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Moving costs 1 energy
                    new_energy = e - 1
                    new_mask = mask

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        new_mask |= (1 << idx)

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        dq.append(state)

            moves += 1

        return -1