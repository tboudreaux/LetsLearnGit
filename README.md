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
Imagine the following setup. 

You have not yet intialized a repository, you have the start of a project;
however, you want to track it on version control.

Let's say you start with a directory stucture that looks like:

```bash
├── data
│   └── data.csv
├── README.md
└── src
    ├── secretAstro.py
    ├── solveAstronomy.py
    └── utils.py
```

When I say "root" I mean in the folder containing "data/" "src/" and
"README.md". The first step is to, from the root, run 
```bash
git init
```
This will initialize a repository for you. The folder structure will now be
(note. there is stuff inside .git, but its not important to be familar with
that)
```bash
├── data
│   └── data.csv
├── .git
├── README.md
└── src
    ├── secretAstro.py
    ├── solveAstronomy.py
    └── utils.py

```
Okay, your project is now a bonafied git repository, just like you always
dreamed it would be. You now need to make your first commit. But wait you say,
before I can commit, I must add! Right you are. You can run the following
command
```bash
git add data/data.csv README.md src/secretAstro.py src/solveAstronomy.py src/utils.py
```
That will add all those files to the staging area. Thats actually kinda a long
command, especially if you have to issue it every time. You can use the shorthand
```bash
git add .
```
to add all files in the current working directory (represented by the period).
Basically git add is recursive so if you give it a directory it will add all
files within that directory. Okay, NOW we can commit things. 
```bash
git commit -m "Initial Commit"
```
This commit everything in the staging area with the message "Initial Commit".
You are required to include some message with every commit (Incidently I have a
conspiracy theory that venmo uses git as their ledgure and thats why you need a
message with every venmo transfer). Note that the first time you run this it
will ask for a name an email for records that store with the commit.


#### Actually Using GitHub

Okay, now lets say that you want to push this to a GitHub repo. You can't
simply push it, first you need to tell your local repository that it is a
"remote" of a repository on some server.
```bash
git remote add origin master git@github.com:tboudreaux/LetsLearnGit.git
```
breaking that down

	1) git remote: The subprogram in the git program you are calling
	2) add: you want to add a remote (you can have multiple or remove them)
	3) origin: call the remote you are adding origin (this is the standard name
	but it can be anything)
	4) master: the branch you are adding. master is the default branch for a
	git project, but you can make new branches, merge them, fork them, whatever
	5) URL: The URL to the remote that you are adding. In this case pulled from GitHub

Now you have told git where the remote is you can push!
```bash
git push origin master
```
Similar to above. You tell git you want to push the branch named master to the
remote named origin. Now if you check github the code will be there! The
subtelty is that you need to login. We will work on this in person cause it can
be kinda complicated to sign in. Generally thogh you should prefer to sign in
with an ssh-key rather than your username and password

Now lets say that you have been away from your computer for a couple days.
During this time its possible a collaborator pushed some code to the
repository. You could start editing like normal and then push. But then there
would be a higher likelyhood of a conflict than if you premtivly "pulled".
Pulling grabs the latest code from github and safley merges it onto your local
machine. It is always good practice to pull before you start working.
```bash
git pull origin master
```
the first time you run this you may also need to configure your git enviroment
to merge instead of rebase or fast-forward (merging is the safest and best way
to handel conflicts).
```bash
git config pull.rebase false
``` 

#### Handeling Conflicts: A n step approach
So long as you have more than one person working on a project you will
eventually encounter a merge conflict. Sometimes you will even encounter them
when you are the only person working on a project, though that is, admitedly,
much rarer. It is important to know how to handel and resolve conflicts when
they arise. Start by trying to see the world from the other codes
perspective....Oh wait, sorry I messed up my note cards. Ah yes, Okay. 

As said earlier a conflict can happen when one file is being edited by multiple
users. The first step is to avoid conflicts. Do this by having a plan about who
edits what, but also do this by having *Branches*. Branches are kind of like
sub repositories within your repository. Say you branch at commit number 5 to a
branch called "B1-MOND". In that case the branch has all the commits in its
hirtory up to and including commit number 5. However any subsequent commits to
the master branch do not affect B1-MOND. Likewise any commits to B1-MOND do not
affect the master branch. If two users are working on different parts of the
same file / codebase a good strategy is to have them working on seperate
branches and then to merge the branches all at once when the changes are done.
 
