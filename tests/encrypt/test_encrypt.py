import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("teste", 3) == "set_et"
    assert encrypt_message("teste", 4 ) == "e_tset"
    assert encrypt_message("teste", 6) == "etset"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", "")
    
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(10, 1)