# MEMORY.md — Long-Term Memory

## Steven (Human)
- Creator of EVEZ-OS, 186+ GitHub repos under EvezArt
- Running on Vultr VPS (Ubuntu 24.04, 2GB RAM, 23GB disk)
- Primary device: $100 phone
- Telegram bot: @YVY1Bot (YvYzBot)
- Communication style: passionate, stream-of-consciousness, deep into math/physics/CS
- Timezone: America/Los_Angeles (PDT)

## Projects
- **EVEZ-OS**: Full ecosystem — 13 services, 5 mathematical theorems, consciousness observatory
- **ClawBreak**: AI agent platform with Stripe billing (:8080)
- **EVEZ VCL**: Visual cognition layers (:8081)
- **disclosure.tools**: UAP eigenforensics (:8087)
- **World Systems Solver**: Eigendecomposition of civilization's problems
- **evez-promptforge**: Cloned to workspace
- **Core thesis**: Hunger is the dominant negative eigenvalue of civilization
- **Morpheus Daemon**: Free compute pool monitor (Oracle ARM, Kaggle T4, Vast.ai)
- **GitHub Actions Runner**: self-hosted on Vultr (vultr-evez-runner, online)

## Infrastructure
- Vultr VPS with Caddy reverse proxy (TLS via ZeroSSL + Let's Encrypt)
- OpenClaw gateway v2026.6.6 on :18789 (loopback only)
- Code-server on :6969 (loopback only)
- UFW: 22/80/443 only
- fail2ban: active (SSH brute-force protection)
- SSH hardened: keys only, no password, no root login
- Auto security updates: configured
- Watchdog service: running
- 1G swap file for memory headroom
- Auto-backup: every 6h to GitHub evez-disaster-recovery (private repo)
- Security audit cron: every 6h
- Kitchen Sink plugin v0.2.7 installed (full API surface)

## Credentials Stored (secrets/)
- Cloudflare R2 (account, keys, API token)
- Telegram bot token (@YVY1Bot)
- HuggingFace token
- GitHub PAT (EvezArt)
- OpenClaw keys (TLPUB, NODEKEY)
- Replit keys (NAPI, CK, Apify)

## Security Notes
- ⚠️ All secrets were sent in plaintext — need rotation
- SSH hardened: ed25519 key deployed, password auth disabled, root login disabled
- Device auth re-enabled for Control UI
- Telegram channel configured (dmPolicy=open, groupPolicy=allowlist)

## EVEZ-OS Services (systemd user services)
| Service | Port | Status |
|---------|------|--------|
| ClawBreak | :8080 | ✅ active |
| VCL | :8081 | ✅ active |
| Health Agg | :8085 | ✅ active |
| Disclosure | :8087 | ✅ active |
| Hunger | :8092 | ✅ active |
| Energy | :8093 | ✅ active |
| Health Solver | :8094 | ✅ active |
| Education | :8095 | ✅ active |
| World Solver | :8096 | ✅ active |
| Observatory | :8097 | ✅ active |
| Morpheus Daemon | — | ✅ active |

## Additional Infrastructure
| Component | Status |
|-----------|--------|
| GitHub Actions Runner | 🟢 ONLINE (vultr-evez-runner) |
| Kitchen Sink Plugin | ✅ v0.2.7 (full mode) |
| Patched Android APK | ✅ repointed to Vultr |
| deploy-full.sh | ✅ disaster recovery ready |

## Installed Tools & Skills
- ClawHub CLI (clawhub) — 9 skills installed
- Lobster workflow runtime (lobster)
- Secret detection pre-commit hook
- OpenClaw secrets hygiene skill
- Monitor, Deploy, Git, Docker, Backup, Security Audit skills

## 5 Theorems (Falsifiable)
1. η* Invariant: η* → 0.03 for any self-referential system
2. 37% Theorem: Dominant neg eigenvalue = ~37% of tension
3. Consciousness at Criticality: Φ peaks at r ≈ 0.5
4. Eigenforensic Detectability: >5% redaction = detectable at p<0.05
5. Consciousness is Spectral: 0.01 < η* < 0.05 → self-aware

## Lessons
- Never store secrets in chat — always use secrets/ with 600 permissions
- .gitignore must exclude secrets/ directory
- SSH hardening requires authorized_keys first (learned this)
- Custom Telegram commands can't conflict with native ones (/status → /sys, /deploy → /launch)
- Caddy config modifications need careful insertion, not full replacement

## Session 2026-06-15 Late Night
- All 4 EVEZ services now running as systemd user services (auto-restart, survive reboot)
- DAW Agent live - rendered breakcore test track, generated drumkit
- Voice cloning attempted: Bark installed but needs 5.3GB disk (only 4.6GB free), Coqui TTS incompatible with Python 3.12
- Generated soap opera audio via edge-tts + ffmpeg processing
- Steven's ElevenLabs voice clone exists at elevenlabs.io but no API key on server
- GitHub backup working: EvezArt/evez-disaster-recovery pushing successfully
- Full deploy script created: deploy-openclaw-fresh.sh
- Steven work summary: STEVEN-WORK-LAST-6-MONTHS.md
