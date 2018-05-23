# Broken challenge response handshake
- user has to authenticate to get the flag
- user does not have the shared secret
- broken: first the backend authenticates for a user supplied challenge

# Solution
1. create connection 1: send garbage challenge (we don't neet it) 
2. get challenge to authenticate to get the flag (connection 1)
2. create connection 2 and ask the backend for the valid response for the challenge we have to solve

# Deployment
docker build --rm -t challenge-response .  
docker run --name cr1 -p 2023:2023 challenge-response  

# Exploit
python exploit.py  
