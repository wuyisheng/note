
# git note

A note base on git , for make a commitment to life.

# getting start

## step 0: install require software

```bash
brew install git
brew install python
```

## step 1 : create git repo

```bash
cd ${you_path_to_git}
git init --bare yeshen_git_note.git
# Initialised empty Git repository in /home/ys_t7/Downloads/tmp/yeshen_git_note.git/
#
# If you already have one repo, change it using following command:
# $ git clone https://github.com/wuyisheng/note.git
# $ git remote add origin yeshen@192.168.0.1:${you_path_to_git}/yeshen_git_note.git
```

## step 2 : accept git repo at another device

```bash
git clone yeshen@192.168.0.1:${you_path_to_git}/yeshen_git_note.git
```


## step 3 : commit note to repo

```bash
python note.py
```

