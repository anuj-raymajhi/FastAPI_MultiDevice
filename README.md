# Run method
load server.py in a device where you want to run a service
  `server : uvicorn server:app --host 0.0.0.0 --port 8001 --reload`
run client.py in a device which would want to request a service from server : put the server IP address in appropriate place
  `python .\client.py`
