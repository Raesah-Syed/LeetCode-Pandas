import pandas as pd
def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity['timestamp'] = activity['timestamp'].where(
        activity['activity_type'] == 'end', -activity['timestamp']
    )

    total = activity.groupby('machine_id').agg(
        process_id=('process_id', 'count'),
        timestamp=('timestamp', 'sum')
    )

    result = total['timestamp'] / (total['process_id'] / 2)

    return result.reset_index(name='processing_time').round(3)


 
  