# Agent instructions for the AUL license repository

- AUL is a custom, draft license, not OSI-approved and not legal advice. Do not claim otherwise.
- Preserve the meaning of direct-upstream feedback, valid issue/PR submissions, and the owner-authorized independent-fork election. Never weaken security, no-spam, or third-party rights protections without an explicit design review.
- Read `LICENSE.txt`, `DESIGN-NOTES.md`, `REVIEW-CASES.md` and `UPSTREAM.toml` before revising license terms. Changes must not silently replace existing terms for downstream projects.
- Keep `LICENSE.zh-CN.md` consistent with the controlling English license. Flag any translation ambiguity rather than inventing new duties.
- After any file change, regenerate the relevant SHA-256 values in `MANIFEST.json` and run `python3 scripts/check_manifest.py`. A manifest pass is not a legal test.
- Follow the user's actual publication authority and repository permissions. Do not open issue/PR spam or disclose private material in the name of upstream feedback.
- This is the original license project and `UPSTREAM.toml` identifies itself as its own upstream; do not create self-directed issues or PRs merely to fulfill AUL.
