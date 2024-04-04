echo "BUILD START"
python3.10.12 -m pip install -r requirements.txt
python3.10.12 manage.py collectstatic --noinput --clear
echo "BUILD END"