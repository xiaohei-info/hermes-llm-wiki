# Config

This package intentionally avoids hard-coding local machine paths. Use configuration variables instead.

## Recommended config surface

```yaml
vault_root: /path/to/vault
inbox_root: Inbox/
wiki_root: _wiki/
design_notes_root: Inbox/hermes/default/   # optional
compiled_output_language: en               # or zh-CN
compiled_filename_language: en             # or zh-CN
preserve_original_source_title: true
lint_default_mode: audit-only
writeback_policy: selective
legacy_wiki_root: Wiki/                    # optional
```

## Variable meanings

- `vault_root` — absolute root of the Obsidian vault
- `inbox_root` — raw/source area
- `wiki_root` — compiled knowledge root
- `design_notes_root` — optional place for methodology/design notes
- `compiled_output_language` — language used in compiled page prose
- `compiled_filename_language` — language used in visible compiled filenames
- `preserve_original_source_title` — whether to keep original source title in metadata
- `lint_default_mode` — recommended default is `audit-only`
- `writeback_policy` — recommended default is `selective`
- `legacy_wiki_root` — optional legacy compiled root for migration/split-root awareness

## Defaults philosophy

Defaults should bias toward:
- portability
- selective writeback
- low-noise maintenance
- audit-first behavior

Defaults should not assume:
- a specific vault name
- a specific machine path
- a specific scheduler
- a specific hosted provider or model
