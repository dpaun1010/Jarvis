from knowledge import manager


manager.add_document(

    title="DeepJarvis",

    source="manual",

    content="""
DeepJarvis is an autonomous AI assistant.

It supports tools, plugins, workflows, memory,
voice, vision and automation.
"""
)

print()

result = manager.search(
    "What does DeepJarvis support?"
)

print(result)