sudo mount /dev/sda1 /files
file="/files/DO-NOT-DELETE.txt"
if [ -e $file ]
then
  echo $file
  rsync -avh /files/ /home/pi/poem-printer/files/ --delete
fi