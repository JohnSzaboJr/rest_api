YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RESET='\033[0m'

echo ${YELLOW}'Testing GET method: (list of objects)'${RESET}
echo ${YELLOW}'-------------------------------------\n'${RESET}
echo ${GREEN}'REQUEST:\n'${RESET}'curl -X GET\
http://127.0.0.1:8000/Cities/\n'
echo ${GREEN}'RESPONSE:'${RESET}
curl -X GET http://127.0.0.1:8000/Cities/
echo '\n'
read ok
