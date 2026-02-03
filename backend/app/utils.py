import uuid
from datetime import datetime

def generate_serial_number():
    timestamp = datetime.now().strftime("%Y%m%d")
    unique = uuid.uuid4().hex[:8].upper()
    return f"SN-{timestamp}-{unique}"

def generate_asset_tag():
    unique = uuid.uuid4().hex[:6].upper()
    return f"AT-{unique}"

def generate_loan_id(net_id: str, asset_tag: str):
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    return f"LN-{net_id}-{asset_tag}-{timestamp}"