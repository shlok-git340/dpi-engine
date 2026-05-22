from fastapi import APIRouter

router = APIRouter(prefix="/stats")


@router.get("/")
def get_stats():
    return {
        "total_packets": 10234,
        "blocked": 123,
        "top_protocol": "TCP"
    }
