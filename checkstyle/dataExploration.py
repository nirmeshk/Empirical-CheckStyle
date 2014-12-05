#import seaborn as sns
import pandas as pd
import MySQLdb
import matplotlib as mpl
import matplotlib.pyplot as plt
from ggplot import *

con = MySQLdb.connect("localhost", "root", "root", "checkstyle" )
df = pd.read_sql('select message, commit_number, message_count from code_analysis where project="fabric" and message in ("syntax-error", "unnecessary-pass", "no-init", "no-member", "duplicate-key", "undefined-loop-variable") order by commit_number', con)

df2= pd.read_sql('select message, commit_number, message_count from code_analysis where project="fabric" order by commit_number',con)


print(ggplot(df, aes(x=commit_number, y=message_count)) + geom_point() + facet_grid( message~.))