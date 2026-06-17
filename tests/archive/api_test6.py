def test_status(api_post):
    assert api_post.status_code == 200

def test_ma_title(api_post):
    assert "title" in api_post.json()