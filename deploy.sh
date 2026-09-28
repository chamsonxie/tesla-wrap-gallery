#!/bin/bash
# Deploy the wrap gallery site to GitHub Pages (new repo).
# Usage: GITHUB_TOKEN=xxx ./deploy.sh
set -e
cd "$(dirname "$0")"
REPO="chamsonxie/tesla-wrap-gallery"

if [ -z "$GITHUB_TOKEN" ]; then echo "set GITHUB_TOKEN first"; exit 1; fi
AUTH="Authorization: Bearer $GITHUB_TOKEN"

echo "== creating repo $REPO"
curl -s -X POST -H "$AUTH" -H "Accept: application/vnd.github+json" \
  https://api.github.com/user/repos \
  -d '{"name":"tesla-wrap-gallery","description":"特斯拉数字车衣皮肤收藏馆 · Tesla digital wrap gallery","private":false,"has_issues":false,"has_wiki":false}' | head -c 300; echo

if [ ! -d .git ]; then git init -b main; fi
git add -A
git -c user.name="muse" -c user.email="muse@local" commit -m "Tesla wrap gallery: 17 skins" --allow-empty || true
git remote remove origin 2>/dev/null || true
git remote add origin "https://x-access-token:$GITHUB_TOKEN@github.com/$REPO.git"
echo "== pushing"
git push -u origin main --force

echo "== enabling Pages"
curl -s -X POST -H "$AUTH" -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/$REPO/pages \
  -d '{"source":{"branch":"main","path":"/"}}' | head -c 300; echo
echo "== done: https://chamsonxie.github.io/tesla-wrap-gallery/"
