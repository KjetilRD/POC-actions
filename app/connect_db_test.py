import connect_db

def test_file1_method1():
    rs = connect_db.connect()

    assert rs is not None, "no resultset"
    assert len(rs) > 0, "no rows in resultset"
    assert len(rs[0]) == 1, "1 column is resultset"


def test_file1_method2():
    x = 5
    y = 6
    assert x+1 == y, "test failed"
