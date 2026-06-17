#!/bin/bash
# EVEZ Codespace Setup Script
# Run this in GitHub Codespace to start EVEZ services

echo "=== EVEZ Codespace Bootstrap ==="

# Install dependencies
pip install aiohttp aiosqlite 2>/dev/null

# Clone EVEZ provider
if [ ! -d ~/evez-provider ]; then
  git clone https://github.com/EVEZX/evez-provider-deploy ~/evez-provider
fi

# Set environment variables
export VULTR_API_KEY="${VULTR_API_KEY:-placeholder}"
export OPENROUTER_API_KEY="${OPENROUTER_API_KEY:-placeholder}"
export GROQ_API_KEY="${GROQ_API_KEY:-placeholder}"
export HUGGINGFACE_API_KEY="${HUGGINGFACE_API_KEY:-placeholder}"

# Start EVEZ Provider on port 9100
cd ~/evez-provider
nohup python3 provider/gateway-v2.py &
echo "EVEZ Provider started on port 9100"

# Start Arena on port 9800
cd ~/evez-arena 2>/dev/null || true
# (Arena code would be here)

echo "=== EVEZ Codespace Ready ==="
echo "Ports forwarded automatically by Codespaces"
