import gzip
import os

def compress_file(file_path):
    # Open the input file for reading
    with open(file_path, 'rb') as input_file:
        # Create a new file with a .gz extension and open it for writing
        with gzip.open(file_path + '.gz', 'wb') as output_file:
            # Write the compressed data to the output file
            output_file.write(input_file.read())
    
    # Calculate the Weissman Score
    original_size = os.path.getsize(file_path)
    compressed_size = os.path.getsize(file_path + '.gz')
    weissman_score = compressed_size / original_size
    
    print(f"File {file_path} compressed successfully with Weissman Score: {weissman_score:.2f}")

# Example usage: compress the file 'example.txt'
compress_file('example.txt')
