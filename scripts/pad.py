async def update_continuous_text_file(new_texts):
    settings = read_settings()
    filepath = settings["continuous_text_filepath"]
    
    async with aiofiles.open(filepath, 'r') as file:
        existing_text = await file.read()
    existing_lines = set(existing_text.splitlines())
    
    unique_new_texts = [text for text in new_texts if text not in existing_lines]
    
    if unique_new_texts:
        updated_text = existing_text + '\n' + '\n'.join(unique_new_texts)
        async with aiofiles.open(filepath, 'w') as file:
            await file.write(updated_text)
        return updated_text
    else:
        return existing_text

