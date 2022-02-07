docker builder prune -f -a
docker build -t locchan:haruka -f Docker/Dockerfile .
RESULT=$?
docker builder prune -f -a
exit $RESULT