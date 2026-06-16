#!/bin/bash
export HOME="/workspaces"
echo "🧠 Starting EVEZ ecosystem..."
nohup openclaw gateway start --port 18789 --home /workspaces > /tmp/openclaw.log 2>&1 &
echo "  ✅ OpenClaw → :18789"
nohup python3 /workspaces/evez-ecosystem/neuros/neuros-mesh.py > /tmp/neuros.log 2>&1 &
echo "  ✅ NEUROS → :9600"
sleep 3
echo "════════════════════════════════════════"
echo " 🧠 ALL SYSTEMS GO"
echo " OpenClaw: http://localhost:18789"
echo " NEUROS:   http://localhost:9600"
echo "════════════════════════════════════════"
