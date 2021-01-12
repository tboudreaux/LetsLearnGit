# Let's Learn Git
## Thomas M. Boudreaux
## January 2021

Welcome to Let's  Learn Git!

<hline>

### What is git? 
Git is version control software that runs locally on your computer. It tracks
all the changes that you tell it about to files within a "repository". It is
important to note that git does not run as a service on your computer; rather
its an application that you run (generally through the command line) when you
need it. Therefore, when coming from things like google docs (or some other
version control software!) that automatically exchange content between users,
its important to reframe how you think about collaboration when using git. With
git you are always working on files local to your computer.

Let's break down some of this terminology. Im gonna skip actually doing
anything for the time. And just talk about the concepts.

#### Repositories, what are they?
Repositories are the highest level structure git understands. Whenever you run
git it checks if you are in a repository. The first step in making a new
project you want on git, or to move an old project onto git is to initialize a
repository. Practically, all a repoitory is is a hidden folder (folder name
prepended with a period on UNIX like systems) called ".git" that stores all of
the version control information. This folder lives at the top of the
repository; however, you can have any number of nested subfolders, all of which
are considered in the same repository. Note that, git enfoces the rule that you
cannot have a repository within another repository.

Repositories store a lot of information. Obviously they can store code.
However, recognize that they can really store any arbitrary data. You can
version control any files you have read permissions for. For every file in the
repository a log is stored of versions, differences between versions, and
authors of versions. 


#### Versioning in local git or How I learned to stop fearing and Commit to the code.
So lets say, you, a young and adventerous astronomer, want to track a software
project for whatever reason. You initialize a git repository and write some
code in a file, lets call it "solveH0.cpp", now what? As I hinted at before,
just writing the file within the repository is not enough. You now have to tell
git to "add" that file (formally you are adding to the git staging area).
Depending on your text editor you may get some kind of note marking
"solveH0.cpp" as an untracked file. So you add the file, all done right? Nope!
The final step is to "commit" the changes for all added files. You commit all
files in the staging area. You must provide a brief description of the commit.
So the most important "concept loop" to keep handy in your head is the "write,
add, commit" loop. Write some amount of code, add that code to the git staging
area, commit that code to the repository, repeate. There are other complexities
such as branching versions but for now we can leave those.

A couple points of note. You can add as many files to the staging area as you
like at one time, but every time you commit, it only commits the staging area,
so don't forget to add the files every time. Git commits, while not technically
undeletable, are by design very hard to delete. So make sure you don't
acidently commit something you dont want to be in the "semi-perminate" record.
Here I really mean don't accidently commit a password or something. I've done
it, its a bain in the behind to deal with.

Locally that's the basic concept. At any point you can revert to any commit
(perminatly or temporarily) and you can do that on a file by file or even line
by line approach depending on how deep you wanna delve into the commands.

#### Versioning with git servers: The rise of GitHub
There are two models of multiuser version control. They have more formal names,
but generally you can think of them as "checkout based" and "resolution based".
Both of these are ways to handel how a document can be edited with multiple
people trying to change it at the same time. Imagine the first "checkout based"
as a system where there is only one copy of each document. If you want to edit
you have to "checkout" that document. While it is checkedout no one else can
edit it until you return it. In the second anyone can edit any file at any
time, git operates as the second kind.

This "resolution based" system has the advantage that you don't have to wait
for the other person to return the file; however, it leads to the all to common
occurence of two versions of the file existing on different peoples computers.
Have no fear intrepid astronomer, git has robust tools to deal with this.

Say two versions of "solveH0.cpp" exist. One on "Cosmology Marry's" (CM)
computer and the other on "Local Universe Joe's" (LUJ) computer. CM and LUJ can
both edit, add, and commit the files to their hearts content without any
apparent issue. However, eventually they will be pleased with their code and
want to "push" it to the server. Pushing can be thought of as packing up all
the commits you have done since the last push, sending off to some git server,
and saying "Hey, I've made some new commits, can you take these?". Imagine that
CM pushes first. The server says "Yup, I can take them". But them LUJ tries to
push. The server says "Wait! The oldest commit you are trying to push is older
than the current newest commit, CONFLICT!". Basically CM pushed fine because
the code had not changed on the server since she last "pulled" from it;
however, once she pushed, that same condition was not true for LUJ, so the the
server will ask "what version of this should we use?".

This is actually done on a line by line basis. You can use any number of tools
to resolve conflicts between different commits. They all basically work by
putting an A and a B file on screen (two different versions of the same file)
and for every line that differs between them you select if you want the A
version or the B version. Obviously this can be tedious, but it turns out to be
a very effective collaboration approach. Especially, if there is a disscusion
about who will edit what files/what part of what files.

This is also where GitHub comes into it. Git is a local tool as I said. GitHub
is a simply a git server. So all the commands that you issue are git commands
put when you push you will push to GitHub. There are other git servers such as
git lab and you can even host your own. But GitHub is definitely the most
widley used.

#### Let's get a little practical here
Imagine the following setup: 

A directory stucture which looks like:

├── data
│   └── data.csv
├── README.md
└── src
    ├── secretAstro.py
    ├── solveAstronomy.py
    └── utils.py
