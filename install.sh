echo "Creating directory..."
sleep 1
mkdir ~/RPS
echo "Directory created at ~/RPS"
sleep 0.5
echo "Downloading python script..."
sleep 1
cd ~/RPS && wget https://raw.githubusercontent.com/Daktoo/rock-paper-scissors/refs/heads/master/rps.py
sleep 1
echo "Python script downloaded successfully."
sleep 0.5
echo "Running the script using Python3..."
sleep 1
python3 ~/RPS/rps.py || echo "Failed to execute the python script. Please check that Python3 is installed on your system."
