# tic tac toe api

- This API is used by my tic tac toe react app game
- API is available here https://tic-tac-toe-api-356923.ue.r.appspot.com/
- It has one endpoint POST /api/get-move -
- payload: { board: 3 x 3 array of X's and O's, player: the player whose move you want to get, difficulty: the difficulty level of the AI, 1-easy,2-medium,3-hard,4-impossible }
- payload example: {
    "board": [
        [
            "",
            "X",
            ""
        ],
        [
            "",
            "O",
            ""
        ],
        [
            "",
            "",
            "X"
        ]
    ],
    "difficulty": 4,
    "player": "O"
}
- example response: {"data": {"position": 6, "coordinates": [1, 2]}}
- position is the position of the move in a board numbered like this [[1,2,3],[4,5,6],[7,8,9]] and the coordinates are the row and column (zero-indexed) in a 3x3 array. Note that position and coordinates communicate the same information in different formats

### Implementation Details
- Easy, Medium, and Impossible difficulties are all based on variations of the minimax algorithm
- Hard mode is using OpenAI's GPT-3 which was trained on data from impossible mode
