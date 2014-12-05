#Analyzing the changes in the coding standards throughout the life cycle of the project.

####Introduction
For each programming language, there are some coding conventions and style guides that are defined, which helps to structure your code and provide better readability. Examples of some of the famous coding standards are [PEP 8](https://www.python.org/dev/peps/pep-0008) for Python and [Oracle's Guide](http://www.oracle.com/technetwork/java/codeconvtoc-136057.html) for Java. Following the coding conventions ensures better code quality and readability. Also, it helps to maintain a consistency in coding pattern throughout the organization. 

In open source projects, it is difficult to maintain these standards as there are many collaborators. This sometimes makes the code hard to understand for new contributors. The goal of this project is to analyze how the coding style changes over the life-cycle of the project. This report provides several analysis of famous git hub repositories taking into account different metrics. 

For most of the languages, there are tools available that scan the code and gives different warnings related to coding styles. The project attempts to identify the type of warnings that occur during different stages of the project. Also, some of the warnings may be less important then others. Apart from observing the nature of these warnings, this analysis tries to provide an efficient way prioritize them.

####Data Collection
In order to collect the sufficient data for my analysis, I have selected below mentioned repositories from github.
The selection is based on 'trending this month' and 'Most forked repositories', for Python language. One can easily search on github based on these 2 criteria.

Selected repositories:

- [Pandas](https://github.com/pydata/pandas.git)
- [Reddit](https://github.com/reddit/reddit.git)
- [Fabric](https://github.com/fabric/fabric.git)
- [Django](https://github.com/django/django.git)
- [Neurokernals](https://github.com/neurokernel/neurokernel.git)
- [Youtube-dl](https://github.com/rg3/youtube-dl.git)
- [Pydub](https://github.com/jiaaro/pydub.git)
- [Tornado](https://github.com/tornadoweb/tornado.git)
- [Scrapy](https://github.com/scrapy/scrapy.git)
- [Ipytho](https://github.com/ipython/ipython.git)
- [Matplotlib](https://github.com/matplotlib/matplotlib.git)
- [Python Koans](https://github.com/gregmalcolm/python_koans.git)

####Introduction to Pylint
There are several parsers available for different languages that analyze the code for bad coding styles and gives you detailed report. I have used [Pylint](http://www.pylint.org/). Pylint is python based tool that helps in finding these warnings for python language. When you parse a python package using Pylint, it gives you error and warning messages along with their count and position of particular warning message in the code. Some of the uses of Pylint are checking line-code's length, checking if variable names are well-formed according to PEP 8 coding standard, checking if imported modules are used, etc. 

It also provides you a **Normalized score for the code out of 10.0**.

####Analysis of the repositories
In this section, I provide analysis results after running Pylint on projects. 

For each repo, 100 commits are selected as checkpoints. For e.g if you have 5000 commits in the project, you place a checkpoint after each 50 commit. Then Pylint is run on code at each checkpoint.

Below are the two plot - 1. Lines of code at each checkpoint & 2. Overall code score Normalized by Number of lines of code over the life cycle. It can be observed from the plot, that there is very little change in the overall code score throughout the life cycle. Even as the number of lines of code increase, the error messages and warnings also increase along with that.

![Code Score](code_score.png)

This motivates us to analyze the code on more fine grain level. By checking the error messages at each checkpoint, it was discovered that the nature of errors and warning is diverse. It can be easily deduced from the plot below that there are broadly 2 different types of error messages- there are some that persist throughout the life-cycle of the project and others which appear at some point, and then are fixed.

At each checkpoint, there are large number of error messages. Currently I am showing only top-6 and bottom-6 messages in the below plot.
![Number Of Messages](message_throughout_lifecyle.png)

####Prioritizing warnings based on the above analysis.

* Messages with highest frequency:
    * invalid-name
    * missing-docstring
    * unused-import
    * superfluous-parens
    * unused-wildcard-import
    * line-too-long
* Messages with lowest frequency:
    * syntax-error
    * unnecessary-pass
    * no-init
    * no-member
    * duplicate-key
    * undefined-loop-variable

####Conclusion
Need to get some feedback from professor.
