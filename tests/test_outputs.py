from src.outputs import hello

def test_std_output(capsys):
    hello("Gaurav")
    stdout, stderr = capsys.readouterr()
    assert stdout == "Hello Hello Gaurav\n"