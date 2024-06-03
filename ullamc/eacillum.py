def generate_content_range(start, end, total):
    return f'Content-Range: bytes {start}-{end}/{total}'

# Example usage:
header = generate_content_range(0, 999, 5000)
print(header)
