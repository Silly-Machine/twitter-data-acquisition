import os

# Get the current directory of the notebook
notebook_dir = os.getcwd()

# Get the root directory's path (assuming the notebook is located in the notebooks folder)
root_dir = os.path.abspath(os.path.join(notebook_dir, ".."))

# Set the root directory as the working directory
os.chdir(root_dir)
