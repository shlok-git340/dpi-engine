from app.database.models import FlowRecord


def save_flow(db, flow_data):
    flow = FlowRecord(**flow_data)

    db.add(flow)
    db.commit()
