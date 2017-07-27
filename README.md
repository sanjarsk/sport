# sport

project root - project directory
`python3 -m venv <env_name>`
`source bin/activate`

`git clone https://github.com/sanjarsk/sport.git`

or

`git clone git@github.com:sanjarsk/sport.git`

then
`git checkout develop`
and start work from new branch

to publish code to corresponding branch in repository:
`git push`

to publish new branch to repository:
`git push -u origin <new_branch name>`

install dependencies with:
`pip install -r requirements.txt`

to add new dependencies for projects use:
`pip freeze > requirements.txt` in root

For window users
`python.exe manage.py runserver 0.0.0.0:8000`
