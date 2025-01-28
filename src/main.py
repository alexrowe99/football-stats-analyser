import football_data
from utils import print_pretty

def main():
	response = football_data.get_comp_standings(2021, {'date': '2025-01-01'})
	print_pretty(response)

if __name__ == "__main__":
	main()