from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import requests
from ..config import settings
from .models import UserToken, RoleEnum

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# For a real implementation, you'd fetch the public key from Keycloak
# e.g., requests.get(f"{settings.KEYCLOAK_URL}realms/{settings.KEYCLOAK_REALM}").json()['public_key']
# Here we mock it or bypass it if dev mode is enabled.

async def get_current_user(token: str = Security(oauth2_scheme)) -> UserToken:
    if settings.AUTH_DEV_MODE:
        return UserToken(username="dev_user", roles=[RoleEnum.ANALYST, RoleEnum.DDMA_OFFICER])
    
    try:
        # In a real setup, verify with the keycloak public key and audience
        # payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"], audience=settings.KEYCLOAK_CLIENT_ID)
        payload = {"preferred_username": "real_user", "realm_access": {"roles": ["analyst"]}}
        
        username: str = payload.get("preferred_username")
        realm_access = payload.get("realm_access", {})
        roles = realm_access.get("roles", [])
        
        user_roles = []
        if "analyst" in roles:
            user_roles.append(RoleEnum.ANALYST)
        if "ddma_officer" in roles:
            user_roles.append(RoleEnum.DDMA_OFFICER)
            
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid auth credentials")
            
        return UserToken(username=username, roles=user_roles)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid auth credentials")

def require_role(required_role: RoleEnum):
    async def role_checker(user: UserToken = Depends(get_current_user)):
        if required_role not in user.roles:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return user
    return role_checker
