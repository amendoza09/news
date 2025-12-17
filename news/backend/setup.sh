echo "downloading dependancies"

python3 -m venv venv
source venv/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt

python3 -m textblob.donwload_corpora
python3 -m spacy download en_core_web_sm

echo "downloads complete!"