# PLAYTHROUGH (projection) — EP-20260627-040456-42

This file is a **mutable projection**. The spine events are immutable. Each step cites a `trace_id` you can grep in `spine/EVENT_SPINE.jsonl`.

## Step 1 — BGP / route ghost
- trace_id: `T083c3a94499142a6`
- truth_plane: `pending`
- claim: In BGP, a failure may present as: route ghost.
- falsifier: same AS-path + reachability from all vantages
- proposed_probe: multi-vantage traceroute

## Step 2 — DNS / naming fork
- trace_id: `T66746fd40d3885a6`
- truth_plane: `pending`
- claim: In DNS, a failure may present as: naming fork.
- falsifier: authoritative answer matches across resolvers
- proposed_probe: compare resolvers + TTL

## Step 3 — AUTH / clock skew gate
- trace_id: `Te530fd87f65abe82`
- truth_plane: `pending`
- claim: In AUTH, a failure may present as: clock skew gate.
- falsifier: no skew; token valid everywhere
- proposed_probe: compare token iat/exp vs server time

## Step 4 — CDN / echo hall
- trace_id: `T6db2d021c92cc203`
- truth_plane: `pending`
- claim: In CDN, a failure may present as: echo hall.
- falsifier: origin and edge agree on freshness
- proposed_probe: inspect cache headers + bypass key

## Step 5 — CDN / echo hall
- trace_id: `Td3a6683af418e411`
- truth_plane: `pending`
- claim: In CDN, a failure may present as: echo hall.
- falsifier: origin and edge agree on freshness
- proposed_probe: inspect cache headers + bypass key

## Step 6 — TLS / identity court
- trace_id: `T95ef5d58efabb13f`
- truth_plane: `pending`
- claim: In TLS, a failure may present as: identity court.
- falsifier: chain ok and time stable
- proposed_probe: validate chain + OCSP + time

## Step 7 — BGP / route ghost
- trace_id: `T23a929502dd3aea3`
- truth_plane: `pending`
- claim: In BGP, a failure may present as: route ghost.
- falsifier: same AS-path + reachability from all vantages
- proposed_probe: multi-vantage traceroute

## Step 8 — FUNDING / USD checkpoint
- trace_id: `Tb9c78ad647aaa59b`
- truth_plane: `pending`
- claim: In FUNDING, a failure may present as: USD checkpoint.
- falsifier: no snapshot; claim rejected
- proposed_probe: require FX snapshot asset + provenance

## Step 9 — BGP / route ghost
- trace_id: `T90a58c623cdb14ce`
- truth_plane: `pending`
- claim: In BGP, a failure may present as: route ghost.
- falsifier: same AS-path + reachability from all vantages
- proposed_probe: multi-vantage traceroute

## Step 10 — FSC / confidence outruns falsifier
- trace_id: `Tbd5641ac166167e7`
- truth_plane: `pending`
- claim: In FSC, a failure may present as: confidence outruns falsifier.
- falsifier: falsifier provided; claim demoted/updated
- proposed_probe: compress narrative; demand falsifier

## Step 11 — MIXED / symptom impersonation
- trace_id: `Te98b2fde27f5abbf`
- truth_plane: `pending`
- claim: In MIXED, a failure may present as: symptom impersonation.
- falsifier: layer attribution stable across tests
- proposed_probe: separate layers with discriminating tests

## Step 12 — DNS / naming fork
- trace_id: `Tcf3a0cab9af5dde4`
- truth_plane: `pending`
- claim: In DNS, a failure may present as: naming fork.
- falsifier: authoritative answer matches across resolvers
- proposed_probe: compare resolvers + TTL

## Step 13 — DNS / naming fork
- trace_id: `T06b7b95fdc9ef856`
- truth_plane: `pending`
- claim: In DNS, a failure may present as: naming fork.
- falsifier: authoritative answer matches across resolvers
- proposed_probe: compare resolvers + TTL

## Step 14 — BGP / route ghost
- trace_id: `Tdaefdd41194ebe61`
- truth_plane: `pending`
- claim: In BGP, a failure may present as: route ghost.
- falsifier: same AS-path + reachability from all vantages
- proposed_probe: multi-vantage traceroute

---

### HUD tail (what the prompter should watch)
- If your confidence rises, your falsifier must rise too.
- If a claim can’t be broken on purpose, it’s theater.
- The map begins when the mapper is mapped.
