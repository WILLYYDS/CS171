# Minesweeper AI Project

## Team Information
- **Members:**
  - Jiayun Wang (UCI NetID: jiayunw4)
  - Shuang Wu (UCI NetID: shuaw18)

## Project Overview
This project implements an AI agent to solve the Minesweeper game efficiently. It consists of two versions: a **Minimal AI** and a **Final AI**, each improving upon the previous version in terms of strategy and performance.

## 1. Minimal AI

### Algorithm Description
The Minimal AI follows a simple strategy based on the number of uncovered tiles:
- If an uncovered tile has a value of `0`, all its neighboring tiles are added to a `toVisit` set.
- If an uncovered tile has a value of `1`, it analyzes its neighbors:
  - If the number of flagged mines equals the tile value, all remaining covered neighbors are safe and added to `toVisit`.
  - If only one covered neighbor remains, it is flagged as a mine.
- The AI continues processing tiles from the `toVisit` set until empty.
- If no further moves are possible, the game is terminated.

### Performance
| Board Size | Sample Size | Score | Worlds Completed |
|------------|-------------|-------|-----------------|
| 5x5        | 20          | 12    | 12              |
| 8x8        | 100         | 0     | 0               |
| 16x16      | 100         | 0     | 0               |
| 16x30      | 100         | 0     | 0               |
| **Total**  | 320         | 12    | 12              |

## 2. Final AI

### Algorithm Enhancements
The Final AI introduces **backtracking search** to improve decision-making:
1. It maintains a `safe_moves` set, storing tiles that are known to be safe.
2. Each move checks the last uncovered tile's value and updates the `safe_moves` set accordingly.
3. If `safe_moves` is not empty, a tile is popped and uncovered.
4. If `safe_moves` is empty, a **backtracking search** is initiated:
   - Selects frontier tiles (tiles adjacent to revealed numbers).
   - Assigns each frontier tile a value of `0` (safe) or `1` (mine) and checks constraints.
   - Uses constraint propagation to ensure valid assignments.
   - Computes probability estimates for mines and flags certain mines.
   - If no safe moves are found, it uncovers the tile with the lowest probability of being a mine.
5. The process continues until all tiles (except mines) are uncovered.

### Performance
| Board Size | Sample Size | Score | Worlds Completed |
|------------|-------------|-------|-----------------|
| 5x5        | 20          | 20    | 20              |
| 8x8        | 100         | 100   | 100             |
| 16x16      | 200         | 322   | 161             |
| 16x30      | 200         | 300   | 100             |
| **Total**  | 520         | 742   | 381             |

## 3. Performance Improvements & Future Work
The major bottleneck in this implementation is the **backtracking search**. Possible optimizations include:
- **Least Constraining Value (LCV):** Selecting tiles in a way that maximizes future options.
- **Forward Checking:** Preventing moves that lead to immediate failure.
- **Parallel Processing:** Running the backtracking algorithm across multiple threads to significantly reduce computation time.

## 4. How to Run the AI
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd minesweeper-ai
