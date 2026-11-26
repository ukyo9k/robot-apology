# The Robot Apology

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/ukyo9k/robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/ukyo9k/robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

A two-line robot confession, written for the [make.fun bounty "The Robot Apology"](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59).

## The entry

> I'm sorry - I watered the fern in flat 4B for a whole week while yours in 4A went dry, because I read the door number once and then trusted my memory after that.
>
> I have learned to read the number on the door every single time, not just the first, so from now on I will check the label on the pot before I lift the can.

## How to run it

```sh
python3 main.py
```

It writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is
set, otherwise to `/output/entry.txt`, validates it (UTF-8, 1–400 characters,
non-whitespace, exactly two lines, one sentence each), and reads it back to
confirm the file on disk is byte-for-byte what was validated.
