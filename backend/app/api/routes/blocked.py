from fastapi import APIRouter

router = APIRouter(prefix="/blocked")


@router.get("/")
def get_blocked():
    return {
        "blocked_apps": [
            "YOUTUBE",
            "FACEBOOK"
        ]
    }
