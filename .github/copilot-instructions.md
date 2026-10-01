# HerVoice: project instructions

## Goal
HerVoice is a voice-first AI guide that helps a first-time woman user in India
(no English, no tech background, no one to ask) independently access ONE
government scheme (PM Ujjwala Yojana) in her own language. It must require
zero prior digital knowledge. Hackathon challenge: "The Invisible Woman".

## Hard requirements
1. No reading needed: one big mic button, icons, every reply spoken AND captioned.
2. Voice OR simple text input. Multilingual: detect the user's language and
   reply in it. Supported: hi-IN, ta-IN, te-IN, bn-IN, mr-IN, kn-IN (list in config.py).
3. Gemini (google-genai SDK) turns speech/text into structured answers and
   phrases replies in simple language. Eligibility is decided ONLY by the
   deterministic rules.py, never by the LLM.
4. Replies must be grounded only in data/schemes/ujjwala.json. Never invent
   scheme facts. Leave `TODO: verify from official source` where unsure.
5. Stack (NO PAID SERVICES, NO BILLING ACCOUNT): Python 3.12, FastAPI, Pydantic,
   vanilla HTML/CSS/JS frontend, Gemini via a free Google AI Studio API key
   read from the GEMINI_API_KEY env var (model name from GEMINI_MODEL; look up
   the current model ID in the docs). Speech input: send recorded audio
   directly to Gemini. Speech output: browser speechSynthesis in the detected
   language. Do not use Cloud Run, Cloud Text-to-Speech, Secret Manager, or any
   billing-gated service.
6. Stateless server. NO database, NO login. Never store audio or personal data.
7. Deployment: Docker container listening on $PORT (default 7860) so it runs
   on Hugging Face Spaces (Docker) or Render free tier. Keep it portable to
   Cloud Run later.

## Quality bar (an AI evaluator scores these)
Type hints, ruff/black, pytest with Gemini mocked, security headers, input
validation, rate limiting, ARIA labels, lang attributes, high contrast,
48px+ touch targets, no secrets in code (env vars only), pinned requirements,
.env.example, README with a "Problem Statement Alignment" table. Every module
has a docstring naming the requirement it serves.

## Structure
app/ (main.py, routes.py, schemas.py, config.py, gemini_service.py,
rules.py, security.py), data/schemes/ujjwala.json, static/, tests/,
Dockerfile, requirements.txt, .env.example, README.md

## Rules for you
- Do NOT add logins, databases, extra schemes, paid services, or unrequested features.
- Work one milestone at a time. After each, stop and wait for my review.
- Keep the app deployable after every step.
