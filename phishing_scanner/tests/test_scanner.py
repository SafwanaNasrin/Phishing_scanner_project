from scanner import has_ip_address, is_shortened_url

def test_ip():
    assert has_ip_address("192.168.1.1") == True

def test_short_url():
    assert is_shortened_url("bit.ly") == True
