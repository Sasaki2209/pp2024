import gzip
import os

def compress_files():
    files_to_compress = ['students.txt', 'courses.txt', 'marks.txt']
    with gzip.open('students.dat', 'wb') as f_out:
        for file_name in files_to_compress:
            with open(file_name, 'rb') as f_in:
                f_out.write(f_in.read())

def decompress_files():
    if os.path.exists('students.dat'):
        with gzip.open('students.dat', 'rb') as f:
            data = f.read()
            with open('students.txt', 'wb') as f_out:
                f_out.write(data[:data.find(b'\n\n')+2])
            with open('courses.txt', 'wb') as f_out:
                f_out.write(data[data.find(b'\n\n')+2:data.rfind(b'\n\n')+2])
            with open('marks.txt', 'wb') as f_out:
                f_out.write(data[data.rfind(b'\n\n')+2:])

# Check if students.dat exists for decompression
decompress_files()

# Your program logic here

# Before closing the program, compress all files into students.dat
compress_files()