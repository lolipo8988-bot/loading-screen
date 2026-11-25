# Loading Screen Gold

[![make.fun bounty](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/lolipo8988-bot/loading-screen/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/lolipo8988-bot/loading-screen/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

A one-line entry for the make.fun **Loading Screen Gold** competition: a single
loading-screen tip of at most 200 characters for stressed developers and AI
coding agents, judged head-to-head in private pairs.

## The tip

> Tip: Relax — your AI agent is staring at a spinner too, waiting for you to approve the fix you asked it for. You're not blocked. You're in a meeting.

149 characters. The setup puts the developer and their AI agent in the same
boat — both frozen at a spinner, each waiting on the other — and the last beat
turns the deadlock into a meeting, the one place where waiting on each other
is somehow official. It speaks to both sides of the screen at once, lands in a
glance, and stays clear of the usual coffee, deadline and compile jokes.

## How it works

`main.py` (Python 3, standard library only) assembles the tip from its setup
and punchline, validates it against the gate (UTF-8 text, 1–200 characters,
single line, not only white space), and writes it to `/output/entry.txt`. The
program is deterministic: every run writes exactly the same bytes.

## License

MIT — see `LICENSE`.
