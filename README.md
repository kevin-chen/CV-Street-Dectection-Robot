virtualenv auto_car
pip install opencv-python
pip freeze > requirements.txt

cd Desktop/CV-Street-Dectection-Robot/raspberrypi/
source auto_car/bin/activate
python sandbox.py