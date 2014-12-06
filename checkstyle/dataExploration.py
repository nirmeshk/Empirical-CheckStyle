#import seaborn as sns
import pandas as pd
import MySQLdb
import matplotlib as mpl
import matplotlib.pyplot as plt
from ggplot import *
from collections import defaultdict

def main():
    #plot_figure_1()
    #plot_figure_2()
    #plot_figure_3()
    find_priority_warnings()

def plot_figure_1():
    con = MySQLdb.connect("localhost", "root", "root", "checkstyle" )

    df = pd.read_sql('select message, commit_number, message_count from code_analysis where project="fabric" and message in ("syntax-error", "unnecessary-pass", "no-init", "no-member", "duplicate-key", "undefined-loop-variable") order by commit_number', con)

    data_1 = pd.read_sql('select commit_number, score from code_score where project ="fabric" order by commit_number', con )


    data_2 = pd.read_sql('select commit_number, statement_count from code_score where project = "fabric" order by commit_number', con)

    p1 = ggplot(data_1, aes(x='commit_number', y='score')) +  xlab("Commit Numbers") + ylab("Normalized Score") + geom_line()
    print(p1)

    p2 = ggplot(data_2, aes(x='commit_number', y='statement_count')) +  xlab("Commit Numbers") + ylab("Lines of Code") + geom_line()
    print(p2)

    con.close()


def plot_figure_2():
    con = MySQLdb.connect("localhost", "root", "root", "checkstyle" )
    
    df_1= pd.read_sql('select message, commit_number, message_count from code_analysis where project="fabric" and message in ("invalid-name","missing-docstring","unused-import","superfluous-parens", "unused-wildcard-import","line-too-long")  order by commit_number',con)

    df_2 = pd.read_sql('select message, commit_number, message_count from code_analysis where project="fabric" and message in ("syntax-error", "unnecessary-pass", "no-init", "no-member", "duplicate-key", "undefined-loop-variable") order by commit_number', con)

    print(ggplot(df_1, aes(x='commit_number', y='message_count')) + geom_point() + facet_grid( 'message' ))

    print(ggplot(df_2, aes(x='commit_number', y='message_count')) + geom_point() + facet_grid( 'message' ))
    con.close()

def plot_figure_3():
    con = MySQLdb.connect("localhost", "root", "root", "checkstyle" )
    df_1 = pd.read_sql('select message, sum(message_count) as total_count from code_analysis group by message order by total_count',con)
    p1 = ggplot(df_1, aes(x='message', y='total_count')) + geom_bar( stat="identity" )
    print(p1)
    con.close()


def find_priority_warnings():
    """A function that decides priorities of various warning messages"""
    con = MySQLdb.connect("localhost", "root", "root", "checkstyle" )
    cur = con.cursor()
    
    cur.execute("SELECT distinct project FROM code_score")
    rows = cur.fetchall()
    project_list = [row[0] for row in rows]
    #project_list = ['fabric']
    print("Project List:") 
    print(project_list)

    #These variable keep the support count of each warning in order to select those warnings
    high_priority = defaultdict(int)
    low_priority = defaultdict(int)

    #create a feature vector [message, longest_streak, total_count]
    for project in project_list:
        print("Starting process for project " + project + "..")
        cur.execute("SELECT distinct commit_number  FROM code_analysis where project = '" + project + "'")
        rows = cur.fetchall()
        commit_list = [row[0] for row in rows]
        cur.execute("SELECT distinct message FROM code_analysis where project = '" + project + "'")
        rows = cur.fetchall()
        message_list = [row[0] for row in rows]

        final_list = []

        for message in message_list:
            streaks = []
            query = "SELECT commit_number, message, message_count FROM code_analysis where project = '%s' and message = '%s'"%(project, message)
            cur.execute( query )
            commit_to_count = defaultdict(int) 
            rows = cur.fetchall()
            for row in rows: 
                commit_to_count[ row[0] ] = row[2]
            count = 0
            for commit in commit_list:
                if (commit_to_count[commit] > 0): #and commit_to_count[commit] > commit_to_count[previous_commit]/2):
                    count += 1
                else:
                    if count > 0: 
                        streaks.append(count) 
                        count = 0             
            streaks.append(count)
            final_list.append( (message, max(streaks)) )

        final_list.sort(key = lambda x: x[1])
        for x,y in final_list[0:20]:
            high_priority[x] += 1
        for x,y in final_list[-20:]:
            low_priority[x] += 1

    import operator
    high_priority = sorted(high_priority.items(), key=operator.itemgetter(1), reverse=True) 
    print("-"*100)
    print("20 Highest priority warnings")
    print("-"*100)
    for x,y in high_priority: print('|' + x + '\t|' + str(y) + '\t|')
    print("-"*100)
    print("20 lowest priority warnings")
    print("-"*100)
    low_priority = sorted(low_priority.items(), key=operator.itemgetter(1), reverse=True)
    for x,y in low_priority: print('|' + x + '\t|' + str(y) + '\t|')

if __name__ == '__main__':
    main()