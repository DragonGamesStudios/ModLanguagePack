git checkout future
git pull
git checkout master
git pull
git merge future
rm Release/*.zip
python3 tools/tracker.py
git commit -m "New release"
git push origin master
git checkout future