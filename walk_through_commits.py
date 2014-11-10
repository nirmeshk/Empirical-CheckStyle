#import pygit2
import sys
import time
import subprocess
import style_check_project
import os


def main():
    if(len(sys.argv) < 4):
        print("Please provide input in following format:"
            "python3 <package_path> <module_name> <steps_size> ")
        exit()
    path_to_repo = sys.argv[1]
    module_name = sys.argv[2]
    steps = int(sys.argv[3])

    if not os.path.exists(path_to_repo):
        print("File or directory does not exists")
        exit()
    elif ((os.path.isfile and path_to_repo[-3:] == ".py") or 
          (os.path.isdir(path_to_repo) and '__init__.py' in os.listdir(path_to_repo)) ): 
        walk_repo(module_name, path_to_repo, steps=steps)
    else:
        print("Provided input is neither python file nor a python package."
              " Please Provide a valid python file path or python package path")
        exit()

def walk_repo(module_name, path_to_repo, steps=100):

    #optionally provide number of commits that need to be skipped between each analysis.
    #The reason being too many commits takes large time to evaluate.
    cmd = ["git", "log", "--pretty=format:'%h'"]
    print(cmd)
    p = subprocess.Popen(cmd, cwd=path_to_repo,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutdata, stderrdata = p.communicate()

    commit_hash = []
    #Create a list of all commit messages

    out = stdoutdata.decode('utf-8').replace("'","")

    for commit in out.split('\n'):
        commit_hash.append(commit)
    print(commit_hash)

    #RESET head to master branch origional
    cmd = ['git', 'checkout', 'master']
    p = subprocess.Popen(cmd, cwd=path_to_repo,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutdata, stderrdata = p.communicate()

    number_of_commits = len(commit_hash)

    for c_i in range(0, number_of_commits, steps):
        #Check out on particular commit
        cmd = ['git', 'checkout', commit_hash[c_i]]
        print(cmd)
        p = subprocess.Popen(cmd, cwd=path_to_repo,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdoutdata, stderrdata = p.communicate()
        print("Output:")
        print(stdoutdata)
        print("Error:")
        print(stderrdata)
        print('#'*50)
        time.sleep(5)
        #Call the function to analyse the code scores for this particular commit
        style_check_project.check(path_to_repo, module_name = module_name, write_to_db = True, commit_hash = commit_hash[c_i])

    print("Finished processing..Reset the head to origional position..")
    cmd = ['git', 'checkout', 'master']
    p = subprocess.Popen(cmd, cwd=path_to_repo,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutdata, stderrdata = p.communicate()

if __name__ == "__main__":
    main()