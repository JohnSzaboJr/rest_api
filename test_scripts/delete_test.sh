YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

clear
echo ${YELLOW}'Testing DELETE method:'${RESET}
echo ${YELLOW}'----------------------\n'${RESET}
echo "Id# to delete:"
read varid
echo "Name:"
echo ${GREEN}'REQUEST:\n'${RESET}'curl --user jszabo \
-X DELETE http://127.0.0.1:8000/Cities/'$varid'/ && \
curl -X GET http://127.0.0.1:8000/Cities/'$varid'/'
echo ${GREEN}'RESPONSE:'${RESET}
curl --user jszabo \
-X DELETE http://127.0.0.1:8000/Cities/$varid/ && \
curl -X GET http://127.0.0.1:8000/Cities/$varid/
echo '\n'
echo 'Do you want to delete more? (Y/N)'
read ans
if [ $ans = "Y" ]; then
    sh delete_test.sh
fi