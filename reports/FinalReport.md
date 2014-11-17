#Analyzing the changes in the coding standards throughout the life cycle of the project.

#####Introduction
For each programming language, there are some coding conventions and style guides that are defined which help to structure your code better. Examples of some of the famous coding standards are [PEP 8](https://www.python.org/dev/peps/pep-0008) for Python and [Oracle's Guide](http://www.oracle.com/technetwork/java/codeconvtoc-136057.html) for Java. Following the coding conventions ensures better code quality and readability. Also, it helps to maintain a consistency in coding pattern throughout the organization or  particular project. In open source projects, it is very hard to maintain these standards as there are many collaborators. This sometimes makes the code hard to understand for new contributors. The goal of this project is to analyze how these standard change over the life-cycle of the project. This report provides several analysis of famous git hub repositories taking into account different matrix. There are several parsers available for different languages that analyze the code for bad coding styles and gives you detailed report. I have used [Pylint](http://www.pylint.org/) to analyze some 10 famous Python repositories.

##### Basic Analysis of the repositories.

In this section, I provide some overall analysis. Pylint provides a detailed analysis of errors such as checking line-code's length,
checking if variable names are well-formed according to PEP 8 coding standard, checking if imported modules are used, etc.


![blah](message_throughout_lifecyle.png)

