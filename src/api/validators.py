def validate_token_response(data):
    assert "token" in data
    assert isinstance(data["token"], str)

def validate_user_object(data):
    assert "id" in data
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
