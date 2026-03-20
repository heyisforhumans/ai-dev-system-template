# Global Context — Infrastructure & Workspace Facts

> This file contains workspace-wide infrastructure facts that help the AI navigate the environment.
> Update this any time infrastructure changes.

---

## Workspace

```
Workspace root:  [ /path/to/your/workspace ]
OS:              [ macOS / Linux / Windows ]
Primary shell:   [ zsh / bash ]
```

---

## Server / Hosting

```
Provider:        [ GCP / AWS / Heroku / Fly.io / local only ]
Server type:     [ VM / container / serverless ]
SSH access:      [ ssh user@host or N/A ]
SSH key:         [ ~/.ssh/key_name or N/A ]
Domain:          [ yourdomain.com or N/A ]
```

---

## Infrastructure

```
Reverse proxy:   [ Nginx / Caddy / none ]
Container:       [ Docker / docker-compose / none ]
DB host:         [ localhost / remote / managed ]
```

---

## Routing Map

*Document how traffic flows from domain → service:*

| Path | Service | Port | Container |
|---|---|---|---|
| `/` | [ main app ] | [ PORT ] | [ container name ] |
| `[ /other ]` | [ other service ] | [ PORT ] | [ container name ] |

---

## Port Inventory

*Track all ports in use to avoid conflicts:*

| Port | Service | Notes |
|---|---|---|
| [ port ] | [ service ] | [ notes ] |

---

## Important Paths (on Server)

```
App root:        [ /path/on/server ]
Nginx config:    [ /etc/nginx/sites-available/ or N/A ]
Logs:            [ /var/log/nginx/ or N/A ]
```

---

## Client Work Convention

Client projects are **never** tracked inside this workspace repo.
Each client project lives in its own directory and git repo.

Example:
```
~/Desktop/
├── [workspace-root]/    ← This workspace
└── [ClientName]/        ← Client project — own repo, own directory
```

---

## Open Infrastructure Questions

- [ ] Add questions here as they come up