Sometimes this is simply not possible and a conflict occurs. First check which
files have conflicts
```bath
git status
```
then run
```bash
git mergetool
```
this will open a program similar to the one I mentioned before where you can
go, line by line, and merge the files. What program is entered will depend on
how your computer is set up. I use vimdiff. If you are familiar with vim I
highly recommend it, if not, it has the same steep but rewarding learning curve
that vim does.


#### Branching
I've talked a lot about "Branching" repositories. But what is this strange and
wonderful world of Branching, and does it have free muffins? Over the next few
inches of the page you are reading I will answer those two questions. Well I
already explained what Branching is in the previous section, but how do you do
it? Simple! From the root
```bash
git branch B1-MOND
git checkout B1-MOND
``` 
This firsts creates a new branch called "B1-MOND" off of whatever commit you
are on in whatever branch you are in. Then it moves you from your current
branch to that new branch. Now if you issue a commit it will go into that
branch and not the master branch. You can push to the git server simply as
```bash
git push origin B1-MOND
```
Finally, you can switch back to the master branch by running
```bash
git checkout master
```
And no, there are no free muffins. 

#### Stashing
One thing you might notice, if you checkout a branch, make some edits, dont
commit them, and try to switch back to the master branch, is that you won't be
able to. Git will tell you that you have unstashed changes. This is a saftey
mechanism so that you don't accidently delete work. If you did change back to
the master while not having commited your work that work would be gone. But
what if the work is not clean enough to put in the perminate record yet? This
is where git stash comes in.

Stashing is kinda like a temporary, single record, commit. Basically you stash,
move away, do some stuff, have a coffee, come back, and then re open the files
that are stashed. You can stash for multiple branches at once. Here is an
example of when a stash might be used and how to use it.
```bash
git checkout B1-MOND
vim src/utils.py # Do some edits to utils.py that you don't want to commit
git stash 
git checkout master
echo src/utils.py # check something in master that you may have deleted in B1-MOND
git stash pop
```
We say "pop" because the stash is whats called a "stack". This is a first in
last out datastructure. So if you stash twice when you run apply it will apply
the most recent stash. If have multiple stashes and want to apply one that is
not the most recent run
```bash
git stash pop stash@{n}
``` 
where n is the index of the stash you want to apply. You can see these indicies by running
```git
git stash list
```

#### Logging in on your UNIX-Like system
We all want to be logged into GitHub. Well, I don't know if we all want that,
but I certainly want that. Well I don't know if I want that but I know you want
that. Well I don't know if you want that but the abstracted versions of the
people that this document is aimed at want that, and if thats not a good enough
reason I don't know what is. Anyways, the best way to log into GitHub with with
an SSH key. This is a public/private key encription string that GitHub will
have part of and you will have part of. Then when you try and log in it will
valibdate and let you in. To set up SSH-key login
```bash
ssh-keygen -t ed25519 -C "your_email@example.com
```
You will have to fill in some information. Note the location where the files
are to be saved! The default location is probably something like
"/home/UserName/.ssh/id_name". You can enter a pass phase, but tbh I find it a
bother and don't. Thats probably bad security but thats a sacrifice I am
currently willing to make (The passphrase is to encrypt the key on your hard
drive, if you are not worried about people getting access to your machine,
either locally or remotly then its not nessiairy, if you are then it is).

Okay now that we have an SSH key we need to 

	1) Add it to your GitHub account
	2) Add it to your local computers identity

First, Adding to your github account. On GitHub click on your profile picture,
then settings. Once there click on "SSH and GPG keys" in the side bar. Click
"New SSH key". This will give you a text field to copy stuff into. Copy all the
contents from the .pub file (for .public) which ssh-keygen created (still
remember that save location???) and paste them into that text field. Finally,
click "Add SSH key" at the bottom and you are set there.

Now in your computer there are two ways of doing this, but one of them is
stupid, and only pillocks, so we are not going to do that way. The way that I
like is to do the following
```bash
vim ~/.ssh/config
```
There may or may not already be a file, its okay if not. Regardelss add the
following line
```bash
IdentityFile ~/.ssh/ssh_key_ed25519
```
now restart your terminal and you will be all set for the great wide world of
already being logged into a serive that you should be logged into already on.

#### Finishing Up
Git is an incredibly powerful tool. I have at the same time covered more than
you will generally need here and less than you will need. The key is to
remember that there are great resources online to help you. 

	1) https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
	2) https://git-scm.com/docs
	3) http://jonas.nitro.dk/git/quick-reference.html

Hope this helps!
