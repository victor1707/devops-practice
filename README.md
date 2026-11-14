# DevOps practice

One tiny app, carried through git → GitHub → Jenkins → Kubernetes. Do one lesson at a time; each ends with a check.

| # | Lesson | Do | Check |
|---|--------|----|-------|
| 1 | Git basics | `git init`, commit everything, make a branch `feature/version`, change `message()`, commit, merge to `main` | `git log --oneline --graph` shows the merge |
| 2 | GitHub | create empty repo, `git remote add origin …`, push; open a PR from a new branch, merge it on GitHub, `git pull` | PR shows as merged; local `main` matches |
| 3 | Docker | do the Dockerfile TODO; `docker build -t devops-practice:local .`; `docker run -p 8080:8080 devops-practice:local` | `curl localhost:8080` shows your version |
| 4 | Jenkins | on your Jenkins VM: Pipeline job → "Pipeline script from SCM" → your GitHub repo; do Build/Push TODOs | build is green; image is on Docker Hub |
| 5 | Kubernetes | on kind: `kind load docker-image devops-practice:local`; do deployment TODOs; `kubectl apply -f k8s/` | `kubectl port-forward svc/devops-practice 8080:80` then `curl localhost:8080` |
| 6 | Full CD | do the Deploy TODO (give Jenkins a kubeconfig credential); add a GitHub webhook | push a commit → new version live without touching anything |

Bonus breakages to fix yourself: create a merge conflict on purpose; make the test fail and watch Jenkins go red; set a wrong image tag and read `kubectl describe pod`.

Run locally: `python3 test_app.py && python3 app.py`
