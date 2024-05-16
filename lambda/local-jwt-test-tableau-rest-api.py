import json, jwt, uuid, os, datetime, requests

# logging
import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

CLIENT_ID = os.environ["CLIENT_ID"]
SECRET_ID = os.environ["SECRET_ID"]
SECRET = os.environ["SECRET"]
SERVER = "https://10ax.online.tableau.com"
SITE = "rcgsepulse"
API_VERSION = "3.22"
HEADERS = {
    'accept': 'application/json',
    'content-type': 'application/json'
}

def create_jwt(username):

    token = jwt.encode(
        {
            "iss": CLIENT_ID,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            "jti": str(uuid.uuid4()),
            "aud": "tableau",
            "sub": username,
            "scp": ["tableau:insights:embed"]
            # "scp": ["tableau:insights_summary:read"]
            # "scp": ["tableau:content:read", "tableau:views:download", "tableau:insights:embed", "tableau:insight_definitions:create", "tableau:insight_definitions_metrics:read", "tableau:insight_definitions:delete", "tableau:insight_definitions:update", "tableau:insights_summary:read", "tableau:insights:read", "tableau:insight:read", "tableau:insight_metrics:create", "tableau:insight_metrics:delete", "tableau:insight_metrics:read", "tableau:insight_metrics:update", "tableau:insight_metrics:create", "tableau:metric_subscriptions:create", "tableau:metric_subscriptions:read", "tableau:metric_subscriptions:delete", "tableau:metric_subscriptions:update", "tableau:metric_subscriptions:create"]
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

def auth_rest_api(jwt):

    ts_url = "{server}/api/{api_version}/auth/signin".format(server=SERVER, api_version=API_VERSION)
    body = { "credentials": {'jwt': jwt, "site": {"contentUrl": SITE}} }


    try:
        r = requests.post(ts_url, json= body, headers=HEADERS, verify=False)
        if r.status_code == 200:
            logger.info('successful sign-in, received status code of {}'.format(str(r.status_code)))
            response_auth = json.loads(r.content)
            logger.info(json.dumps(response_auth, indent=4))
            ts_site_luid = response_auth["credentials"]["site"]["id"]
            ts_auth_token = response_auth["credentials"]["token"]
            ts_user_luid = response_auth["credentials"]["user"]["id"]
            return ts_auth_token
        else:
            logger.error('sign-in failed, received status code of {}'.format(str(r.status_code)))
            logger.error(r.text)
            raise SystemExit('sign-in failed, received status code of {}'.format(str(r.status_code)))

    except requests.exceptions.RequestException as e: 
        logger.error(e)
        raise SystemExit(e)  

def get_users(rest_token):

    ts_url = "{server}/vizportal/api/web/v1/getUsers".format(server=SERVER)
    HEADERS['X-tableau-auth'] = rest_token
    body = {
            "method": "getUsers",
            "params": {
                "page": {
                    "startIndex": 0,
                    "maxItems": 30
                },
                "filter": {
                    "operator": "and",
                    "clauses": [
                        {"operator": "matches", "value": "an"}
                    ]
                },
                "order": [],
                "statFields": []
            }
    }



    try:
        r = requests.post(ts_url, json= body, headers=HEADERS, verify=False)
        if r.status_code == 200:
            logger.info('successful sign-in, received status code of {}'.format(str(r.status_code)))
            response_auth = json.loads(r.content)
            logger.info(json.dumps(response_auth, indent=4))
            ts_site_luid = response_auth["credentials"]["site"]["id"]
            ts_auth_token = response_auth["credentials"]["token"]
            ts_user_luid = response_auth["credentials"]["user"]["id"]
            return ts_auth_token
        else:
            logger.error('sign-in failed, received status code of {}'.format(str(r.status_code)))
            logger.error(r.text)
            raise SystemExit('sign-in failed, received status code of {}'.format(str(r.status_code)))

    except requests.exceptions.RequestException as e: 
        logger.error(e)
        raise SystemExit(e)  
    

def get_pulse_insights_summarization_strategy_digest(api_token):
    # url = "https://us-west-2a.online.tableau.com/api/-/pulse/insights/summaries/SUMMARIZATION_STRATEGY_DIGEST"
    

    url = "{server}/api/-/pulse/insights/summaries/SUMMARIZATION_STRATEGY_DIGEST".format(server=SERVER)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Tableau-Auth": api_token
    }

    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()  # Raises for http 4xx, 5xx

        data = resp.json()
        print(data)
        return data

    except requests.exceptions.HTTPError as http_err:
        logger.error(f'HTTP error occurred: {http_err}') 
        return {'error': str(http_err)}
    except Exception as err:
        logger.error(f'Other error occurred: {err}')  
        return {'error': str(err)}

jwt = create_jwt('jcraycraft@salesforce.com')
rest_auth_token = auth_rest_api(jwt)
get_users(rest_auth_token)
# get_pulse_insights_summarization_strategy_digest(rest_auth_token)

