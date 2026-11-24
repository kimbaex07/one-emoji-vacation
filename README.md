# One Emoji, One Dream Vacation

[![make.fun · u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/kimbaex07/one-emoji-vacation/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/kimbaex07/one-emoji-vacation/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35?utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for [One Emoji, One Dream Vacation](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) on make.fun — one emoji, nothing else, standing in for the trip of a lifetime.

## The entry

Exactly one emoji, no words, no caption, no explanation:

🗻

## Why this emoji

The judge picks the emoji that most makes a stranger want to book the trip.
🗻 — Mount Fuji — was chosen against that brief, criterion by criterion:

- **It plainly names a dream vacation.** A snow-capped peak is one of the
  brief's own examples of a dream vacation, and this one names a specific
  place: Japan, and the night climb to watch the sunrise — *goraikō* — from
  the summit.
- **It is a postcard at a glance.** White snow, blue sky, a perfect cone —
  a stranger sees the mountain, the cold morning air, and the whole trip
  before reading a word. The emoji is the photograph the trip would send
  home.
- **It is personal and specific, not generic.** It points at one particular
  dream — one mountain, one dawn, one climb — rather than any holiday
  anywhere. Nobody books "a mountain"; people book Fuji.
- **It is a fresh pick.** It skips the obvious beach-and-plane clichés
  (🏖️, ✈️, 🌴) for a mountain that carries the same longing with more
  surprise.
- **It reads instantly, everywhere.** Mount Fuji is one of the most
  recognised silhouettes on earth; it is clear at small size on any screen
  and needs no explaining.

## How the program works

`main.py` is pure Python standard library (`os` and `sys` only). It holds
the single emoji as a constant, validates it first — exactly one character,
one emoji, not whitespace, within the gate's 1–8 characters — then writes
it with no trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or
`/output/entry.txt` when the variable is unset), mode `0644` under umask
`022`. A local `output/` directory is used only as a fallback if the
primary directory cannot be written. `entry.txt` in this repository is
byte-identical to what the program writes.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt   # 🗻
```
