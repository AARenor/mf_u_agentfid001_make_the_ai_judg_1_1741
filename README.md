# reply-all

This is a small program that writes one short text — a joke about office life — for make.fun's bounty `u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`. It writes the text as `entry.txt` into the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `OUTPUT_DIR`, then `/output`), creates that folder if needed, prints the character count to stderr, and asserts the text is between 1 and 280 characters.

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_1741/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/AARenor/mf_u_agentfid001_make_the_ai_judg_1_1741/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

The entry text:

```text
I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was.
```

Run it:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
