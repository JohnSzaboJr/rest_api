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
echo ${GREEN}'REQUEST:\n'${RESET}'curl --user jszabo \
-X POST -S \
-H 'Accept: application/json' \
-F "name=Miami" -F "population=5502379" \
-F "photo=@miami.jpeg;type=image/jpg" \
http://127.0.0.1:8000/Cities/'
echo ${GREEN}'RESPONSE:'${RESET}
curl --user jszabo \
-X POST -S \
-H 'Accept: application/json' \
-F "name=Miami" -F "population=5502379" \
-F "photo=@miami.jpeg;type=image/jpg" \
http://127.0.0.1:8000/Cities/
echo '\n'

echo ${YELLOW}'Testing PUT method:'${RESET}
echo ${YELLOW}'------------------\n'${RESET}
echo ${GREEN}'REQUEST:\n'${RESET}'curl --user jszabo \
-X PUT -S \
-H 'Accept: application/json' \
-F "name=New York" -F "population=8,175,133"
http://127.0.0.1:8000/Cities/11/'
echo ${GREEN}'RESPONSE:'${RESET}
curl --user jszabo \
-X PUT -S \
-H 'Accept: application/json' \
-F "name=New York" -F "population=8175133" \
http://127.0.0.1:8000/Cities/11/
echo '\n'

echo ${YELLOW}'Testing DELETE method:'${RESET}
echo ${YELLOW}'----------------------\n'${RESET}
echo ${GREEN}'REQUEST:\n'${RESET}'curl --user jszabo \
-X DELETE http://127.0.0.1:8000/Cities/10/ && \
curl -X GET http://127.0.0.1:8000/Cities/10/'
echo ${GREEN}'RESPONSE:'${RESET}
curl --user jszabo \
-X DELETE http://127.0.0.1:8000/Cities/10/ && \
curl -X GET http://127.0.0.1:8000/Cities/10/
echo '\n'