# tiny-chess-01 entry

A 4 KB chess engine in a single `main.py` (Python 3.13, standard library
only). It plays the house gauntlet through the env at `MAKEFUN_ENV_URL`.

Engine: 0x88 board, negamax alpha-beta with iterative deepening under a
fixed 60,000-node budget per move (never a clock, fully deterministic),
transposition table (exact scores + ordering moves, cleared per move),
quiescence over captures with delta pruning, MVV-LVA and killer-move
ordering, material plus piece-square-style positional evaluation, bishop
pair and endgame king centralisation.

Grade locally from the kit directory:

    node cli/makefun.mjs grade-local --kit . --bot ../tiny-chess-01-entry --driver process --instances 1
