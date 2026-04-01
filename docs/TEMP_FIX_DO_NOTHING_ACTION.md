# Temporary Fix: Remove DO_NOTHING Action (OASIS Schema Bug)

## Problem

The OASIS/CAMEL library's `DO_NOTHING` action has a malformed JSON schema that OpenAI's API now rejects:

```
openai.BadRequestError: Error code: 400 - {'error': {'message': "invalid JSON schema for tool do_nothing, tools[4].function.parameters: 'required' present but 'properties' is missing"}}
```

This caused simulation startup failures with exit code 1.

## Temporary Fix Applied

Removed `ActionType.DO_NOTHING` from available actions in `backend/scripts/run_parallel_simulation.py`:

- **TWITTER_ACTIONS**: Removed DO_NOTHING (line 183)
- **REDDIT_ACTIONS**: Removed DO_NOTHING (line 199)

## Impact

**Downsides:**
- Agents can no longer "pass" their turn
- May increase action volume (agents must take active actions)
- Could reduce behavioral realism in some scenarios

**Benefits:**
- Simulation runs without crashing
- More activity data for reports
- Unblocks testing and development

## When to Remove This Fix

This is a **TESTING-ONLY WORKAROUND**. Remove when:
1. OASIS library releases a patch for the JSON schema bug
2. You upgrade to a fixed version of `oasis-ai` or `camel-ai`
3. You implement a proper fix in the library itself

## Proper Long-Term Fix

The correct fix is in the OASIS library's tool schema generation. The `do_nothing` tool should either:
- Have an empty `properties: {}` object, OR
- Have `required: []` removed from the schema

Track: https://github.com/camel-ai/oasis (or relevant OASIS repo) for upstream fixes.

## Bug Fix Summary

| Bug | Cause | Fix |
|-----|-------|-----|
| Simulation crashes immediately | do_nothing tool has invalid OASIS JSON schema | Removed ActionType.DO_NOTHING from both action lists |
| Reddit hangs/crashes mid-run | trend tool has same invalid JSON schema | Removed ActionType.TREND from Reddit actions |
| Frontend stuck on "Running" forever | Dead code: early continue on line 614 skipped ALL event_type processing, so simulation_end was never detected | Removed the premature continue so simulation_end events now correctly mark simulation as completed |

---
*Applied: April 2026 | Status: Temporary Testing Workaround*
