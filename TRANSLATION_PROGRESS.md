# MiroFish Chinese → English Translation Progress

## Completed

### Batch 1 — Utilities & small backend files
| File | Chinese lines translated |
|------|--------------------------|
| `backend/app/utils/retry.py` | Docstrings, comments, log messages |
| `backend/app/utils/zep_paging.py` | Module/function docstrings |
| `backend/app/utils/logger.py` | Section comments, docstrings |
| `backend/app/utils/file_parser.py` | Error strings, section headers |
| `backend/app/utils/llm_client.py` | Error strings |
| `backend/app/models/task.py` | Enum comments, status messages |
| `backend/app/models/project.py` | Class/method docstrings, status comments |
| `backend/app/config.py` | Inline comments, validation error strings |
| `backend/run.py` | Console output strings |

### Batch 2 — Infrastructure / config files
| File | Chinese lines translated |
|------|--------------------------|
| `docker-compose.yml` | Mirror image comment |
| `.env.example` | All comment lines |
| `Dockerfile` | All comment lines |

### Batch 3 — Backend API files
| File | Chinese lines translated |
|------|--------------------------|
| `backend/app/api/graph.py` | Module docstring, section headers, all function docstrings, error/response strings, log messages, inline comments |
| `backend/app/api/report.py` | Module docstring, section headers, all function docstrings, error/response strings, log messages, inline comments |
| `backend/app/api/simulation.py` | Module docstring, section headers, all function docstrings, stage names, error/response strings, log messages, inline comments. **Note:** `INTERVIEW_PROMPT_PREFIX` value intentionally kept in Chinese (it's a prompt sent to AI agents). |

### Batch 4 — Non-prompt backend services (partial)
| File | Status |
|------|--------|
| `backend/app/services/graph_builder.py` | Done — class/method docstrings, all inline comments, status messages, error strings |
| `backend/app/services/text_processor.py` | Done — class/method docstrings, inline comments |
| `backend/app/services/simulation_ipc.py` | Done — module docstring, class/method docstrings, log messages, error string, inline comments |
| `backend/app/services/zep_entity_reader.py` | Done — module/class/method docstrings, all log messages, comments |
| `backend/app/services/zep_graph_memory_updater.py` | Done — module/class/method docstrings, all log messages, comments, activity descriptions |
| `backend/app/services/simulation_manager.py` | Done — module/class/method docstrings, all log messages, comments, status strings |

---

## Remaining

### Batch 5 — Core LLM prompt services (semantic translation)
| File | Status |
|------|--------|
| `backend/app/services/ontology_generator.py` | Done — module/class/method docstrings, all LLM prompts (semantic translation), comments |
| `backend/app/services/simulation_config_generator.py` | Done — module/class/method docstrings, all LLM prompts (semantic translation), comments, log messages |
| `backend/app/services/oasis_profile_generator.py` | Done — module/class/method docstrings, all LLM prompts (semantic translation), comments, log messages |
| `backend/app/services/zep_tools.py` | Done — module/class/method docstrings, all LLM prompts (semantic translation), comments, log messages |
| `backend/app/services/report_agent.py` | Done — module/class/method docstrings, all LLM prompts (semantic translation), comments |
| `backend/app/services/simulation_runner.py` | Done — module/class/method docstrings, all comments, log messages |

---

## Remaining

### Batch 6 — Backend scripts
- `backend/scripts/` (5 Python files)

### Batch 7 — Frontend components
- `frontend/src/components/` (7 Vue files)

### Batch 8 — Frontend views, API clients, and docs
- `frontend/src/views/` (Vue files)
- `frontend/src/api/` (JS files)
- `frontend/src/App.vue`
- `frontend/src/main.js`
- `README.md`

---

## Translation rules applied
- Comments, docstrings, log messages, error strings, UI text: literal translation
- LLM prompt strings: **semantic** translation (e.g. "用中文回复" → "Respond in English")
- `INTERVIEW_PROMPT_PREFIX` in `simulation.py`: **kept in Chinese** (it is a Chinese-language prompt sent directly to simulated AI agents)
