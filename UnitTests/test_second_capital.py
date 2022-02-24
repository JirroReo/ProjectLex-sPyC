import subprocess

def run_second_capital():
    output = subprocess.run('python spyc.py -f UnitTests/testSecondCapital.spyc', shell=True, capture_output=True)
    print(output.stdout.decode('UTF-8'))

def test_second_capital(capfd):
    run_second_capital()
    out, err = capfd.readouterr()
    assert out == 'OK!\r\n\n'