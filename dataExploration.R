library(ggplot2)
library(RMySQL)
multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)
  # reference : http://www.cookbook-r.com/Graphs/Multiple_graphs_on_one_page_(ggplot2)/
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}



con <- dbConnect(MySQL(), user="root", password="root",
                  dbname="checkstyle", host="localhost")

data1 = dbGetQuery(con, 'select message, commit_number, message_count from code_analysis 
                 where project="fabric" and message in 
                 ("invalid-name","missing-docstring","unused-import","superfluous-parens",
                 "unused-wildcard-import","line-too-long") order by commit_number' )

p1 <- ggplot(abc, aes(x=commit_number, y=message_count)) + geom_line() + facet_grid( message~.)

data2 = dbGetQuery(con, 'select message, commit_number, message_count from code_analysis 
                 where project="fabric" and message in 
                 ("syntax-error","unnecessary-pass","multiple-statements",
                  "no-init","no-member","catching-non-exception",
                   "duplicate-key","undefined-loop-variable") order by commit_number' )

p2 <- ggplot(data2, aes(x=commit_number, y=message_count)) + geom_line() + facet_grid( message~.)


multiplot(p1,p2,cols=2)







