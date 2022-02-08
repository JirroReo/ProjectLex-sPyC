import subprocess, io

def run_spyc():
    output = subprocess.run('python shell.py -f testDT.spyc -o pytestOutput', shell=True, capture_output=True)
    print(output.stdout.decode('UTF-8'))

def test_spyc():
    run_spyc()

    assert list(io.open('pytestOutput.txt')) == list(io.open('symbolTable.txt'))
    