RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

clear
echo ${YELLOW}'Testing GET method: (list of objects)'${RESET}
echo ${YELLOW}'-------------------------------------\n'${RESET}
echo ${GREEN}'REQUEST:\n'${RESET}'curl -X GET\
http://127.0.0.1:8000/Cities/\n'
echo ${GREEN}'RESPONSE:'${RESET}
curl -X GET http://127.0.0.1:8000/Cities/
echo '\n'

echo ${YELLOW}'Testing GET method: (specific object)'${RESET}
echo ${YELLOW}'-------------------------------------\n'${RESET}
echo ${GREEN}'REQUEST:\n'${RESET}'curl -X GET\
http://127.0.0.1:8000/Cities/'$ARG'/\n'
echo ${GREEN}'RESPONSE:'${RESET}
curl -X GET http://127.0.0.1:8000/Cities/$ARG/
echo '\n'

echo ${YELLOW}'Testing POST method:'${RESET}
echo ${YELLOW}'-------------------\n'${RESET}
echo ${GREEN}'REQUEST:\n'${RESET}'curl --user jszabo -d\
'{"name":"Shanghai", "population":"24115000"}' \
-H "Content-Type: application/json" -X POST \
http://127.0.0.1:8000/Cities/\n'
echo ${GREEN}'RESPONSE:'${RESET}
curl --user jszabo -d \
'{"name":"Shanghai", "population":"24115000"}' \
-H "Content-Type: application/json" -X POST \
http://127.0.0.1:8000/Cities/
echo '\n'