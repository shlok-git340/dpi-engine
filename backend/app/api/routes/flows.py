from fastapi import APIRouter

router = APIRouter(prefix="/flows")


@router.get("/")
def get_flows():
    return [
        {
            "src_ip": "192.168.1.2",
            "dst_ip": "142.250.183.14",
            "app_type": "YOUTUBE",
            "blocked": True
        }
    ]