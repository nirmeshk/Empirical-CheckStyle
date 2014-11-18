#Analyzing the changes in the coding standards throughout the life cycle of the project.

#####Introduction
For each programming language, there are some coding conventions and style guides that are defined which help to structure your code better. Examples of some of the famous coding standards are [PEP 8](https://www.python.org/dev/peps/pep-0008) for Python and [Oracle's Guide](http://www.oracle.com/technetwork/java/codeconvtoc-136057.html) for Java. Following the coding conventions ensures better code quality and readability. Also, it helps to maintain a consistency in coding pattern throughout the organization or  particular project. In open source projects, it is very hard to maintain these standards as there are many collaborators. This sometimes makes the code hard to understand for new contributors. The goal of this project is to analyze how these standard change over the life-cycle of the project. This report provides several analysis of famous git hub repositories taking into account different matrix. There are several parsers available for different languages that analyze the code for bad coding styles and gives you detailed report. I have used [Pylint](http://www.pylint.org/) to analyze some 10 famous Python repositories.

##### Basic Analysis of the repositories.

In this section, I provide some overall analysis. Pylint provides a detailed analysis of errors such as checking line-code's length,
checking if variable names are well-formed according to PEP 8 coding standard, checking if imported modules are used, etc.

Below is the plot of basic code score Normalized by Number of lines of code over the life cycle. It can be observed from the plot, that there is very little change in the overall code score throughout the life cycle. Even as the number of lines of code increase, the error messages and warnings also increase along with that.

![Code Score](code_score.png)

This motivates us to analyze the code on more fine grain level. By checking the error messages at each checkpoint, it was discovered that the nature of errors and warning is diverse. It can be easily deduced from the plot below that there are broadly 2 different types of error messages- there are some that persist throughout the life-cycle of the project and others which appear at some point, and then are fixed.

![Number Of Messages](message_throughout_lifecyle.png)

