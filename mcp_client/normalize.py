def normalize_tool(tool):
    raw = tool.model_dump(mode="json")

    return {
        "name": tool.name,
        "description": tool.description,
        "input_schema": raw.get("input_schema"),
        "output_schema": raw.get("output_schema"),
        "raw_metadata": raw,
    }