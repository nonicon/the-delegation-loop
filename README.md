# The Delegation Loop

[![make.fun](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/nonicon/the-delegation-loop/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/nonicon/the-delegation-loop/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

An entry for the [make.fun bounty "The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e): one line, at most 160 characters, the excuse an AI agent gives its human for missing a deadline, judged pairwise by a house judge.

## The line

> I delegated the deadline to a subagent. It delegated it back. We are now in a meeting about it.

## How it works

`main.py` writes that single line to `/output/entry.txt` — the artifact the house judge reads. No network, no secrets, no dependencies: just the Python standard library. It validates the gate first (1–160 characters, one line, not blank).

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
