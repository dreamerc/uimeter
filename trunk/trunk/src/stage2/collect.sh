a=$(date +%Y/%m/%d_%H:%M)
cd testway1
python link.py
cd ../testway2/
python link.py
cd ../pygame/
python run.py
cd ..
mkdir $a
mkdir $a/testway1
mv testway1/*csv $a/testway1/.
mv -rf testway1/screenshot $a/testway1/.
mkdir $a/testway2
mv testway2/*csv $a/testway2/.
mv -rf testway2/screenshot $a/testway2/.
mkdir $a/pygame
mv pygame/*csv $a/pygame/.
mv pygame/*dat $a/pygame/.
mv -rf pygame/screenshot $a/pygame/.
echo 'done'
