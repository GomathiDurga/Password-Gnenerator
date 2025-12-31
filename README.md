# 🔐 Smart Password Generator

**Secure CLI password generator** with strength rating. Uses `secrets` module (cryptographically secure).

## Features
- ✨ Custom length + character types
- 🏷️ Strength rating: Weak/Medium/Strong
- 🔒 `secrets` module (not `random`)
- ✅ Guarantees 1 of each selected type


## Strength Criteria
| Rating | Length | Character Types |
|--------|--------|-----------------|
| **Weak** | <8 | ≤1 type |
| **Medium** | ≥8 | 2-3 types |
| **Strong** | ≥12 | All 4 types |

## Commands / Prompts
| Step | Input | Options |
|------|-------|---------|
| Length | Enter number | `12`, `16`, `20+` |
| Lowercase | `y/n` | `y` (a-z), `n` |
| Uppercase | `y/n` | `y` (A-Z), `n` |
| Digits | `y/n` | `y` (0-9), `n` |
| Symbols | `y/n` | `y` (!@#$...), `n` |

## Tech Stack
- Python 3.x + `secrets` (cryptographic)
- `string` module
- Input validation + error handling

## Setup & Run
```bash
python smart_password_generator.py

