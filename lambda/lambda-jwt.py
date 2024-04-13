import json, jwt, uuid, os, datetime

CLIENT_ID = os.environ["CLIENT_ID"]
SECRET_ID = os.environ["SECRET_ID"]
SECRET = os.environ["SECRET"]

def lambda_handler(event, context):
    content = event.get('queryStringParameters')
    username = json.dumps(content['username']).strip('"')

    token = jwt.encode(
        {
            "iss": CLIENT_ID,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": username,
            "scp": ["tableau:views:embed", "tableau:insights:embed"]
        },
        SECRET,
        algorithm="HS256",
        headers={
            'kid': SECRET_ID,
            'iss': CLIENT_ID
        }
    )
    
    return token