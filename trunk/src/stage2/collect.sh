a=$(date +%Y%m%d_%H:%M)
cd testway1
python link.py
rm *pyc
cd ../testway2/
python link.py
rm *pyc
cd ../pygame/
python run.py
rm *pyc
cd ..
mkdir $a
mkdir $a/testway1
mv testway1/*csv $a/testway1/.
cp -rf testway1/screenshot $a/testway1/.
rm testway1/screenshot/*
mkdir $a/testway2
mv testway2/*csv $a/testway2/.
cp -rf testway2/screenshot $a/testway2/.
rm testway2/screenshot/*
mkdir $a/pygame
mv pygame/*csv $a/pygame/.
mv pygame/*dat $a/pygame/.
cp -rf  pygame/screenshot $a/pygame/.
rm pygame/screenshot/*
echo 'done'
