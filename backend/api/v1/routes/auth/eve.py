from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse
import os
import requests
from urllib.parse import urlencode
import json
import jwt  # For parsing JWT tokens
from src.services.eve_service import eve_service

router = APIRouter()

# EVE Online SSO configuration
EVE_SSO_AUTH_URL = "https://login.eveonline.com/v2/oauth/authorize"
EVE_SSO_TOKEN_URL = "https://login.eveonline.com/v2/oauth/token"
EVE_SSO_CLIENT_ID = os.getenv("EVE_ONLINE_CLIENT_ID")
EVE_SSO_CLIENT_SECRET = os.getenv("EVE_ONLINE_CLIENT_SECRET")
EVE_SSO_REDIRECT_URI = os.getenv("EVE_ONLINE_REDIRECT_URI", "http://localhost:8000/api/v1/auth/eve/callback")

# Scopes required for character information
EVE_SCOPES = "esi-characters.read_character_attributes.v1 esi-characters.read_corporation.v1 esi-characters.read_faction.v1 esi-characters.read_medals.v1 esi-characters.read_standings.v1"

@router.get("/login")
async def eve_login():
    """Initiate EVE Online SSO login"""
    if not EVE_SSO_CLIENT_ID or not EVE_SSO_CLIENT_SECRET:
        raise HTTPException(status_code=500, detail="EVE Online authentication credentials not configured")
    
    # Prepare authorization parameters
    params = {
        'response_type': 'code',
        'redirect_uri': EVE_SSO_REDIRECT_URI,
        'client_id': EVE_SSO_CLIENT_ID,
        'scope': EVE_SCOPES,
        'state': 'some_random_state_value'  # In a real app, use crypto-random values and validation
    }
    
    # Construct the authorization URL
    auth_url = f"{EVE_SSO_AUTH_URL}?{urlencode(params)}"
    
    return RedirectResponse(url=auth_url)

@router.get("/callback")
async def eve_callback(request: Request, code: str, state: str):
    """Handle EVE Online SSO callback and exchange code for tokens"""
    if not EVE_SSO_CLIENT_ID or not EVE_SSO_CLIENT_SECRET:
        raise HTTPException(status_code=500, detail="EVE Online authentication credentials not configured")
    
    # Prepare token exchange parameters
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
    }
    
    # Authenticate with client credentials
    response = requests.post(
        EVE_SSO_TOKEN_URL,
        data=token_data,
        auth=(EVE_SSO_CLIENT_ID, EVE_SSO_CLIENT_SECRET)
    )
    
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to exchange authorization code for tokens")
    
    token_response = response.json()
    
    # Extract character ID from the access token (JWT)
    try:
        # Decode JWT without verification for getting the character ID
        decoded_token = jwt.decode(
            token_response["access_token"], 
            options={"verify_signature": False}
        )
        
        # The character ID is in 'sub' field with format: "CHARACTER:EVE:<character_id>"
        character_id = int(decoded_token.get("sub", "").split(":")[-1])
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to decode access token for character ID")
    
    # Return the access token and character information
    return {
        "access_token": token_response["access_token"],
        "expires_in": token_response["expires_in"],
        "token_type": token_response["token_type"],
        "refresh_token": token_response["refresh_token"],
        "character_id": character_id
    }

@router.get("/character-info")
async def get_character_info(access_token: str, character_id: int):
    """Get detailed information about a character by ID"""
    try:
        # We need to fetch the character_id from the ESI token - this requires more complex handling
        return eve_service.get_character_info(access_token, character_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch character info: {str(e)}")

@router.get("/character-attributes")
async def get_character_attributes(access_token: str, character_id: int):
    """Get character's attributes"""
    try:
        return eve_service.get_character_attributes(access_token, character_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch character attributes: {str(e)}")

@router.get("/character-corporation")
async def get_character_corporation(access_token: str, character_id: int):
    """Get character's corporation info"""
    try:
        return eve_service.get_character_corporation(access_token, character_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch character corporation: {str(e)}")
