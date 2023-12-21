def tournament_winner(competitions=list, results=list):
    scores = {}
    for game_round in range(len(results)):
        winner_of_round = competitions[game_round][0] if results[game_round] == 1 else competitions[game_round][1]
        if winner_of_round in scores:
            scores[winner_of_round] = scores[winner_of_round] + 3
        else:
            scores[winner_of_round] = 3
    print(scores.get)
    final_winner = max(scores, key=scores.get)
    print(final_winner)
    return final_winner



if __name__ == '__main__':
    # [hometeam, awayteam]
    # 1 means hometeam won, 0 means away team won.
    competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
    ]

    results = [0, 1, 1]

    tournament_winner(competitions, results)
