#!/bin/bash

#kill all existing tmux sessions
tmux kill-server

#cd into project folder
cd /root/project-ssquad-sally

#ensure git repo inside VPS has latest changes from main branch on GitHub
git fetch && git reset origin/main --hard

#enter python virtual env + install python dependencies
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

#start new detached tmux session
tmux new -d -s portfolio 'cd /root/project-ssquad-sally && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
