# Setup backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mkdir data
mkdir images
deactivate
cd ..

# Setup frontend
cd frontend
nvm use 21.5.0
npm install
cd ..