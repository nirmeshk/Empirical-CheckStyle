#import pygit2
import sys
import time
import subprocess
import style_check_project
import os
import math


def main():
    if(len(sys.argv) < 4):
        print("Please provide input in following format:"
            "python3 <repo_path> <package_path> <module_name>")
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

def walk_repo(module_name, package_path):
    
    #final_commit_list = find_most_large_commits(package_path, commit_hash)
    #RESET head to master branch origional
    cmd = "git checkout master"
    p = subprocess.Popen(cmd, cwd=package_path, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutdata, stderrdata = p.communicate()

    commit_hash = get_commit_list(package_path)
    step_size = calculate_step_size( len(commit_hash) )
    
    for c_i in range(0, len(commit_hash), step_size):
        try:
            #Check out on particular commit
            cmd = 'git checkout ' + commit_hash[c_i]
            print(cmd)
            p = subprocess.Popen(cmd, cwd=package_path, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdoutdata, stderrdata = p.communicate()
            print("Output:")
            print(stdoutdata)
            print("Error:")
            print(stderrdata)
            print('#'*50)
            time.sleep(5)
            #Call the function to analyse the code scores for this particular commit
            style_check_project.check(package_path, 
                module_name = module_name, 
                write_to_db = True, 
                commit_hash = commit_hash[c_i],
                commit_number = c_i )
        except FileNotFoundError:
            continue

    print("Finished processing..Reset the head to origional position..")
    cmd = 'git checkout master'
    p = subprocess.Popen(cmd, cwd=package_path, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutdata, stderrdata = p.communicate()

def get_commit_list(package_path):

    path = package_path + '/' + "__init__.py"

    cmd = "git log --diff-filter=A --follow --format='%h' -1 -- " + path 
    print(cmd)

    p = subprocess.Popen(cmd, cwd=package_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdoutdata, stderrdata = p.communicate()
    print("out: " + stdoutdata + "err:" + stderrdata)

    cmd = "git log --pretty=format:'%h' " + stdoutdata.strip(' \t\n\r') + "..HEAD"
    print(cmd)
    #print(cmd)
    p = subprocess.Popen(cmd, cwd=package_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdoutdata, stderrdata = p.communicate()

    #Create a list of all commit messages
    commit_hash = [commit for commit in stdoutdata.splitlines()]

    #Reverse the list to parse it in chronological order
    commit_hash.reverse()
    #print(commit_hash)
    return commit_hash


def find_most_large_commits(package_path, commit_hash, number_of_commits_to_return = 50):
    """returns top 100 commits that have most changes in them"""
    final_scores = []

    for c1, c2 in zip(commit_hash,commit_hash[1:]):
        cmd = "git diff --shortstat %s %s" % (c1, c2)
        p = subprocess.Popen(cmd, cwd=package_path, shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdoutdata, stderrdata = p.communicate()
        stats = [int(s) for s in stdoutdata.split() if s.isdigit()]
        #print(stats)
        score = sum(stats)
        final_scores.append( (c2,score) )

    #Sorting commits by there score
    final_scores.sort(key = lambda item: item[1])

    return [ x for x,y in final_scores[:number_of_commits_to_return] ]


def calculate_step_size(number_of_commits):
    #The goal is to create 100 checkpoints during the entire lifetime of project
    return math.ceil( number_of_commits/100 )


if __name__ == "__main__":
    main()