##############################################################################
# clone, keycmd, github, project.
cd ~/projects
git clone git@github.com:iogf/keycmd.git keycmd-code
##############################################################################
# delete, remove, clean, *.pyc files, keycmd.
cd /home/tau/projects/keycmd-code/
find . -name "*.pyc" -exec rm -f {} \;
##############################################################################
# push, keycmd.
cd ~/projects/keycmd-code
git status
git add *
git commit -a
git push 
##############################################################################
# undo, fix, changes, keycmd.
cd ~/projects/keycmd-code
git checkout *
##############################################################################
# create, development, branch, keycmd.
cd /home/tau/projects/keycmd-code
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# install, keycmd.
sudo bash -i
cd /home/tau/projects/keycmd-code
python2 setup.py install
rm -fr build
exit
##############################################################################
# remove, delete, .keycmd, tau, startup, configuration, file.
rm -fr ~/.keycmd/
##############################################################################
# check, preview, keycmd, README.md, markdown, tool, html, turn, convert.
markdown README.md > README.html
google-chrome README.html
rm README.html
##############################################################################
# keycmd, pip.
cd ~/projects/keycmd-code
# need a setup.cfg.
python setup.py sdist register upload
rm -fr sdist
##############################################################################
# update, backup, keycmd, .keycmd, .cmdrc.

rm -fr /home/tau/projects/esc-code/keycmd
cp -R /home/tau/.keycmd /home/tau/projects/esc-code/keycmd

##############################################################################
# create, vy, desktop, entry, xdg-open, keycmd.
xdg-mime query filetype setup.py

cd ~/.local/share/applications/

echo '
[Desktop Entry]
Name=vy
Exec=/usr/bin/vy
MimeType=text/plain
Icon=vy
Terminal=false
Type=Application
' > ~/.local/share/applications/vy.desktop
vy ~/.local/share/applications/vy.desktop
xdg-open setup.py

update-desktop-database ~/.local/share/applications
xdg-mime default vy.desktop text/html 
##############################################################################
# check for Key-r.
grep -r -l "<Key-r>" .
##############################################################################
# merge development into master.
cd /home/tau/projects/keycmd-code/
git checkout master
git merge development
git push
git checkout development


