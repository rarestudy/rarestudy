import json

print("[process] Starting batch conversion...")

# Read original file
with open('mybatches.json', 'r') as f:
    batches = json.load(f)

# Directly use batches without any encryption
result = []
for batch in batches:
    batch_copy = batch.copy()

    # If MAHAPACK, just copy subBatches as-is
    if batch.get('type') == 'MAHAPACK' and batch.get('subBatches'):
        sub_batches = []
        for sub in batch['subBatches']:
            sub_batches.append(sub.copy())
        batch_copy['subBatches'] = sub_batches

    result.append(batch_copy)

# Write to new file batches.json
with open('batches.json', 'w') as f:
    json.dump({'success': True, 'batches': result}, f, indent=2)

print(f"[process] Done. {len(result)} batches written to batches.json")