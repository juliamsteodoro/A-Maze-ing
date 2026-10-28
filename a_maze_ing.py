"""Main entry point for A-Maze-ing."""
import sys

def main() -> None:
	if len(sys.argv) < 2:
		print("Usage: python3 a_maze_ing.py <config.txt>")
		sys.exit(1)

	config_file = sys.argv[1] #config.txt
	print(f"Reading configuration file: {config_file}")


if __name__ == "__main__": 
	main()