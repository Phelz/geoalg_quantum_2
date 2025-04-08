import os
import subprocess
import re
from multiprocessing import Pool, cpu_count

NUM_CORES=8

# Files starting with any of these will be skipped
# exc_list = ['s18']  # Add more as needed
# exc_list = ['s09', 's10', 's11', 's12', 's13', 's14', 's15', 's16']
# exc_list = ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08', 's09',]
exc_list = ['s20']

# Pattern to match files like s01_..., s02_..., etc.
pattern = re.compile(r'^(s\d{2}).*\.py$')

# Get and sort matching files
files = sorted(f for f in os.listdir('.') if pattern.match(f))

# Filter out excluded files, with print statements
def filter_files(filename):
    match = pattern.match(filename)
    if not match:
        return None
    prefix = match.group(1)
    if prefix in exc_list:
        print(f"Skipping {filename} (excluded by {prefix})")
        return None
    return filename

# Command runner
def compile_file(filename):
    if '_mgl_' in filename:
        # cmd = ['manimgl', filename, '-w', '-l']
        cmd = ['manimgl', filename, '-w', '--uhd']
    else:
        # cmd = ['manim', '-ql', filename]
        cmd = ['manim', '-qk', filename]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd)

if __name__ == '__main__':
    filtered = list(filter(None, map(filter_files, files)))
    for i in range(0, len(filtered), 4):
        group = filtered[i:i + 4]
        with Pool(processes=min(len(group), NUM_CORES)) as pool:
            pool.map(compile_file, group)


# import os
# import subprocess
# import re

# # Files starting with any of these will be skipped
# exc_list = ['s18']  # Add more as needed

# # Pattern to match files like s01_..., s02_..., etc.
# pattern = re.compile(r'^(s\d{2}).*\.py$')

# # Get and sort matching files
# files = sorted(f for f in os.listdir('.') if pattern.match(f))

# for filename in files:
#     match = pattern.match(filename)
#     prefix = match.group(1)

#     if prefix in exc_list:
#         print(f"Skipping {filename} (excluded by {prefix})")
#         continue

#     if '_mgl_' in filename:
#         cmd = ['manimgl', filename, '-w', '-l']
#     else:
#         cmd = ['manim', '-ql', filename]

#     print(f"Running: {' '.join(cmd)}")
#     subprocess.run(cmd)


# import os
# import subprocess
# import re

# # Files starting with any of these will be skipped
# exc_list = ['s01']  # Add more as needed

# # Pattern to match files like s01_..., s02_..., etc.
# pattern = re.compile(r'^(s\d{2}).*\.py$')

# for filename in os.listdir('.'):
#     match = pattern.match(filename)
#     if not match:
#         continue

#     prefix = match.group(1)
#     if prefix in exc_list:
#         print(f"Skipping {filename} (excluded by {prefix})")
#         continue

#     if '_mgl_' not in filename:
#         cmd = ['manim', '-ql', filename]
#     else:
#         cmd = ['manimgl', filename, '-w', '-l']

#     print(f"Running: {' '.join(cmd)}")
#     subprocess.run(cmd)


# import os
# import subprocess
# import re

# # Pattern to match files like s01_..., s02_..., s09_mgl_...
# pattern = re.compile(r'^s\d{2}.*\.py$')

# for filename in os.listdir('.'):
#     if pattern.match(filename):
        
        
#         if '_mgl_' not in filename:
#             # Use manim
#             cmd = ['manim', '-ql', filename]
        
#         else:
#             # Use manimgl
#             cmd = ['manimgl', filename, '-w', '-l']

#         print(f"Running: {' '.join(cmd)}")
#         subprocess.run(cmd)