import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None or suffix is None or len(suffix) == 0 or not path:
        return None

    files = []
    for entry in os.scandir(path):
        if entry.is_dir():
            files.extend(find_files(suffix, entry))
        elif entry.is_file() and entry.name.endswith(suffix):
            files.append(entry.path)
    return files

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files('.c', 'testdir'))

# Test Case 2
print(find_files('.h', 'testdir'))

# Test Case 3
print(find_files(None, 'testdir'))
print(find_files('.c', None))
print(find_files('', 'testdir'))
print(find_files('.py', ''))

