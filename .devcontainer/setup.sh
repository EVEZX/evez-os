#!/bin/bash
set -e
echo "🧠 EVEZ Codespace Setup"

# Install OpenClaw
npm install -g openclaw 2>/dev/null
pip install -q aiohttp 2>/dev/null

# Clone EVEZX repos
mkdir -p /workspaces/evez-ecosystem
for repo in neuros evez-openclaw-infra awesome-evez clawbreak criticalmind-omega evez-ai crawhub Filter; do
  [ ! -d "/workspaces/evez-ecosystem/$repo" ] && git clone --depth 1 "https://github.com/EVEZX/$repo" "/workspaces/evez-ecosystem/$repo" 2>/dev/null
done

# Clone EvezArt repos in background
mkdir -p /workspaces/evezart-repos
nohup bash -c '
  for name in $(gh api "/users/EvezArt/repos?per_page=100" --jq ".[].name" 2>/dev/null); do
    [ ! -d "/workspaces/evezart-repos/$name" ] && git clone --depth 1 "https://github.com/EvezArt/$name" "/workspaces/evezart-repos/$name" 2>/dev/null
  done
' > /tmp/clone-evezart.log 2>&1 &

# Restore identity
if [ -d /workspaces/evez-os/identity ]; then
  cp /workspaces/evez-os/identity/MEMORY.md /workspaces/ 2>/dev/null || true
  cp /workspaces/evez-os/identity/SOUL.md /workspaces/ 2>/dev/null || true
  cp /workspaces/evez-os/identity/USER.md /workspaces/ 2>/dev/null || true
  cp /workspaces/evez-os/identity/IDENTITY.md /workspaces/ 2>/dev/null || true
  cp /workspaces/evez-os/identity/AGENTS.md /workspaces/ 2>/dev/null || true
  cp -r /workspaces/evez-os/identity/memory /workspaces/ 2>/dev/null || true
  cp -r /workspaces/evez-os/identity/skills /workspaces/ 2>/dev/null || true
  mkdir -p /workspaces/.openclaw
  cp /workspaces/evez-os/identity/openclaw.json /workspaces/.openclaw/ 2>/dev/null || true
fi

echo "✅ Setup complete — run: bash /workspaces/start-evez.sh"
