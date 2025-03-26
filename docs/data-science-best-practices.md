# Data Science Best Practices

## Table of Contents
* [Using Python in an IDE](#using-python-in-an-ide)
* [GitHub Best Practices](#github-best-practices)
* [Creating a Package](#creating-a-package)

## Using Python in an IDE 

### Create a Virtual Environment for Each New Project
A best practice among Python developers is to avoid installing packages into a global interpreter environment. You instead use a project-specific  `virtual environment`  that contains a copy of a global interpreter. An "environment" in Python is the context in which a Python program runs. An environment consists of an interpreter and any number of installed packages. A virtual environment is a subfolder in a project that contains a copy of a specific interpreter. When you activate the virtual environment, any packages you install are installed only in that environment's subfolder. When you then run a Python program within that environment, you know that it's running against only those specific packages. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions. To create a  _virtual environment_  and install the required packages, enter the following commands as appropriate for your operating system:

* For Windows:
```
python3 -m venv .venv
.venv\scripts\activate
```
* Alternatively, for Linux just type:
 ```
 virtualenv nameofdir
```

* And then to activate it:
```
source mypython/bin/activate
```
and ```deactivate``` to stop. You can switch environments at any time; switching environments helps you test different parts of your project with different interpreters or library versions as needed.

Any changes you make to an activated environment within the terminal are persistent. For example, using  `conda install <package>`  from the terminal with a conda environment activated installs the package into that environment permanently. Similarly, using  `pip install`  in a terminal with a virtual environment activated adds the package to that environment.

### Using jupyter notebooks with a virtual environment

see [here](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/).

### Correct Broken Code Immediately
Like with the broken code theory, correct your broken code immediately. If you let it be while you work on something else, it can lead to worse problems later. This is what Microsoft does. It once had a terrible production cycle with MS Word’s first version. So now, it follows a ‘zero defects methodology’, and always corrects bugs and defects before proceeding.

### Follow Style Guidelines

The PEP8 holds some great community-generated proposals. PEP stands for Python Enhancement Proposals - these are guidelines and standards for development. There are other PEPs like the PEP20, but PEP8 is the Python community bible for you if you want to properly style your code. This is to make sure all Python code looks and feels the same. For example:

-   Use proper naming conventions for variables, functions, methods, and more.
-   Variables, functions, methods, packages, modules: this_is_a_variable
-   Classes and exceptions: CapWords
-   Protected methods and internal functions: _single_leading_underscore
-   Private methods: __double_leading_underscore
-   Constants: CAPS_WITH_UNDERSCORES
-   Use 4 spaces for indentation.

### Use Long and Descriptive Variable Names

Have you noticed anything about the examples above? The names of functions and variables almost always quite long. That’s no coincidence. It may seem superfluous to use so many characters for a bit of code, but it’s a lot better for reading the code. Besides, it doesn’t take that much longer to code — most editors have autocomplete anyway.


### Comment Well

Make sure you keep your comments short and to-the-point. I like to think about what somebody would like to read if they’d never seen my code but had a look at it now because they wanted to change something. Comments are designated with a hash mark (#). Python ignores everything after the hash mark and up to the end of the line. You can insert them anywhere in your code, even inline with other code

## GitHub Best Practices
GitHub is a code sharing site for programmers. Think of it as a combination of a cloud storage platform and a back-up service for all of your Computer Programming needs. 

Git is a Version Control System (VCS), a category of software tools that help teams manage changes to source code over time. VSCs keep track of every modification to the code in a special kind of database. It’s a filing system for every draft of a document.

For a full-length tutorial on how to use GitHub for collaborative work [see here](https://github.com/cassgvp/github-for-collaborative-documentation) and [here](https://www.neonscience.org/resources/learning-hub/tutorials/git-setup-remote).

### Writing Commit messages

In general, a commit message should be a short (72 chars or less) summary. Even detailed explanatory text should be capped at this. However, longer messages should have a  _subject line_, followed by a blank line that seperates it from the main body - unless you omit the body entirely.

**Rule of Thumb**

A properly formed git commit subject line should always be able to complete the following sentence:

> _If applied, this commit will <your subject line here>_
> 

read more [here](https://github.com/SianJMBrooke/Introduction_To_Git/blob/master/Commit_Message_Guidelines.md). 

### Moving files into new locations using the command line

You can use the command line to move files within a repository by removing the file from the old location and then adding it in the new location: see [here](https://docs.github.com/en/github/managing-files-in-a-repository/moving-a-file-to-a-new-location-using-the-command-line ).

### Using Project Boards to assign tasks

Use [Project Boards](https://rhianvanesch.com/posts/2019/11/10/staying-organised-with-github-project-boards/) to improve your GitHub workflow in terms of setting tasks and keeping an overview of what tasks need completing.

### Installing Packages from GitHub

`pip install git+git://github.com/django/django.git`

there are in fact three ways you can install repositories, depending on whether a `setup.py` file is included; see [here](https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github) for details. 


### GitHub key terms

Before we set up GitHub it is crucial that we familiarise you with some key terms. The definitions below will help you follow the instructions to set up GitHub for your course and troubleshoot any problems you may have. These terms aren’t specific to GitHub; they are used anywhere that employs Git VCS.

**Branch**

> A version of the repository that diverges from the main working project. Branches can be a new version of a repository, experimental changes, or personal forks of a repository for users to alter and test changes.

**Checkout**

> The git checkout command is used to switch branches in a repository.

**Clone**

> A clone is a copy of a repository or the action of copying a repository.

**Fetch**

> By performing a Git fetch, you are downloading and copying that branch’s files to your computer. Multiple branches can be fetched at once, and you can rename the branches when running the command to suit your needs.

**Fork**

> Creates a copy of a repository.

**HEAD**

> HEAD (capitals) is a reference variable used to denote the most current commit of the repository in which you are working. When you add a new commit, HEAD will then become that new commit.

**Master**

> The primary branch of all repositories. All committed and accepted changes should be on the master branch. You can work directly from the master branch, or create other branches.

**Merge**

> Taking the changes from one branch and adding them into another (traditionally the master) branch. These commits are usually first requested via pull request before being merged by the user who maintains the project.

**Origin**

> The conventional name for the primary version of a repository. Git also uses origin as a system alias for pushing and fetching data to and from the primary branch.

**Pull/Pull Request**

> If someone has changed code on a separate branch of a project and wants it to be reviewed to add to the master branch, that someone can put in a pull request. Pull requests ask the user who maintains the repo to review the commits made, and then, if acceptable, merge the changes upstream. A pull happens when adding the changes to the master branch. When think ing about branches, remember that the  _base branch_  is  **where**  changes should be applied, the  _head branch_  contains  **what**  you would like to be applied.

**Push**

> Updates a remote branch with the commits made to the current branch. You are literally “pushing” your changes onto the remote.

**Remote**

> A copy of the original branch. When you clone a branch, that new branch is a remote, or clone. Remotes can talk to the origin branch, as well as other remotes for the repository, to make communication between working branches easier.

**Upstream**

> While there is not necessarily a default “upstream” or “downstream” for Git projects, upstream can be considered where you push your Git changes — this is often the master branch of the project within the origin
> 

## Creating a requirements.txt

A requirements file is a list of all of a project's dependencies. This includes the dependencies needed by the dependencies. It also contains the specific version of each dependency, specified with a double equals sign ( == ). pip freeze will list the current projects dependencies to stdout

Use Pipenv or other tools for improving your development flow.

`pip3 freeze > requirements.txt  # Python3`

## Creating a package

What is a Package?
A collection of modules

… and the documentation

… and the tests

… and any top-level scripts

… and any data files required

… and a way to build and install it…

For python packaging tools and more see [here](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html).
