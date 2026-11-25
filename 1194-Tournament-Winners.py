import pandas as pd

def tournament_winners(players: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:

    a = matches[['first_player', 'first_score']].rename(
        columns={'first_player': 'player_id', 'first_score': 'score'}
    )

    b = matches[['second_player', 'second_score']].rename(
        columns={'second_player': 'player_id', 'second_score': 'score'}
    )

    g = pd.concat([a, b]).groupby('player_id', as_index=False)['score'].sum()

    g = players.merge(g, on='player_id', how='left').fillna({'score': 0})

    g = g.sort_values(['group_id', 'score', 'player_id'],
                      ascending=[True, False, True])

    return g.drop_duplicates('group_id')[['group_id', 'player_id']]