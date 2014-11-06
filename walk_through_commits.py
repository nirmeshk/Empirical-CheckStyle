import pygit2
import sys
import time
import subprocess
import basic_style_check_on_project


def main():
    if(len(sys.argv) < 2):
        print("Please provide python file or package path as command line argument")
        exit()
    target = sys.argv[1]
    if not os.path.exists(target):
        print("File or directory does not exists")
        exit()
    elif ((os.path.isfile and target[-3:] == ".py") or 
          (os.path.isdir(target) and '__init__.py' in os.listdir(target)) ): 
        check(target)
    else:
        print("Provided input is neither python file nor a python package."
              " Please Provide a valid python file path or python package path")
        exit()    


def walk_repo(path_to_repo=None, steps=2):
    path_to_repo = sys.argv[1]

    #optionally provide number of commits that need to be skipped between each analysis.
    #The reason being too many commits takes large time to evaluate.
    if(len(sys.argv)>=3): steps = sys.argv[2]

    repo = pygit2.Repository(path_to_repo)

    commit_hash = []
    #Create a list of all commit messages
    for commit in repo.walk(repo.head.target, pygit2.GIT_SORT_TIME):
        #print(commit.hex + '|' + commit.message) 
        commit_hash.append(commit.hex)
    print(commit_hash)

    commit_hash.append('master')
    number_of_commits = len(commit_hash)


    for i in range(0,number_of_commits,steps):
        """Check out on particular commit"""
        cmd = ['git', 'checkout', commit_hash[i]]
        print(cmd)
        p = subprocess.Popen(cmd, cwd=path_to_repo,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdoutdata, stderrdata = p.communicate()
        print("Output:")
        print(stdoutdata)
        print("Error:")
        print(stderrdata)
        print('#'*50)
        time.sleep(5)
        #call pylint code here

    #First Store the current head  
if __name__ == "__main__":
    walk_repo()