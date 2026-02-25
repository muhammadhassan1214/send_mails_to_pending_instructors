import requests
from ..static import ApiEndpoints

url = "https://atlas-api-gateway.heart.org/orgManagement/v1/organisation/invites?statusList=INVITED,REQUESTED,UNALIGN_REQUEST_PENDING&roleId=17&parentId=18260"


def get_pending_requests(jwt_token):
    pending_requests = []
    response = requests.get(url, headers=ApiEndpoints.get_headers(jwt_token))
    if response.status_code == 200:
        response_data = response.json()
        raw_data = response_data.get('data', []).get('userInvitations', [])
        for data in raw_data:
            instructor_data = data.get("toUser", {})
            pending_requests.append({
                "email": instructor_data.get("emailId"),
                "name": f'{instructor_data.get("firstName")} {instructor_data.get("lastName")}'
            })
        return pending_requests
    else:
        print(f"Failed to fetch pending requests: {response.status_code} - {response.text}")
        return []
