def validate_token_response(body):
    """
    Validates that the response body contains
    a valid token structure.
    """

    assert isinstance(body, dict), "Response body must be a dictionary"

    assert "token" in body, "Missing 'token' in response"

    assert isinstance(body["token"], str), "Token must be a string"

    assert body["token"], "Token must not be empty"
