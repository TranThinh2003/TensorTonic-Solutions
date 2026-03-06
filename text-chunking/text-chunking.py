"""
 *     author:  Shinomiyaaa
 *     created: 06.03.2026 08:15:31
"""
def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    if not tokens: return []
    if len(tokens) <= chunk_size: return [tokens]
    step = chunk_size - overlap
    chunks = []
    for i in range(0, len(tokens) - chunk_size + 1, step):
        chunk = tokens[i : i + chunk_size]
        chunks.append(chunk)
    return chunks
    