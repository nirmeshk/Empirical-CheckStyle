#import seaborn as sns
import pandas as pd
import MySQLdb
import matplotlib as mpl
import matplotlib.pyplot as plt
from ggplot import *

def main():
    plot_figure_2()

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

if __name__ == '__main__':
    main()