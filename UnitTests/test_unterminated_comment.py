import subprocess

def run_unterminated_comment():
    output = subprocess.run('python spyc.py -f UnitTests/testUnterminatedComment.spyc', shell=True, capture_output=True)
    print(output.stdout.decode('UTF-8'))

def test_unterminated_comment(capfd):
    run_unterminated_comment()

    out, err = capfd.readouterr()
    assert out == 'ERROR FOUND!\r\n\n'