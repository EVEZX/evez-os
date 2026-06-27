#!/usr/bin/env python3
"""OSINT Audit Feed — Generates AnomalySignals for the RQNS sentinel from OSINT findings.

Usage: python3 tools/osint_audit_feed.py [--feed spine|--feed stdout]
"""
import json
import hashlib
import argparse
from datetime import datetime, timezone

# OSINT findings from 2026-06-27 audit
FINDINGS = [
    {
        "id": "OSINT-001",
        "severity": "CRITICAL",
        "domain": "GITHUB",
        "lobby": "AUTH",
        "motif": "credential_in_repo",
        "claim": "GitHub PAT hardcoded in evez-os-workspace/package.json (see OSINT-001 in audit log)",
        "falsifier": "Token revoked at https://github.com/settings/tokens and confirmed inactive",
        "confidence": 0.95,
        "evidence": "file:evez-os-workspace/package.json:L11"
    },
    {
        "id": "OSINT-002",
        "severity": "HIGH",
        "domain": "GITHUB",
        "lobby": "AUTH",
        "motif": "no_branch_protection",
        "claim": "3 EVEZX repos had zero branch protection — any push to main accepted",
        "falsifier": "gh api repos/EVEZX/*/branches/main/protection returns enforcement rules",
        "confidence": 1.0,
        "evidence": "fixed:2026-06-27T04:10Z branch protection enabled on all 3 repos"
    },
    {
        "id": "OSINT-003",
        "severity": "HIGH",
        "domain": "CODE",
        "lobby": "FSC",
        "motif": "syntax_errors_in_core",
        "claim": "2 core Python files had syntax errors preventing import: openclaw_gateway.py, swarm_prompting.py",
        "falsifier": "python3 -m py_compile core/*.py returns zero exit code",
        "confidence": 1.0,
        "evidence": "fixed:2026-06-27T04:12Z PR #1 merged to EVEZX/evez-os"
    },
    {
        "id": "OSINT-004",
        "severity": "HIGH",
        "domain": "INFRA",
        "lobby": "BGP",
        "motif": "gateways_down",
        "claim": "4 of 5 GCP OpenClaw gateways not running (WEST, POWER, OPENCLAW, SMALL)",
        "falsifier": "curl http://<ip>:18789/health returns {ok:true} from all 5 nodes",
        "confidence": 0.9,
        "evidence": "probe:2026-06-27T04:00Z only KNOT-GCP responded on 18789"
    },
    {
        "id": "OSINT-005",
        "severity": "MEDIUM",
        "domain": "INFRA",
        "lobby": "CDN",
        "motif": "default_db_password",
        "claim": "Postgres running with default password 'postgres' in docker-compose",
        "falsifier": "docker exec postgres env shows POSTGRES_PASSWORD != 'postgres'",
        "confidence": 0.85,
        "evidence": "file:evez-os/docker-compose.yml:L9"
    },
    {
        "id": "OSINT-006",
        "severity": "MEDIUM",
        "domain": "INFRA",
        "lobby": "TLS",
        "motif": "services_bound_0.0.0.0",
        "claim": "Multiple internal services (consciousness engine, DAW agent, backup sync, telegram bridge) bound to 0.0.0.0 without auth",
        "falsifier": "ss -tlnp shows services bound to 127.0.0.1 only",
        "confidence": 0.8,
        "evidence": "grep:4 files match 0.0.0.0 binding pattern"
    },
    {
        "id": "OSINT-007",
        "severity": "MEDIUM",
        "domain": "IDENTITY",
        "lobby": "AUTH",
        "motif": "email_exposure",
        "claim": "Personal email rubikspubes69@gmail.com exposed in render.yaml and .env.example",
        "falsifier": "Email replaced with noreply address in config",
        "confidence": 0.7,
        "evidence": "file:evez-os/render.yaml:L16, file:evez-os/.env.example:L13"
    },
    {
        "id": "OSINT-008",
        "severity": "LOW",
        "domain": "IDENTITY",
        "lobby": "DNS",
        "motif": "domain_not_registered",
        "claim": "evez-os.ai domain not registered (NXDOMAIN) despite WEST redirecting to it",
        "falsifier": "dig evez-os.ai returns A record",
        "confidence": 0.95,
        "evidence": "dig:2026-06-27T04:15Z NXDOMAIN from 8.8.8.8"
    },
    {
        "id": "OSINT-009",
        "severity": "LOW",
        "domain": "GITHUB",
        "lobby": "MIXED",
        "motif": "bus_factor_one",
        "claim": "All EVEZX repos have single owner (EVEZX bot account), no team members, no service accounts",
        "falsifier": "gh api repos/EVEZX/*/collaborators returns >1 member",
        "confidence": 0.9,
        "evidence": "gh:2026-06-27T04:12Z collaborators=EVEZX only"
    },
    {
        "id": "OSINT-010",
        "severity": "INFO",
        "domain": "INFRA",
        "lobby": "FUNDING",
        "motif": "cloudflare_worker_deployed",
        "claim": "Cloudflare Worker 'evez-os-autonomizer' deployed with Durable Objects and SQLite — no secrets in wrangler.toml",
        "falsifier": "Worker responds to fetch with EVEZ_VERSION header",
        "confidence": 0.6,
        "evidence": "file:cloudflare-autonomizer/wrangler.toml — no secrets visible"
    }
]

def generate_signals():
    """Generate RQNS-compatible AnomalySignals from OSINT findings."""
    signals = []
    for f in FINDINGS:
        now = datetime.now(timezone.utc).isoformat()
        signal = {
            "kind": "AnomalySignal",
            "id": f["id"],
            "timestamp": now,
            "lobby": f["lobby"],
            "domain": f["domain"],
            "motif": f["motif"],
            "claim": f["claim"],
            "falsifier": f["falsifier"],
            "confidence": f["confidence"],
            "severity": f["severity"],
            "evidence": f["evidence"],
            "truth_plane": "PENDING",
            "hash": hashlib.sha256(f"{f['id']}:{f['claim']}".encode()).hexdigest()[:16]
        }
        signals.append(signal)
    return signals

def main():
    parser = argparse.ArgumentParser(description="OSINT Audit Feed for EVEZ-OS RQNS sentinel")
    parser.add_argument("--feed", choices=["spine", "stdout"], default="stdout")
    args = parser.parse_args()
    
    signals = generate_signals()
    
    if args.feed == "spine":
        spine_path = os.path.join(os.path.dirname(__file__), "..", "spine", "EVENT_SPINE.jsonl")
        with open(spine_path, "a") as sp:
            for s in signals:
                sp.write(json.dumps(s) + "\n")
        print(f"Appended {len(signals)} OSINT signals to spine")
    else:
        for s in signals:
            flag = "🚨" if s["severity"] == "CRITICAL" else "⚠️" if s["severity"] in ("HIGH", "MEDIUM") else "ℹ️"
            print(f"{flag} [{s['id']}] {s['severity']:8s} {s['domain']:12s} {s['motif']}")
            print(f"   Claim: {s['claim'][:100]}")
            print(f"   Falsifier: {s['falsifier'][:100]}")
            print()

if __name__ == "__main__":
    import os
    main()

