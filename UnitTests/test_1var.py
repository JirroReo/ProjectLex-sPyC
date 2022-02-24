import subprocess

def run_1var():
    output = subprocess.run('python spyc.py -f UnitTests/test1var.spyc', shell=True, capture_output=True)
    print(output.stdout.decode('UTF-8'))

def test_1var(capfd):
    run_1var()
    out, err = capfd.readouterr()
    assert out == 'ERROR FOUND!\r\n\n'