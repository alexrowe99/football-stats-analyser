import json

# print dictionary as json with formatting
def print_pretty(dictionary):
	print(json.dumps(dictionary, indent=4))

def filter_dict2str(filters):
	if not filters:
		return ""
	result = ""
	for key, value in filters.items():
		if isinstance(value, list):
			result += f"{key}={','.join(map(str, value))}&"
		else:
			result += f"{key}={value}&"
	return result