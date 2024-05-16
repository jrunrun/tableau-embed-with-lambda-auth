import json, jwt, uuid, os, datetime

CLIENT_ID = os.environ["CLIENT_ID"]
SECRET_ID = os.environ["SECRET_ID"]
SECRET = os.environ["SECRET"]

def lambda_handler(username):

    token = jwt.encode(
        {
            "iss": CLIENT_ID,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": username,
            # "scp": ["tableau:views:embed", "tableau:insights:embed"],
            "scp": ["tableau:views:embed"],
            "Region": ["East", "South"],
            "https://tableau.com/oda": "true",
            "https://tableau.com/groups": ["justinOnDemandGroup"]
        },
        SECRET,
        algorithm="HS256",
        headers={
            'kid': SECRET_ID,
            'iss': CLIENT_ID
        }
    )

    print(token)
    
    return token

lambda_handler('j@j.com')

