tar xf roberta.tar.xz
yes '' | ssh-keygen -t ed25519 -b 4096
pip install -r requirements.txt
ssh -oStrictHostKeyChecking=no -R 80:localhost:5000 localhost.run & python app.py
