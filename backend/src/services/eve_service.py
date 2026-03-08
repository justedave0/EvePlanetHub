from esipy import EsiApp, EsiClient
from esipy.exceptions import APIException
import os
from typing import Dict, Any, Optional
from fastapi import HTTPException
import httpx
import jwt  # For parsing JWT tokens when needed

class EVEOnlineService:
    def __init__(self):
        # Initialize ESI app with the appropriate region
        self.esi_app = EsiApp()
        
        # Use a client that's pre-configured for authentication 
        self.client = EsiClient(
            universe='singularity',
            cache=None,
            headers={'User-Agent': 'EvePlanetHub/1.0'}
        )
    
    def get_character_info(self, access_token: str, character_id: int) -> Dict[str, Any]:
        """
        Get detailed information about a character using their access token
        """
        try:
            # Update the client with the access token for authentication
            self.client.update_token(token={
                'access_token': access_token,
                'expires_in': 3600,  # 1 hour
                'token_type': 'Bearer'
            })
            
            # Get character info using ESI API
            response = self.client.req(
                url='/v5/characters/{character_id}/',
                path={'character_id': character_id}
            )
            
            return response.data
            
        except APIException as e:
            raise HTTPException(status_code=400, detail=f"ESI API Error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to fetch character info: {str(e)}")
    
    def get_character_attributes(self, access_token: str, character_id: int) -> Dict[str, Any]:
        """
        Get character attributes
        """
        try:
            self.client.update_token(token={
                'access_token': access_token,
                'expires_in': 3600,
                'token_type': 'Bearer'
            })
            
            response = self.client.req(
                url='/v1/characters/{character_id}/attributes/',
                path={'character_id': character_id}
            )
            
            return response.data
            
        except APIException as e:
            raise HTTPException(status_code=400, detail=f"ESI API Error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to fetch character attributes: {str(e)}")
    
    def get_character_corporation(self, access_token: str, character_id: int) -> Dict[str, Any]:
        """
        Get character's corporation info
        """
        try:
            self.client.update_token(token={
                'access_token': access_token,
                'expires_in': 3600,
                'token_type': 'Bearer'
            })
            
            response = self.client.req(
                url='/v2/characters/{character_id}/corporation/',
                path={'character_id': character_id}
            )
            
            return response.data
            
        except APIException as e:
            raise HTTPException(status_code=400, detail=f"ESI API Error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to fetch character corporation: {str(e)}")

# Global service instance
eve_service = EVEOnlineService()