A report on data Exploration tasks performed for the project
=============================================================

I have cloned 20 representative projects from GitHub in python language. 

10 repositories are selected based on trends of Last month. Following are there git hub URL:

- https://github.com/pydata/pandas.git
- https://github.com/reddit/reddit.git
- https://github.com/taigaio/taiga-back.git
- https://github.com/jonathanslenders/python-prompt-toolkit.git
- https://github.com/jiaaro/pydub.git
- https://github.com/django/django.git
- https://github.com/schematics/schematics.git
- https://github.com/neurokernel/neurokernel.git
- https://github.com/rg3/youtube-dl.git
- https://github.com/datamade/usaddress.git


10 repositories are selected based on Most forked python repositories on github.

- https://github.com/tornadoweb/tornado.git
- https://github.com/scrapy/scrapy.git
- https://github.com/ipython/ipython.git
- https://github.com/divio/django-cms.git
- https://github.com/faif/python-patterns.git
- https://github.com/gregmalcolm/python_koans.git
- https://github.com/matplotlib/matplotlib.git
- https://github.com/edx/edx-platform.git
- https://github.com/simplegeo/python-oauth2.git
- https://github.com/fabric/fabric.git

Since git version control contains all the historical changes and diffs, we can simply checkout to any commit, and run Analysis of Check styling on that particular version to see how the coding standards are improving over the period of time.

###Checking coding styles using Pylint

Pylint is a tool used to analyse the coding errors and styles in python. By Running pylint on core module of Pandas repository, it gives us following basic analysis:

|message id                     |occurrences |
|-------------------------------|------------|
|invalidname                    |1049        |
|nomember                       |953         |
|missingdocstring               |936         |
|protectedaccess                |504         |
|linetoolong                    |454         |
|badwhitespace                  |316         |
|unusedargument                 |143         |
|toomanyarguments               |128         |
|starargs                       |101         |
|toomanybranches                |91          |
|unusedwildcardimport           |74          |
|unusedvariable                 |73          |
|toomanylocals                  |71          |
|bareexcept                     |59          |
|fixme                          |55          |
|redefinedbuiltin               |48          |
|importerror                    |43          |
|maybenomember                  |42          |
|noselfuse                      |39          |
|toofewpublicmethods            |36          |
|locallydisabled                |35          |
|toomanypublicmethods           |31          |
|superfluousparens              |31          |
|attributedefinedoutsideinit    |31          |
|unpackingnonsequence           |29          |
|redefinedoutername             |29          |
|toomanystatements              |26          |
|unusedimport                   |21          |
|broadexcept                    |20          |
|argumentsdiffer                |19          |
|abstractmethod                 |18          |
|toomanyreturnstatements        |15          |
|nonameinmodule                 |15          |
|toomanylines                   |14          |
|toomanyinstanceattributes      |12          |
|badbuiltin                     |9           |
|pointlessstringstatement       |8           |
|undefinedvariable              |7           |
|unnecessarylambda              |6           |
|duplicatecode                  |6           |
|badstaticmethodargument        |6           |
|anomalousbackslashinstring     |6           |
|reimported                     |5           |
|abstractclassnotused           |5           |
|superinitnotcalled             |4           |
|wildcardimport                 |3           |
|oldstyleclass                  |3           |
|multiplestatements             |3           |
|emptydocstring                 |3           |
|dangerousdefaultvalue          |3           |
|raisingbadtype                 |2           |
|methodhidden                   |2           |
|globalstatement                |2           |
|functionredefined              |2           |
|execused                       |2           |
|unreachable                    |1           |
|unbalancedtupleunpacking       |1           |
|notimplementedraised           |1           |
|notcallable                    |1           |
|globalvariableundefined        |1           |
|globalvariablenotassigned      |1           |
|deprecatedlambda               |1           |
|blacklistedname                |1           |
|badindentation                 |1           |

##Code Rating given by Pylint

Your code has been rated at 4.86/10

##Conclusions

The basic data exploration shows that we need to tweak some of the warning messages provided by Pylint. In addition to that, we need to use other code check styles such as PEP8 and PyFlakes, and compare the results. 

Another challenge is that differnt organisations follow different coding conventions. How do we compare the results in such scenario.  
