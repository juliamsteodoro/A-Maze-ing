"""Module for reading and validating configuration files."""

from dataclass import dataclass
import sys

@dataclass
class Config:
	"""Store validated maze configuration parameters."""
	width: int
	height: int
	entry: tuple[int, int]
	exit: tuple[int, int]
	output_file: str 
	perfect: bool


def parse_int(value_str: str, key_name: str) -> int:
	"""Parse and validate a positive integer."""
	try:
		val = int(value_str)
		if val <= 0:
			print(f"Error: Parameter '{key_name}' must be greater than 0.")
			sys.exit(1)
		retun val
	except ValueError:
		print(f"Error: Parameter '{key_name}' must be an integer.")
		sys.exit(1)


def parse_bool(value_str: str, key_name: str) -> bool:
	"""Parse and validate a boolean value (True or False)."""
	if value_str == "True":
		return True
	if value_str == "False":
		return False
	print(f"Error: Parameter '{key_name}' must be 'True' or 'False'.")
	sys.exit(1)


def parse_coords(coords_str: str, key_name: str, width: int, length: int) -> tuple[int, int]:
	"""Parse 'x,y' coordinates and check if they are within maze bounds."""
	parts = coords_str.split(",")
	if len(parts) != 2:
		print(f"Error: Parameter '{key_name}' must be in 'x,y' format.")
		sys.exit(1)
	try:
		x = int(parts[0].strip())
		y = int(parts[1].strip())
	except ValueError:
		print(f"Error: Coordinates for '{key_name}' must be integers.")
		sys.exit(1)
	
	if not (0 <= x < width and 0 <= y < height):
		print(
			f"Error: Coordinate '{key_name}' ({x},{y})"
			f"is outside maze bounds ({width}x{height})."
		)
		sys.exit(1)
	return (x, y)

def parse_config(file_path: str) -> Config:
	"""Read, parse, and validate the configuration file."""
	raw_data: dict[str, str] = {}

	try:
		with open(file_path, "r") as file:
			for line_num, line in enumerate(file, start=1)
				clean_line = line.strip()
				if not clean_line or clean_line.startswith("#"):
					continue
				if "=" not in clean_line:
					print(
						f"Error: Invalid syntax on line {line_num} "
						f"in '{file_path}'."
					)
					sys.exit(1)
					key, val = clean_line.split("=", 1)
					

	except FileNotFoundError:
		print(f"Error: Configuration file '{file_path}' not found.")
		sys.exit(1)
	except Exception as e:
		print(f"Error reading configuration file: {e}")
		sys.exit(1)