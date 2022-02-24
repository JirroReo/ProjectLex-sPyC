import subprocess

def run_correct():
    output = subprocess.run('python spyc.py -f UnitTests/testCorrectAll.spyc', shell=True, capture_output=True)
    print(output.stdout.decode('UTF-8'))

def test_correct(capfd):
    run_correct()
    out, err = capfd.readouterr()
    assert out == 'OK!\r\n\n'