git checkout experimental
git pull
git checkout master
git merge experimental
rm Release/*.zip
python3 tools/release.py
git add info.json
git commit -m "New release"
git push origin master