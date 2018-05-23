docker build --rm -t challenge-response .
docker run --name cr1 -p 2023:2023 challenge-response
python exploit.py
