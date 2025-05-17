# test-sphinx
Sphinx Python documentation test

## Dev
### Package Management
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync --all-groups
```

```bash
uv add `パッケージ名`
uv export --no-annotate --no-hashes --no-header -o requirements.txt
```
