import sys

def process_args():
    args = sys.argv[1:]
    if not args:
        return "No arguments provided"
    return f"Arguments: {args}"

print(process_args())