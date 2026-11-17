import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    x = len(friend_request[['sender_id', 'send_to_id']].drop_duplicates())
    y = len(request_accepted[['requester_id', 'accepter_id']].drop_duplicates())
    rate = 0.00 if x == 0 else round((y * 1.0) / x, 2)
    return pd.DataFrame({'accept_rate': [rate]})