import sys
from walk_through_commits import walk_repo

def main():
    if(len(sys.argv) < 4):
        print("Please provide input in following format:"
            "python3 <repo_path> <package_path> <project_name>")
        exit()


    path_to_repo = sys.argv[1]
    package_path = sys.argv[2]
    module_name = sys.argv[3]

    walk_repo(module_name, package_path)

    """
    if not os.path.exists(path_to_repo):
        print("File or directory does not exists")
        exit()
    elif ((os.path.isfile and path_to_repo[-3:] == ".py") or 
          (os.path.isdir(path_to_repo) and '__init__.py' in os.listdir(path_to_repo)) ): 
        
    else:
        print("Provided input is neither python file nor a python package."
              " Please Provide a valid python file path or python package path")
        exit()
    """

if __name__ == "__main__":
    main()