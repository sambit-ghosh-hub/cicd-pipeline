cd ..
cd flask-hello-world
git pull
kill -9 $(lsof -t -i:5001)
python app.py