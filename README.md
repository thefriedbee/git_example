# Git management

## Three strategies
- merge
- rebase
- stash

## Review
- basic operation
- create repository


## Task 1. Start a new project
1. `git init`
2. `git branch --all` or `git branch -a`
3. Edit a file
4. `git add README.md`
5. `git commit -m "init project"`
6. Open git tab
7. Change default editor
   1. `git config --global core.editor "nano"`


## Task 2. Create branch & Push to remote website
1. `git remote add origin YOUR_REMOTE_LINK_NAME`
2. `git branch -m main`
3. `git push -u origin main`


## Task 3. Create new branchs to develop code
1. Create new branch
   1. `git branch feature1`
   2. `git checkout freature1`
2. Quicker way:
   1. `git checkout -b 'feature1'`
3. Standard operation
   1. `git add`
   2. `git commit -m "edit message"`
4. `git checkout main`


## Task 4. Merge branches
1. `git checkout main`
2. `git merge feature1 --no-ff`


## Task 5. Git rebase
1. `git checkout 'feature1'`
2. `git rebase main`
3. manually fix conflict:
   1. `git rebase --continue`
4. Note: Don't rebase after branches are uploaded remotely


## Task 6. Git Stash, reset, amend
1. store edits
   1. `git stash`
2. find the good branch
3. get results
   1. `git stash pop`
4. reset last commit
   1. git reset: `git reset --soft HEAD~1`
5. amend message: `git commit --amend -m "new message"`


## Task 7. Git Squash
1. Squash between branches `git merge --squash feature1`
   1. Can select that in Github
2. Squash last n commits
   1. `git reset --soft HEAD~3`
   2. `git commit`
   3. Interactively rebase the last n commits: `GIT_EDITOR=nano git rebase -i HEAD~n`


## Task 8. Undo staged file
Undo add (staged file)
- Use IDE key
- `git reset <file>`
- `git restore --staged <file>`


## Task 9. Pushed results to remote branch
- `git push origin main`
- Preview graph: `git log --oneline --graph`

The above includes basic operations within local reporsitory.


Thanks for watching!


