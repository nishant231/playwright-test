def test_api(playwright):
    call = playwright.request.new_context(
        extra_http_headers={
                            "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1KRTJsd2J2RWN4Y0ZaVk9HN2NKdSJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLndlYi5xYTAxLnNoYXN0YWNsb3VkLmNvbS8iLCJzdWIiOiJhdXRoMHw2OWIwMThmMDE1MDBiYTc0NjBiZmM2ZTUiLCJhdWQiOlsiaHR0cDovL3FhMDEuc2hhc3RhLmNvbSIsImh0dHBzOi8vcWEwMS1jZ3cudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTc4MDgzMDg4OSwiZXhwIjoxNzgzNDIyODg5LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG9mZmxpbmVfYWNjZXNzIiwiYXpwIjoiYUVsdnk1WU50NXRyUzc4b1hleFgweVdiZmp1ZjhiWTIifQ.ECwy1v2C5BC8Awn8RbD07AHyFa_1EGrRaSjKvT7YJYznmDr0D_tEnWnLjc1wiQbjEV3Qntr1-11utr4M0foAf3loUDdKR81JNDI01LqcgW2DO3qaU9IyOk-QCiQBjZW_bfEAOVnz56MwKUKRZu0pG295_uUn-n2wUUV3R062YyUxnlR9jUwOcI1lpeWIhgimazz0HwQM4PhzWJsw1R2_1xJcsTQWVcysr1W2KDcPOn1Jxzx7MXF8OD8onWHC2QrTvbwDZJm0Crb_zVaXMGGBOI6c0kgszk4oyveAk5qE1vkP74HNuFACrXUJ44gfzcFjl9ocREArCdthKA_TGuCyew"}
    )
    response = call.get("https://apis.qa01.shastacloud.com/firmware/upgrade/organization/166/count?children=true")
    assert response.status == 200
    # data = response.json()
    print(response.json())
    # assert data["id"] == 1
    call.dispose()
    #assert data["title"] == "delectus aut autem"
