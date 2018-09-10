YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

clear
echo ${YELLOW}'Testing GET method: (specific object)'${RESET}
echo ${YELLOW}'-------------------------------------\n'${RESET}
echo "Id#:"
read varid
echo ${GREEN}'REQUEST:\n'${RESET}'curl -X GET\
http://127.0.0.1:8000/Cities/'$varid'/\n'
echo ${GREEN}'RESPONSE:'${RESET}
curl -X GET http://127.0.0.1:8000/Cities/$varid/
echo '\n'
echo 'Do you want to get more items? (Y/N)'
read ans
if [ $ans = "Y" ]; then
    sh get_test2.sh
fi