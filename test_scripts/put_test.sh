YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

clear
echo ${YELLOW}'Testing PUT method:'${RESET}
echo ${YELLOW}'------------------\n'${RESET}
echo "Id# to update:"
read varid
echo "Name:"
read varname
echo "Population:"
read varpopulation
echo "Photo path:"
read varphoto
echo ${GREEN}'REQUEST:\n'${RESET}'curl --user jszabo \
-X PUT -S \
-H 'Accept: application/json' \
-F "name='$varname'" -F "population='$varpopulation'" \
-F "photo=@'$varphoto';type=image/jpg" \
http://127.0.0.1:8000/Cities/'$varid'/'
echo ${GREEN}'RESPONSE:'${RESET}
curl --user jszabo \
-X PUT -S \
-H 'Accept: application/json' \
-F "name=$varname" -F "population=$varpopulation" \
-F "photo=@$varphoto;type=image/jpg" \
http://127.0.0.1:8000/Cities/$varid/
echo '\n'
echo 'Do you want to update more? (Y/N)'
read ans
if [ $ans = "Y" ]; then
    sh put_test.sh
fi