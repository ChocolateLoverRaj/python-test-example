import subprocess

def test_subprocess():
    output = subprocess.run(["python3", "main.py"], capture_output=True).stdout.decode("utf-8").strip()
    assert output == "Hello from python-test!"
